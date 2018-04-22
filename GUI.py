from tkinter import *
from tkinter import Label

import sklearn.externals
import matplotlib.image as mpimg

clf = sklearn.externals.joblib.load("Hackathon_model.sav")
clf2 = sklearn.externals.joblib.load("Hackathon_model2.sav")
import numpy as np

print(clf)

root = Tk()

from PIL import Image, ImageTk

root.title("ABCD")

root.configure(background="blue")

def returns_entry(en):
    content = en.get()
    print(content)

def readnumbers(numbers, model):
    numbers = [np.array(numbers)]
    pred = model.predict(np.array(numbers))
    return(pred)

def readimage(img, model):
    image2 = mpimg.imread(img)
    image2 = image2.reshape(7500, )
    image2 = [np.array(image2)]
    pred = model.predict(np.array(image2))
    return (pred)

def pic():
    y = str(input('Enter Photo Address: '))

    pred = readimage(y, clf)
    print(pred)


def numbre():
    c=0
    matrix = []
    while c < 29:
        c = c+1
        x = input('Enter Data: ')
        matrix.append(x)
    pred = readnumbers(matrix, clf2)
    print(pred)





class buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(side=BOTTOM, fill=X)

        topFrame = Frame(root)
        topFrame.pack(side=TOP, fill=X)

        self.another = Button(topFrame, text="Pic", command=pic)
        self.another.pack(fill=X)

        self.another2 = Button(topFrame, text="Numbers", command=numbre)
        self.another2.pack(fill=X)

        self.quitButton = Button(frame, text="QUIT", command=frame.quit)
        self.quitButton.pack(fill=X)


b = buttons(root)

image = Image.open("Cells.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()

"""


path = "\\Users\\erichu\\Downloads\\IDC_regular_ps50_idx5" 8863_idx5_x151_y1401_class0.png
picture_names = []
c = 0
for filename in os.listdir(path):
    for file2 in os.listdir(path +"\\"+ filename):
        for file3 in os.listdir(path +"\\"+ filename + "\\" + file2):
            c= c+1
            if c > 53033:
                break
            else:
                print(file3 + " : " + str(c))
                picture_names.append(file3)

picture_names = picture_names[0:10000]
count = 0
for i in picture_names:
    print(i)
    count=count+1
    print(count)

path = "\\Users\\erichu\\Downloads\\IDC_regular_ps50_idx5"
pictures = []
Y_data = []
c = 0
for filename in os.listdir(path):
    for file2 in os.listdir(path +"\\"+ filename):
        for file3 in os.listdir(path +"\\"+ filename + "\\" + file2):
            c= c+1
            if c > 1500:
                break
            else:
                temp_variable = mpimg.imread(path +"\\"+ filename + "\\" + file2 + "\\" + file3)
                if temp_variable.shape == (50,50,3):
                    pictures.append(temp_variable)
                    Y_data.append(int(file2))
print(pictures)

X_data = []      
for i in pictures:
    j = i.reshape(7500,)
    X_data.append(j)

print(X_data)
print(Y_data)

train_x, test_x = X_data[0:1200], X_data[1200:]
train_y, test_y = Y_data[0:1200], Y_data[1200:]

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import ExtraTreesClassifier # to apply the Logistic regression
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn.cross_validation import KFold # use for cross validation
from sklearn.model_selection import GridSearchCV# for tuning parameter
from sklearn.ensemble import RandomForestClassifier # for random forest classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def function(model):
    model.fit(train_x, train_y)
    prediction = model.predict(test_x)
    accuracy = metrics.accuracy_score(prediction, test_y)
    print(accuracy)
function(LogisticRegression())
function(RandomForestClassifier())
function(GaussianNB())
function(ExtraTreesClassifier())
function(GradientBoostingClassifier())

"""

"""""
13.0,21.82,87.5,519.8,0.1273,0.1932,0.1859,0.09353,0.235,0.07389,0.3063,1.002,2.406,24.32,0.005731,0.03502,0.03553,0.01226,0.02143,0.003749,15.49,30.73,106.2,739.3,0.1703,0.5401,0.539,0.206,0.4378,0.1072

\\Users\\erichu\\Downloads\\IDC_regular_ps50_idx5 8863_idx5_x151_y1401_class0.png
"""