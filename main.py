import sklearn
import csv
import pandas as pd

file = open("e:/taha/code/HW2/src/train.csv", "r")
csv_reader = csv.reader(file)
train = []
label = []
lists_from_csv = []

for row in csv_reader:
    lists_from_csv.append(row)
    label.append(row[24])
    train.append([x for x in row[1:24]])

train.pop(0)
print(len(train))
for i in range(len(train)):
    #male or female
    if train[i][1] == 'Male':
        train[i][1] = 1
    else:
        train[i][1] = 0
    #loyal customer or dis
    if train[i][2] == 'Loyal Customer':
        train[i][2] = 1
    else:
        train[i][2] = 0
    #business or personal travel
    if train[i][4] == 'Personal Travel':
        train[i][4] = 1
    else:
        train[i][4] = 0
    #business or eco plus
    if train[i][5] == 'Eco Plus':
        train[i][5] = 1
    else:
        train[i][5] = 0

    if label[i] == 'satisfied':
        label[i] = 1
    else:
        label[i] = 0

    for j in range(len(train[i])):
        # print()
        if (j == 22):
            train[i][j] = float(train[i][j])
        train[i][j] = int(train[i][j])


# print(train)



from sklearn.linear_model import Perceptron

clf = Perceptron(random_state=0).fit(train, label)
