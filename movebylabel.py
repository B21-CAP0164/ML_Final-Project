import os
import xml.etree.ElementTree as ET
import shutil

path = 'D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset'

label_list_per_image = {}

os.chdir(path)
for root, dirs, files in os.walk(".", topdown = False):
  for name in files:
    try:
      if (not name.startswith("._")) and name.endswith(".xml"):
        # parsing xml disini
        tempList = []
        # if name == "Adachi_20170921160404.xml":
        full_path = os.path.join(root, name)
        # print("root : ", root)
        print(full_path)
        tree = ET.parse(full_path)
        xml_root = tree.getroot()
        
        for child in xml_root:
          if child.tag == "object":
            for objects in child:
              if objects.text.strip() != "" : tempList.append(objects.text.strip())
        
        label_list_per_image[name[:-4]+".jpg"] = tempList
    except:
      print("gagal")

# print(label_list_per_image)
first = True
for root, dirs, files in os.walk(".", topdown = False):
  if first:
    try:
      os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\poor")
      os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\\very_poor")
      os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\good")
      first = False
    except FileExistsError:
      print("DAH ADA BAMBANG")
  for name in files:
    if (not name.startswith("._")) and name.endswith(".jpg"):
      if name in label_list_per_image:
        print(name, "-> ", label_list_per_image[name])
        if "D40" in label_list_per_image[name] :
          print("very poor")
          shutil.copyfile(os.path.join(root, name), os.path.join("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\\very_poor", name))
        
        elif ("D00" in label_list_per_image[name]) or ("D10" in label_list_per_image[name]) or ("D20" in label_list_per_image[name]):
          print("poor")
          shutil.copyfile(os.path.join(root, name), os.path.join("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\poor", name))
        
        else:
          print("good")
          shutil.copyfile(os.path.join(root, name), os.path.join("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\good", name))