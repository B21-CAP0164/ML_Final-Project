import base64 

PATH = 'test.txt'

empty_str = b""

with open(PATH, "rb") as text:
  empty_str = text.read()

print(empty_str)

with open("imageToSave.png", "wb") as fh:
  fh.write(base64.decodebytes(empty_str))