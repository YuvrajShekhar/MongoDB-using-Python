import pymongo 

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employees']

information = mydb.employeeinformation

record = [{
    "First_Name":"Yuvraj", 
    "Last_Name":"S",
    "Company" : "Subex"
},
{
    "First_Name":"xyz", 
    "Last_Name":"c",
    "Company" : "Subex"
},
{
    "First_Name":"abc", 
    "Last_Name":"p",
    "Company" : "FlyCamp"
}]

information.insert_many(record)
for record in information.find({'Company':{'$in':['Subex']}}):
   print(record)
 

