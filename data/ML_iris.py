import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

df = pd.read_csv('iris.csv')
array = df.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(
    X, Y, test_size=validation_size, random_state=seed
)

lgr = LogisticRegression(max_iter=10000)
lgr.fit(X_train, Y_train)
# print(lgr.predict(X_validation))
joblib.dump(lgr, 'logit_iris.pkl')

knn = KNeighborsClassifier()
knn.fit(X_train,Y_train)
joblib.dump(knn, 'knn_iris.pkl')

svm = SVC()
svm.fit(X_train,Y_train)
joblib.dump(svm, 'svm_iris.pkl')
