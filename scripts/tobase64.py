import base64 

PATH = 'D:\ML_Final-Project\img\dariCloud.jpg'

with open(PATH, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    
    # print(encoded_string)
    with open("../test.tmp", "wb") as text:
      text.write(encoded_string)