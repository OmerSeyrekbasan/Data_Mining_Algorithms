# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:00:30 2018
K nearest neighbour
@author: Ömer Seyrekbasan
"""


#bu fonksiyon iki veri arasındaki uzaklığı hesaplar
def calc_distance(data1, data2):
    total = 0
    i = 0
    while(i < 6):
        total += abs(data1[i] - data2[i])
        i += 1
    distance = total / 6
    return distance
#bu fonksiyon verilen bir test verisi için knn hesaplar
def find_class(train_set, test_data):
    w, h = 2, len(train_set);
    distance_matrix = [[0 for x in range(w)] for y in range(h)] 
    i = 0
    while(i < len(train_set)):
        val = calc_distance(train_set[i], test_data)
        #değerin classı
        distance_matrix[i][0] = train_set[i][6]
        #değer
        distance_matrix[i][1] = val
        
        i += 1
    distance_matrix.sort(key=lambda x : x[1])
    
    i = 0
    a = [0, 0, 0, 0]
    
    while (i < 9):
        if (distance_matrix[i][0] == "unacc\n"):
            a[0] += 1
        elif (distance_matrix[i][0] == "acc\n"):
            a[1] += 1
        elif (distance_matrix[i][0] == "good\n"):
            a[2] += 1
        elif (distance_matrix[i][0] == "vgood\n"):
            a[3] += 1
        i += 1
    return a

#bu fonksiyon test seti üzerinden confusion matrix oluşturur
def acc(train, test):
    w, h = 5, 5;
    confusion_matrix = [[0 for x in range(w)] for y in range(h)] 
    
    confusion_matrix[0][1] = confusion_matrix[1][0] = "unacc"
    confusion_matrix[0][2] = confusion_matrix[2][0] = "acc"
    confusion_matrix[0][3] = confusion_matrix[3][0] = "good"
    confusion_matrix[0][4] = confusion_matrix[4][0] = "vgood"
    
    for i in test:
        res = find_class(train, i)
        pos = res.index(max(res))
        if (pos == 0):
            pos_class = "unacc\n"
        elif (pos == 1):
            pos_class = "acc\n"
        elif (pos == 2):
            pos_class = "good\n"
        elif (pos == 3):
            pos_class = "vgood\n"
            
        #Burada matrisin ilk satırı sınıflar olduğu için pozisyonun 1 arttırılması gerekiyor    
        if (pos_class == i[6]):
            confusion_matrix[pos+1][pos+1] += 1
        elif (i[6] == "unacc\n" ):
            confusion_matrix[pos+1][1] +=1
        elif (i[6] == "acc\n" ):
            confusion_matrix[pos+1][2] +=1
        elif (i[6] == "good\n" ): 
            confusion_matrix[pos+1][3] +=1
        elif (i[6] == "vgood\n" ):
            confusion_matrix[pos+1][4] +=1
             
    
    return confusion_matrix
#test edilmek istenen dosya yüklenmelidir
train_file = open('datasetpath','r')
test_file =  open('datasetpath','r')

train =train_file.readlines()
test = test_file.readlines()

train = train[11:]
test = test[11:]

i = 0
while (i < len(train)):
    train[i] = train[i].split(",")
    i = i+1

i = 0
while (i < len(test)):
    test[i] = test[i].split(",")
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
    
i = 0
while (i < len(test)):
    if (test[i][0] == "vhigh"):
        test[i][0] = 1
    elif (test[i][0] == "high"):
        test[i][0] = 0.66
    elif (test[i][0] == "med"):
        test[i][0] = 0.33
    elif (test[i][0] == "low"):
        test[i][0] = 0.0
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
    
i = 0
while (i < len(test)):
    if (test[i][1] == "vhigh"):
        test[i][1] = 1
    elif (test[i][1] == "high"):
        test[i][1] = 0.66
    elif (test[i][1] == "med"):
        test[i][1] = 0.33
    elif (test[i][1] == "low"):
        test[i][1] = 0.0
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

i = 0
while (i < len(test)):
    if (test[i][2] == "5more"):
        test[i][2] = 1
    elif (test[i][2] == "4"):
        test[i][2] = 0.66
    elif (test[i][2] == "3"):
        test[i][2] = 0.33
    elif (test[i][2] == "2"):
        test[i][2] = 0.0
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
    
i = 0
while (i < len(test)):
    if (test[i][3] == "more"):
        test[i][3] = 1
    elif (test[i][3] == "4"):
        test[i][3] = 0.50
    elif (test[i][3] == "2"):
        test[i][3] = 0
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
    
i = 0
while (i < len(test)):
    if (test[i][4] == "big"):
        test[i][4] = 1
    elif (test[i][4] == "med"):
        test[i][4] = 0.50
    elif (test[i][4] == "small"):
        test[i][4] = 0
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
    
i = 0
while (i < len(test)):
    if (test[i][5] == "high"):
        test[i][5] = 1
    elif (test[i][5] == "med"):
        test[i][5] = 0.50
    elif (test[i][5] == "low"):
        test[i][5] = 0
    i = i+1
    
    

mtx = acc(train, test)

i = 1
total = 0
while(i < 5):
    j = 1
    while (j < 5):
        total += mtx[i][j]
        j += 1
    i += 1
    
    
i = 0
while(i < 5):
    j = 0
    while (j < 5):
        print ( "%5s" % (str(mtx[i][j])), end=" ", flush=True)
        j += 1
    print()
    i += 1
    


i = 1
correct = 0
while(i<5):
    correct += mtx[i][i]
    i = i+1


print()

print()

print()

print(correct/ total)

train_file.close()
test_file.close()



















