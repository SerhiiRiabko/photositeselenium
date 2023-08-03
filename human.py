import json
import xmltodict

class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        data = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "birth_year": self.birth_year
        }
        return json.dumps(data)

    def convert_to_xml(self):
        data = {
            "Human": {
                "name": self.name,
                "age": self.age,
                "gender": self.gender,
                "birth_year": self.birth_year
            }
        }
        return xmltodict.unparse(data)
      
