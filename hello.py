

#takes a sequence and row length of x (n)
#returns a 2d list (x) of n amount of x values- each list removes the first element of that list
#returns a list (y) of the y values- the (n+1)th value that corresponds to the lists in the 2d x list

import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

with open('design_data_01.csv') as csvfile:
    object_sequence= csv.reader(csvfile, delimiter= ',')
    for sequence in object_sequence:
        copy=sequence
        n=3
        xResult=[]
        yResult=[]
        currList=[]
        for i in sequence:      #getXlist
            for j in range(n):
                currList.append(copy[j])
                if len(copy) < n: break
            if len(currList)==n:
                xResult.append(currList)
            currList=[]
            copy.pop(0)

        for k in range(n,len(list(sequence))):      #get yList
            yResult.append(sequence[k])
        
x_train, x_test, y_train, y_test= train_test_split(xResult,yResult)

scaler= StandardScaler()
scaler.fit(x_train)
x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)
    
mlp= MLPClassifier(hidden_layer_sizes=(30))
mlp.fit(x_train,y_train)

MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
    beta_2=0.999, early_stopping=False, epsilon=1e-08,
    hidden_layer_sizes=(40), learning_rate='invscaling',
    learning_rate_init=0.00001, max_iter=1000, momentum=0.9,
    nesterovs_momentum=True, power_t=0.5, random_state=1000,
    shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
    verbose=False, warm_start=False)

predictions= mlp.predict(x_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
    


###### TEST FCNS

def testGetXList():
    print("testing getxList")
    assert(getXList("1234567",3) == [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]])
    print("passed")
    
def testGetYList():
    print("testing getYList")
    assert(getYList("1234567",3) == [4,5,6,7])
    print("passed")

def testDataSort():
    print("testing dataSort...", end="")
    assert(dataSort("1234567",3) == [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]], [4,5,6,7])
    print("passed!")


#testDataSort()
    