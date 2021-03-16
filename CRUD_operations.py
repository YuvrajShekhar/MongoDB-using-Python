import pymongo 

client = pymongo.MongoClient('mongodb://abc:123@127.0.0.1:27017/')

mydb = client.test

col = mydb.person

#CREATE operation - insert
col.insert_one(
   {
      "name": "John",
      "salary": 100 ,
   }
)
##insert many
col.insert_many(
   [
     { "name": "Jeorge", "salary": 100},
     { "name": "Steve", "salary": 100},
     { "name": "David","salary": 100}
   ]
)

#READ operation - find
#returns cursor position
print(col.find())


#finds the resepective object
print(col.find_one({"name": "John"}))

#UPDATE operation - update
col.update_one({"name":"John"}, {"$set":{"name":"Joseph"}})

# update_many
col.update_many({"name":"John"}, {"$set":{"name":"Joseph"}})

#DELETE operation - delete
col.delete_one({"name":"Joseph"})
col.delete_one({"name":"Steve"})
col.delete_one({"name":"David"})

col.delete_many({"name":"Jeorge"})

col.delete_one({"name":"John"})


