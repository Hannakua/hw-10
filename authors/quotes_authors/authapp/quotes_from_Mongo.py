# from mongoengine import connect

# try:
#     connect(
#         host="mongodb+srv://annka:PPBVqTIHCRrtHgMy@cluster0.7dlllzi.mongodb.net/?retryWrites=true&w=majority"
#     )
#     print("ok connection")
# except:
#     print("no connection")


from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://annka:PPBVqTIHCRrtHgMy@cluster0.7dlllzi.mongodb.net/?retryWrites=true&w=majority"
)

db=client.database_name
c=db.collection_name // This is used to check whether the collection is there or not.


mongoexport --uri="mongodb+srv://annka:PPBVqTIHCRrtHgMy@cluster0.7dlllzi.mongodb.net/?retryWrites=true&w=majority"  --collection=authors  --out=authors.json 
