import pymongo 

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ibrahimkus07:OOihwqP4SK9rJe2A@cluster0.i1inm.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

#result = mycollection.find_one()
for i in mycollection.find({},{"_id":0, "name":1,"price":1}):
    print(i)
