from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import pandas as pd
import os
class pre:
    
    def __init__(self):
        #初始化读取操作
        self.PATH = os.path.dirname(__file__) +"\\"
        self.df = pd.read_csv(self.PATH + 'iris data', names=["sepal length", "sepal width", "petal length", "petal width", "class"])
        self.clf = RandomForestClassifier(max_depth=5, n_estimators=10)

    def pred(self,sl,sw,pl,pw):  #获得预测数据的方法
        
        X = self.df.ix[:,:4]  
        y = self.df.ix[:,4]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)  #分割训练数据
        self.clf.fit(X_train,y_train) #训练
        y_pred = self.clf.predict([sl,sw,pl,pw])  #预测

        return y_pred

p=pre()