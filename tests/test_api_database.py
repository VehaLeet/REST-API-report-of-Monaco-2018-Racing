import pytest
import converter
from racing_report import racing_report


@pytest.mark.parametrize('test_input, expected',
                         [('/api/v1/report/', racing_report.build_report('data')['SVF'])])
def test_database(test_input, expected, client, app):
    converter.convert_from_files_to_db('data', app.config['DATABASE'])
    assert client.get(test_input).json['SVF'] == expected
