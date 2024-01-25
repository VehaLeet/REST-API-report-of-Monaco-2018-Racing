import xml.etree.ElementTree as ET
from flask import current_app, request, jsonify
from flask_restful import Resource
from racing_report import racing_report as rcreport
from converter import convert_from_db


def xml_format_report(data: dict):
    root = ET.Element("drivers")
    for k, v in data.items():
        driver = ET.SubElement(root, 'driver')
        name = ET.SubElement(driver, 'name')
        abbreviation = ET.SubElement(driver, 'abbreviation')
        car = ET.SubElement(driver, 'car')
        lap_time = ET.SubElement(driver, 'lap_time')

        driver.attrib = {'abb': k}
        name.text = v['name']
        abbreviation.text = v['abbreviation']
        car.text = v['car']
        lap_time.text = v['lap_time']

    return current_app.response_class(ET.tostring(root), mimetype='application/xml')


def xml_format_driver(data):
    root = ET.Element("drivers")
    driver = ET.SubElement(root, 'driver')
    name = ET.SubElement(driver, 'name')
    abbreviation = ET.SubElement(driver, 'abbreviation')
    car = ET.SubElement(driver, 'car')
    lap_time = ET.SubElement(driver, 'lap_time')

    name.text = data['name']
    abbreviation.text = data['abbreviation']
    car.text = data['car']
    lap_time.text = data['lap_time']

    return current_app.response_class(ET.tostring(root), mimetype='application/xml')


class ReportPage(Resource):

    def get(self):
        """
        This is an GET method
        ---
        tags:
          - restful
        parameters:
          - in: query
            name: format
            required: false
            description: Different output, try 'xml', or 'json'!
            type: string
          - in: query
            name: order
            required: false
            description: Sort report, try 'desc'!
            type: string
        responses:
          200:
            description: The report data
            schema:
              id: report
              properties:
                report:
                  type: string
                  default: report
        """
        
        report = convert_from_db()

        order_switcher = True
        order_query = request.args.get('order')
        if order_query == 'desc':
            order_switcher = False

        format_query = request.args.get('format')
        if format_query == 'xml':
            return xml_format_report(rcreport.sort_report(report, order_switcher))
        elif format_query == 'json':
            return jsonify(rcreport.sort_report(report, order_switcher))
        else:
            return rcreport.sort_report(report, order_switcher)


class DriverPage(Resource):
    def get(self, driver_id: str):
        """
        This is an GET method
        ---
        tags:
          - restful
        parameters:
          - in: path
            name: driver_id
            required: true
            description: The ID of the driver, try SVF!
            type: string
          - in: query
            name: format
            required: false
            description: Different output, try xml, or json!
            type: string
        responses:
          200:
            description: The drivers data
            schema:
              id: Driver
              properties:
                driver:
                  type: string
                  default: Driver
        """
        try:
            report = convert_from_db()

            format_query = request.args.get('format')
            if format_query == 'xml':
                return xml_format_driver(report[driver_id.upper()])
            elif format_query == 'json':
                return jsonify(report[driver_id.upper()])
            else:
                return report[driver_id.upper()]
        except KeyError as e:
            return {'error': str(f'KeyError: {e}')}



