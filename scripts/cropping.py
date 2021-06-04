import cv2
import os

path = 'D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset'
os.chdir(path)

data_dir_list = ['poor', 'good', 'very_poor']

try:
  os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\\new_poor")
  os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\\new_very_poor")
  os.mkdir("D:\ML_Final-Project\Dataset\Dataset\RoadDamageDataset\\new_good")
except FileExistsError:
  print("dah ada")

for dataset in data_dir_list:
    img_list=os.listdir(dataset)
    for img_name in img_list:
        if 'hand' in img_name:
            print('file hand')
            img = cv2.imread(dataset+'/'+img_name)
            dim = (100, 100)
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite('new_'+dataset+'/'+img_name,img)
        else:
            print(img_name)
            #read image
            img = cv2.imread(dataset+'/'+img_name)
            h,w = img.shape[:2]

            #cropping
            # x = 100
            # width = w - 700
            # y = 1000
            # height = h -20
            x=0
            y=int((50/100)*h)
            img = img[y:int((95/100)*h), x:w]

            #resize
            dim = (100, 100)
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            #imwrite
            cv2.imwrite('new_'+dataset+'/'+img_name,img)
        # except:
        #     print('skip')