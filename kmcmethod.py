# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:42:43 2018

K means clustering
@author: Ömer Seyrekbasan
"""



#bu fonksiyon bir matristeki her bir sütunun ortalamasını hesaplar
def calc_mean(matrix):
    j = 0
    avg = []
    while(j < len(matrix[0]) - 1 ):
        i = 0
        avg.append(0)
        while(i < len(matrix)):
            avg[j] += matrix[i][j]
            i += 1
        avg[j] /= len(matrix)
        j = j+1
    return avg

#bu fonksiyon 4 uzaklık arasındaki minimum uzaklığı bulur
def find_min(val1, val2, val3, val4):
    min_val = val1
    pos = 1
    if (min_val > val2):
        min_val = val2
        pos = 2
    if (min_val > val3):
        min_val = val3
        pos = 3
    if (min_val > val4):
        min_val = val4
        pos = 4
    return pos

#bu fonksiyon iki veri arasındaki uzaklığı hesaplar
def calc_distance(data1, data2):
    total = 0
    i = 0
    while(i < 6):
        total += abs(data1[i] - data2[i])
        i += 1
    distance = total / 6
    return distance

#k means clustering algoritması bu foknsiyonde gerçeklenmiştir
#k vb. sayılar dataset için hardcode lanmıstır
def cluster(dataset):
    num_of_iter = 10000
    cont = True
    i = 0
    cent_1 = dataset[0]
    cent_2 = dataset[600]
    cent_3 = dataset[1200]
    cent_4 = dataset[1600]
    while (i < num_of_iter and cont ):
        j = 0
        cent_1_elements = []
        cent_2_elements = []
        cent_3_elements = []
        cent_4_elements = []
        while(j < len(dataset)):
           dist_1 =  calc_distance(dataset[j], cent_1)
           dist_2 =  calc_distance(dataset[j], cent_2)
           dist_3 =  calc_distance(dataset[j], cent_3)
           dist_4 =  calc_distance(dataset[j], cent_4)
           min_pos = find_min(dist_1, dist_2, dist_3, dist_4)
           if (min_pos == 1):
               cent_1_elements.append(dataset[j])
           elif (min_pos == 2):
               cent_2_elements.append(dataset[j])
           elif (min_pos == 3):
               cent_3_elements.append(dataset[j])
           elif (min_pos == 4):
               cent_4_elements.append(dataset[j])
               
           j += 1
    
        cent_1 = calc_mean(cent_1_elements)
        cent_2 = calc_mean(cent_2_elements)
        cent_3 = calc_mean(cent_3_elements)
        cent_4 = calc_mean(cent_4_elements)
        i += 1
    print(len(cent_1_elements))
    print(len(cent_2_elements))
    print(len(cent_3_elements))
    print(len(cent_4_elements))
    return cent_1_elements, cent_2_elements, cent_3_elements, cent_4_elements

#bu fonksiyon accuracy ölcmek icindir
def acc(cent_1, cent_2, cent_3, cent_4):
    c1 = [0, 0, 0, 0]
    c2 = [0, 0, 0, 0]
    c3 = [0, 0, 0, 0]
    c4 = [0, 0, 0, 0]

    for i in cent_1:
        if (i[6] == "unacc\n"):
            c1[0] += 1 
        elif (i[6] == "acc\n"):
            c1[1] += 1
        elif (i[6] == "good\n"):
            c1[2] += 1
        elif (i[6] == "vgood\n"):
            c1[3] += 1
    for i in cent_2:
        if (i[6] == "unacc\n"):
            c2[0] += 1 
        elif (i[6] == "acc\n"):
            c2[1] += 1
        elif (i[6] == "good\n"):
            c2[2] += 1
        elif (i[6] == "vgood\n"):
            c2[3] += 1
    for i in cent_3:
        if (i[6] == "unacc\n"):
            c3[0] += 1 
        elif (i[6] == "acc\n"):
            c3[1] += 1
        elif (i[6] == "good\n"):
            c3[2] += 1
        elif (i[6] == "vgood\n"):
            c3[3] += 1
    for i in cent_4:
        if (i[6] == "unacc\n"):
            c4[0] += 1 
        elif (i[6] == "acc\n"):
            c4[1] += 1
        elif (i[6] == "good\n"):
            c4[2] += 1
        elif (i[6] == "vgood\n"):
            c4[3] += 1
    return c1, c2, c3, c4

train_file_1 = open('datasetpath','r')
train_file_2 = open('datasetpath','r')

train1 = train_file_1.readlines()
train2 = train_file_2.readlines()

train_file_1.close()
train_file_2.close()

train1 = train1[11:]
train2 = train2[11:]

train = train1 + train2




i = 0
while (i < len(train)):
    train[i] = train[i].split(",")
    i = i+1

#Birinci sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][0] == "vhigh"):
        train[i][0] = 1
    elif (train[i][0] == "high"):
        train[i][0] = 0.66
    elif (train[i][0] == "med"):
        train[i][0] = 0.33
    elif (train[i][0] == "low"):
        train[i][0] = 0.0
    i = i+1
    

#ikinci sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][1] == "vhigh"):
        train[i][1] = 1
    elif (train[i][1] == "high"):
        train[i][1] = 0.66
    elif (train[i][1] == "med"):
        train[i][1] = 0.33
    elif (train[i][1] == "low"):
        train[i][1] = 0.0
    i = i+1
    
#üçüncü sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][2] == "2"):
        train[i][2] = 1
    elif (train[i][2] == "3"):
        train[i][2] = 0.66
    elif (train[i][2] == "4"):
        train[i][2] = 0.33
    elif (train[i][2] == "5more"):
        train[i][2] = 0.0
    i = i+1

#dördüncü sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][3] == "more"):
        train[i][3] = 1
    elif (train[i][3] == "4"):
        train[i][3] = 0.50
    elif (train[i][3] == "2"):
        train[i][3] = 0
    i = i+1
    
#beşinci sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][4] == "big"):
        train[i][4] = 1
    elif (train[i][4] == "med"):
        train[i][4] = 0.50
    elif (train[i][4] == "small"):
        train[i][4] = 0
    i = i+1
    
#altıncı sütunu normalize et
i = 0
while (i < len(train)):
    if (train[i][5] == "high"):
        train[i][5] = 1
    elif (train[i][5] == "med"):
        train[i][5] = 0.50
    elif (train[i][5] == "low"):
        train[i][5] = 0
    i = i+1
    
    
c1, c2, c3, c4 = cluster(train)

ac1,ac2,ac3,ac4 = acc(c1, c2, c3, c4)


