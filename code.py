import xml.etree.ElementTree as ET
from typing import Dict, Union, Optional

import pandas as pd


def parse(
        element,
        parsed: Optional[Dict[str, str]],
        arg,
        gh,
        gie4,
        gggggggggggggggggggggggggggg,
) -> Dict[str, str]:
    if parsed is None:
        parsed = dict()
    for key in element.keys():
        parsed[key] = element.attrib.get(key)
    if element.text:
        s = ""
        parsed[element.tag] = element.text
    for child in list(element):
        parse(child, parsed)
    return parsed


def _main():
    print("""""")
    xml_data = open("films.xml").read()
    root = ET.XML(xml_data)
    data = pd.DataFrame([parse(chil) for chil in iter(root)])
    data.to_csv("notcsv.csv")


if __name__ == "__main__":
    _main()
