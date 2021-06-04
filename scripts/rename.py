import os

path = 'D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset'

os.chdir(path)
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      # print(name)
      old_name = os.path.join(root, name)
      try:
        if name.startswith("._"):
          name = name[2:]
          new_name = os.path.join(root, name)
          os.rename(old_name, new_name)
          print("kepindah")
          # os.remove(old_name)
      except FileExistsError:
        print("file exists")
      except:
        print("gagal")
  #  for name in dirs:
  #     print(os.path.join(root, name))