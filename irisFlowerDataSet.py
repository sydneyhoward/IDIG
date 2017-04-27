from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

dataset=datasets.load_iris()
model= DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(model)

X= dataset['data']
y= dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X,y)

scaler = StandardScaler()
scaler.fit(X_train)

X_train= scaler.transform(X_train)
X_test= scaler.transform(X_test)

mlp= MLPClassifier(hidden_layer_sizes=(30,30,30))
mlp.fit(X_train,y_train)

MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(10), learning_rate='constant',
       learning_rate_init=0.00001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1000,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
       
predictions= mlp.predict(X_test)

expected= dataset.target
predicted= model.predict(dataset.data)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
