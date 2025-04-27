import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "name": "John" }
newvalues = { "$set": { "name": "Aman" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find({"name":"Aman"}):
  print(x)