#生成yolo模型需要的数据映射文件，2007_train.txt
#建立图片存储地址和图片真实框、类别的映射

list_file = open('%s_%s.txt' % (2007, 'train'), 'w')
anno_file = open('VOCdevkit/VOC%s/Annotations/train.txt' % (2007), 'r')

list_anno = anno_file.readlines()
last_image = ''
for i in range(0, len(list_anno)):
    anno = list_anno[i].strip('\n')
    image_id = anno.split(',')[0]

    if image_id != last_image:
        if i != 0:
            list_file.write('\n')
        list_file.write('VOCdevkit/VOC%s/JPEGImages/%s' % (2007, image_id))
        last_image = image_id

    index = anno.split(',')[1:]
    position = ','.join(index)
    position += ',0'  # 397,210,538,417,0 所有的框都是face类别

    str = ' ' + position
    list_file.write(str)

list_file.close()