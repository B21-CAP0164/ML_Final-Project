import json

PATH = 'test.tmp'
empty_str = ""

with open(PATH, "r") as text:
  empty_str = text.read()

response_json = {"data" : str(empty_str)}

with open("data.json", "w") as fh:
  fh.write(json.dumps(response_json))

print("saved to data.json")