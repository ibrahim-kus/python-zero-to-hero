import pymongo 
from bson.objectid import ObjectId #id ye göre sorgulamalar için gerekli 

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ibrahimkus07:OOihwqP4SK9rJe2A@cluster0.i1inm.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name', -1) # 1 increase sort -1 decrease sort
# result = mycollection.find().sort('price', -1)
result = mycollection.find().sort([('name',1), ('price',-1)])

for i in result:
    print(i)