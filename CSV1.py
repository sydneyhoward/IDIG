import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix


with open('asdf.csv') as csvfile:
    readCSV= csv.reader(csvfile, delimiter= ',')
    inOutSets= []
    x=[]
    y=[]
    for row in readCSV:
        x.append(row[0:3])
        y.append(row[3])
        
 
x_train, x_test, y_train, y_test= train_test_split(x,y)

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
#precision: number of true positives (correctly labeled as belonging to the pos class)/ total number of elements labeled as belonging to the positive class (sum of true pos and false pos (incorrectly labeled as belonging to the class))
#recall: number of true pos/ total number of elements actually belonging to the pos class (sum of true pos and false neg(not labeled as belonging to pos class but should've been))
#f1-score: the harmonic mean of precision and recall; gives the accuracy of the classifier in classifying the data points in that particular category
#support: the number of samples from the training data that lie in that class

