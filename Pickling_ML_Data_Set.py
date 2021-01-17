import pickle
import requests
data_set=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
data_set=data_set.text
data_set=data_set.split("\n")
file="uciml_data_set.pkl"
fileobject=open(file,"wb")
pickle.dump(data_set,fileobject)
fileobject.close()
fileobject=open("uciml_data_set.pkl","rb")
data_set=pickle.load(fileobject)
print(data_set)
print(type(data_set))
fileobject.close()
