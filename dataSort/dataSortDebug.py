
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

with open('ddtesting.csv') as csvfile:
    sequence1= csv.reader(csvfile, delimiter= ',')
    n=8
    xResult=[]
    currList=[]
    for sequence in sequence1:
        copy=sequence
        indicator= False
        if len(sequence)%2==1:
            yResult= sequence[n:]
        else:
            yResult=sequence[n:]
        while len(sequence)>=n:
            for j in range(n):
                for k in range(len(sequence)):    
                    currList.append(sequence[k])
                    if len(currList)==n:
                        xResult.append(currList)
                        currList=[]
                        sequence=sequence[1:]
                        break
                    if k+1 == len(sequence):
                        indicator=True 
                if indicator==True:
                    break
            if indicator == True:
                break
        xResult.pop()
        print(xResult,yResult)
        
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