import pymongo 

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ibrahimkus07:OOihwqP4SK9rJe2A@cluster0.i1inm.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

#print(myclient.list_database_names())
print(mydb.list_collection_names())

# # product = {"name":"Iphone14", "price":3000}
# # result = mycollection.insert_one(product)

# # print(result)
# # print(type(result))
# # print(result.inserted_id)

#Multi insert
productList = [
    #{"_id": 1,"name":"Samsung A10","price":2000}, 
    {"name":"Samsung A20","price":22000, "desc":"Android"}, 
    {"name":"Samsung A35","price":3000},
    {"name":"Samsung A40","price":4000}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)