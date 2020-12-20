#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
import os

from yolo import YOLO
from PIL import Image

yolo = YOLO()
a=0
for root,dirs,files in os.walk("./test/gt"):

         for filename in files:
            a=a+1
            os.mkdir("./test/pred/"+str(a))
            fullname = "./test/gt/"+filename
            with open(fullname) as f:
                while 1:
                    line = f.readline().rstrip('\n')
                    if not line:
                        break

                    file = "./test/pred/"+str(a)+"/"+line+".txt"
                    with open(file, 'a+') as p:
                         p.write(line+'\n')
                         try:
                             image = Image.open('./test/images/'+line+'.jpg')
                         except:
                             str = './test/images/'+line+'.jpg' + ' can not open! Error!'
                             print(str)
                             continue
                         else:
                             boxlist = yolo.generate_box(image)
                             p.write(len(boxlist)+'\n')
                             for box in boxlist:
                                 p.write(box+'\n')
                    p.close()



# testfile = open('%s.txt' % ('test'), 'w')
# imgfile = 'test/images'
# imglist = os.listdir(imgfile)
# for img in imglist:
#     try:
#         image = Image.open(imgfile+'/'+img)
#     except:
#         str = img + ' can not open! Error!'
#         print(str)
#         continue
#     else:
#         # r_image = yolo.detect_image(image)
#         # r_image.show()
#         boxlist = yolo.generate_box(image)
#         for box in boxlist:
#             line = img + ',' + box + '\n'
#             print(line)
#             testfile.write(line)
#
# testfile.close()
