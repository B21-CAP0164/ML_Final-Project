import base64 

PATH = 'test.tmp'

empty_str = b""

with open(PATH, "rb") as text:
  empty_str = text.read()

# print(empty_str)
print("saved to imageToSave.png")

with open("imageToSave.png", "wb") as fh:
  fh.write(base64.decodebytes(empty_str))