import pymongo


#Mongoclient pour me servir a créer une base de donnée sur un lien ou elle sera hebergé
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#creer une base de données et une collection
mydb =  myclient["databaseprojet"]
first_collection = mydb["collection_one"]

#inserer un document
"""liste_des_document = [{"Nom":"Idir","Chanson":"Mliyi"},
                      {"Nom":"Slimane Azem","Chanson":"Awin istoufan","Top":"1"},
                      {"Nom":"Rayan and Rima","Chanson":"Dana Dana"}]
a = first_collection.insert_many(liste_des_document)
print(a.inserted_ids)"""



#update un field rapidement
first_collection.update_one(
{"Nom":"Slimane Azem"},
{"$set":{"Top":1}}
)

#trouver des documents grace à find
first_find = first_collection.find({},{"Nom":1,"Chanson":1})
second_find = first_collection.find({"Nom":"Slimane Azem"},{})
third_find = first_collection.find(({"Top":{"$lt":2}}))
"""for x in third_find:
    print(x)"""


#sorting de cette facon
a = first_collection.find().sort("Nom",1)
"""for i in a :
    print(i)"""

#supprimer un element
first_collection.delete_one({"Nom":"Idir"})