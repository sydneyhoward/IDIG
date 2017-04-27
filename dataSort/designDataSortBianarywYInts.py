import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

"""
create empty list with 7 0's
loop through each element (n) in sequence
index to n-1 and +1
"""

def getXList(sequence,n,numOfNums):
    currList= [0]*numOfNums
    nList=[]
    finalList=[]
    indicator=False
    for i in sequence:
        copy=i
        while len(i)>n:
            for j in copy:
                currList[int(j)-1]+=1
                for k in currList:
                    nList.append(k)
                currList= [0]*numOfNums
                if len(nList)==n*numOfNums:
                    finalList.append(nList)
                    copy= copy[1:]
                    break
                if len(copy)<=n+1:
                    indicator=True
            if indicator==True:
                break
            nList=[]
    return finalList
    
    
def getYList(sequence,n,numOfNums):
    yResult=[] 
    for i in sequence:
        yResult= i[n:]
    return yResult


def getFinalXList():
    finalXList=[]    
    for i in range(1, 49):
        a=""
        i=str(i)
        if len(i)== 1:
            a+=str(0) 
        a+=i
        with open('design_data_' + a + '.csv') as csvfile:
            objectSequence= csv.reader(csvfile, delimiter= ',')
            n=3
            numOfNums=7
            xList= getXList(objectSequence,n,numOfNums)
        for j in xList:
            finalXList.append(j)
        xList= []
    return finalXList

def getFinalYList():
    finalYList=[]    
    for i in range(1, 49):
        a=""
        i=str(i)
        if len(i)== 1:
            a+=str(0) 
        a+=i
        with open('design_data_' + a + '.csv') as csvfile:
            objectSequence= csv.reader(csvfile, delimiter= ',')
            n=3
            numOfNums=7
            yList= getYList(objectSequence,n,numOfNums)
        for j in yList:
            finalYList.append(j)
        yList= []
    return finalYList

x,y=[],[]            
x= getFinalXList()
y= getFinalYList()
    
x_train, x_test, y_train, y_test= train_test_split(x,y)

scaler= StandardScaler()
scaler.fit(x_train)
x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)


mlp=MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
    beta_2=0.999, early_stopping=False, epsilon=1e-08,
    hidden_layer_sizes=(20), learning_rate='invscaling',
    learning_rate_init=0.01, max_iter=1000, momentum=0.9,
    nesterovs_momentum=True, power_t=0.5, random_state=1000,
    shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
    verbose=False, warm_start=False)
print(x_train,x_test)
    
mlp.fit(x_train,y_train)
predictions= mlp.predict(x_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

    