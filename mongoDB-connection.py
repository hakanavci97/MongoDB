import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]

#print(myclient.list_database_names())
#print (mydb.list_collection_names())

mycollection = mydb["products"]


# product = {"name":"Samsung S9","price":2000}


# result = mycollection.insert_one(product)

# print(result.inserted_id)

# productList = [
# {"name":"Samsung S9","price":2000},
# {"name":"Samsung S10","price":3000},
# {"name":"Samsung S6","price":4000},
# {"name":"Iphone 8","price":5000},
# {"name":"Iphone X","price":6000},
# {"name":"Iphone 12","price":8000},
# {"name":"Iphone 11","price":7000}

# ]

# productList = [
# {"name":"Samsung S9","price":2000, "description":"iyi telefon"},
# {"name":"Iphone 12","price":8000,"categories":["telefon","elektronik"]}

# ]


# result = mycollection.insert_many(productList)

# print(result.inserted_ids)

# result = mycollection.find_one()

# for i in mycollection.find({},{"_id":0,"name":1,"price":1}):
#     print(i)

# print(result)

filter = {"name":"Samsung S9"}

# result = mycollection.find(filter)

# for i in result:
#     print(i)

# result = mycollection.find_one({"_id": ObjectId("622c973dfc376c8c44e63b12")})
# print(result)



# result = mycollection.find({
#     "name": {
#         "$in":["Iphone 8","Samsung S9"]
#     }

# }) Products with Iphone 8 and Samsung s9 in the product name





# result = mycollection.find({
#     "price":{
#         "$gte":2000
#     }
# })Products with a price greater than or equal to 2000




# result = mycollection.find({
#     "price":{
#         "$eq":2000
#     }
# }) Products with a price equal to 2000

# result = mycollection.find({
#     "price":{
#         "$lte":2000
#     }
# }) Products with a price equal to or less than 2000


# result = mycollection.find({
#     "name":{"$regex":"^İ"}
# })

# for i in result:
#     print(i)


# result = mycollection.find().sort("name",1)
#sort products by name in ascending order
#result = mycollection.find().sort("name",1)
#sort products by name in descending order 

# result = mycollection.find().sort("price",-1)
# result = mycollection.find().sort([("name",1),("price",-1)])

# for i in result:
#     print(i)

#UPDATE_ONE()
#UPDATE_MANY()
# for i in mycollection.find():
#     print(i)

# mycollection.update_one(
#     {"name":"Samsung S6"},
#     {"$set":{
#         "name":"Iphone 6"

#     }}
# )


# mycollection.update_many(
#     {"name":"Samsung S9"},
#     {"$set":{
#         "name":"Iphone 11",
#         "price":10000

#     }}
# )

# for i in mycollection.find():
#     print(i)

# query =  {"name":"Samsung S10"}
# newValues = {"$set":{
#         "name":"Iphone 11",
#         "price":10000  }}



# result = mycollection.update_many(query,newValues)

# print (f"{result.modified_count} records updated.")

#DELETE_ONE()
#DELETE_MANY()



for i in mycollection.find():
    print(i)
print('*'*50)

mycollection.delete_one({"name":"Iphone 11"})

result = mycollection.delete_many({"name":{"$regex":"^S"}})

print (f"{result.deleted_count} records deleted")

for i in mycollection.find():
    print(i)
print('*'*50)