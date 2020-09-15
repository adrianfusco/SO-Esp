# S.O Question: https://es.stackoverflow.com/questions/389238/python-xml-iterar-para-obtener-todos-los-hijos-de-un-elemento/389241

# Import module:
import xml.etree.ElementTree as ET

# Get root:
root = ET.parse('xml_example.xml').getroot()

# Define namespace (see the xml example)
ns = "{https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.3/facturaElectronica}"

# For every node in the root -> child -> {namespace}OtroTexto
for nodo in root.findall(".//"+ns+"OtroTexto"):
    # For every element in the node iteration:
    for elemento in nodo.iter():
        # Get key in every element attribute
        for key in elemento.attrib:
            # Print the attribute and the content of the xml tag
            print(elemento.attrib[key], ":", elemento.text)
