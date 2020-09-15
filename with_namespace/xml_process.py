import xml.etree.ElementTree as ET

root = ET.parse('xml_example.xml').getroot()

ns = "{https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.3/facturaElectronica}"


for nodo in root.findall(".//"+ns+"OtroTexto"):
    for elemento in nodo.iter():
        for key in elemento.attrib:
            print(elemento.attrib[key], ":", elemento.text)
