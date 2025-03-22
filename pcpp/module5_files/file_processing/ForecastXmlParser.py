import xml.etree.ElementTree as ET


class TemperatureConverter:

    @staticmethod
    def convert_celsius_to_fahrenheit(temperature):
        return round((9 / 5) * temperature + 32, 1)


class ForecastXmlParser:

    @staticmethod
    def parse(filename):
        tree = ET.parse(filename).getroot()
        for element in tree:
            print(f'{element[0].text}: {element[1].text} Celsius, {TemperatureConverter.convert_celsius_to_fahrenheit(
                int(element[1].text))} Fahrenheit')


ForecastXmlParser.parse('forecast.xml')
