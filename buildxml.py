import encodings
import xml.etree.ElementTree as ET
import re
import fileinput
import os


inputFile = 'files/manfred_extracted.txt'
xmlFile = 'files/output.xml'

tree = ET.ElementTree(element= ET.Element('document'))
root=tree.getroot()

# Add header
header = ET.Element('header')
root.append(header)

title = ET.Element('title')
title.text = 'Manfred - Ingénierie Documentaire (2021)'
header.append(title)

authors = ET.Element('authors')
authors.text = "compiled by Philipa Payne et Fábio Cabral"
header.append(authors)

drama = ET.Element('drama')
root.append(drama)

countActs = 0

with open (inputFile, 'r', encoding="utf-8") as txt_file:
    for line in txt_file:
        #act match
        a = re.match(r'\s*(ACT\s([I]{1,3})\.)', line)
        if a:
            countActs += 1
            print("Act caught")
#            act = ET.SubElement(drama, 'act', attrib = {'n': a.group(2)})
            act = ET.SubElement(drama, 'act', attrib = {'n': str(countActs)})
            act.text = a.group()

        b = re.match(r'\s*(SCENE\s([I]{1,3})\.)', line)
        if b:
            print("Scene caught")
            scene = ET.SubElement(drama, 'scene', attrib = {'n': b.group(2)})
#            act = ET.SubElement(drama, 'act', attrib = {'n': str(countActs)})
            scene.text = b.group()

        c = re.match(r'\s*(SCENE\s(IV)\.)', line)
        if c:
            print("Scene caught")
            scene = ET.SubElement(drama, 'scene', attrib = {'n': c.group(2)})
#            act = ET.SubElement(drama, 'act', attrib = {'n': str(countActs)})
            scene.text = c.group()

        else:
            pass


ET.indent(tree)
tree.write(xmlFile, encoding="utf-8", xml_declaration=True)