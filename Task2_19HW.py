import argparse
import json
import xmltodict
from human import Human

human = Human("John", 30, "male", 1993)

if args.format == "json":
    json_data = human.convert_to_json()
    print(json_data)
   
elif args.format == "xml":
    xml_data = human.convert_to_xml()
    print(xml_data)
  
