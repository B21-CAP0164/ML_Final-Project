import base64 

PATH = 'D:\ML_Final-Project\dariCloud.jpg'

with open(PATH, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    
    # print(encoded_string)
    with open("testCloud.txt", "wb") as text:
      text.write(encoded_string)