import os
from datetime import datetime
import argparse


def __datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d_%H:%M:%S.%f')


def read_abb(file_path: str) -> dict:
    with open(file_path) as f:
        result = {}
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            abb, name, car = line.split('_')
            result[abb] = {
                "name": name,
                "abbreviation": abb,
                "car": car,
            }
        return result


def read_log(file_path: str) -> dict:
    with open(file_path) as f:
        result = {}
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            abb, date_time = line[:3], line[3:]
            result[abb] = __datetime(date_time)
        return result


def build_report(folder_path: str) -> dict:
    racers_info = read_abb(os.path.join(folder_path, 'abbreviations.txt'))
    start_time = read_log(os.path.join(folder_path, 'start.log'))
    end_time = read_log(os.path.join(folder_path, 'end.log'))

    result = {}
    for abb, info in racers_info.items():
        info["lap_time"] = str(abs(end_time[abb] - start_time[abb]))
        result[abb] = info
    return result


def sort_report(report: dict, order: bool) -> dict:
    return dict(sorted(
        report.items(),
        key=lambda x: x[1]["lap_time"],
        reverse=not order,
    ))


def driver_info(report: dict, name: str) -> dict:
    return {key: val for (key, val) in report.items() if val['name'] == name}


def print_driver_info(report: dict):
    for key_o, value_o in report.items():
        print(f"{value_o['name']:{25}} | {value_o['car']:{25}} | {value_o['lap_time']}")


def print_report(report: dict):
    for num, (key, value) in enumerate(report.items(), start=1):
        print(f"{num}.{value['name']:{25}} | {value['car']:{25}}  |  {value['lap_time']}")
        if num == 15:
            print('-' * 80)


def main(argv=None):
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Empty"
    )
    parser.add_argument("--file")
    parser.add_argument("--driver")
    parser.add_argument("--asc", action='store_true', dest='order')
    parser.add_argument("--desc", action='store_false', dest='order')
    args = parser.parse_args(argv)

    if args.file and args.driver:
        print_driver_info(driver_info(build_report(args.file), args.driver))

    elif args.file:
        print_report(sort_report(build_report(args.file), args.order))


if __name__ == '__main__':
    print(build_report(r'C:\Users\DELL\Desktop\Foxminded_course\task-7-web-report-of-monaco-2018-racing\data'))
    # main(['--file', r'C:\Users\DELL\Desktop\Foxminded_course\task-7-web-report-of-monaco-2018-racing\data', '--asc'])
