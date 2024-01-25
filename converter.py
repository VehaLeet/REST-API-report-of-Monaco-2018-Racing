from peewee import *
from racing_report import racing_report
import argparse
from models import Driver, database_proxy


def convert_from_files_to_db(files_folder, db_file):
    db = SqliteDatabase(f'{db_file}.db')
    database_proxy.initialize(db)

    database_proxy.create_tables([Driver])

    from_files = racing_report.build_report(files_folder)
    for key, value in from_files.items():
        Driver.create(name=value['name'],
                      abbreviation=value['abbreviation'],
                      car=value['car'],
                      lap_time=value['lap_time'])

    return Driver.select().count()


def convert_from_db():
    result = {}
    for driver in Driver.select():
        result[driver.abbreviation] = {
            "name": driver.name,
            "abbreviation": driver.abbreviation,
            "car": driver.car,
            "lap_time": driver.lap_time
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Convert data from files to database."
    )

    parser.add_argument('--files')
    parser.add_argument('--db')
    args = parser.parse_args(argv)

    return convert_from_files_to_db(args.files, args.db)


if __name__ == '__main__':
    main()









