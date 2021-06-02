import os

path = 'D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset'

listDiGood = []

good = 0
poorBefore = 0
poorAfter = 0

os.chdir(os.path.join(path, "new_good"))
print(os.getcwd())

for root, dirs, files in os.walk(".", topdown = False):
  for name in files:
    if (not name.startswith("._")) and name.endswith(".jpg"):
      listDiGood.append(name)
      # print(name)

good = len(listDiGood)

os.chdir(os.path.join(path, "new_poor"))
print(os.getcwd())
for root, dirs, files in os.walk(".", topdown = False):
  poorBefore = len(files)
  poorAfter = poorBefore
  for name in files:
    if (not name.startswith("._")) and name.endswith(".jpg"):
      if name in listDiGood:
        os.remove(name)
        print(name, "dihapus dari new_poor")
        poorAfter = poorAfter - 1

print("good = ",good)
print("poor before = ",poorBefore)
print("poor after = ",poorAfter)