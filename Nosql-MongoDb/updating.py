import pymongo 
from bson.objectid import ObjectId #id ye göre sorgulamalar için gerekli 

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ibrahimkus07:OOihwqP4SK9rJe2A@cluster0.i1inm.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# update_one
# update_many
####################################################3
# mycollection.update_one( #Update the first record found
#     {"name": "Samsung A10"},
#     {"$set":{"name":"Samsung A10-UPDATED"
#              }}
#     )

mycollection.update_many( #Update the all record found
    {"name": "Samsung A20"},
    {"$set":{"name":"Samsung A20-UPDATED"
             }}
    )

for i in mycollection.find(): 
    print(i)