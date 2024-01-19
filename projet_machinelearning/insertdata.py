import pandas as pd
import pymongo

myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
mydatabase = myclient["projectDatabase"]
first_collection = mydatabase["collectionPoem"]
second_collection = mydatabase["collectionhaiku"]

#creation Index
first_collection.create_index([("french_poem",1)],name="indexpoem")
second_collection.create_index([("haiku",1)],name="indexhaiku")

#prendre les données
resultat_poem = first_collection.find({},{"_id":0,"french_poem":1})
resultalt_haiku = second_collection.find({},{"_id":0,"haiku":1})

#tout mettre dans une liste
liste_poem=[]
for i in resultat_poem:
    liste_poem.append(i)
liste_haiku = []
for i in resultalt_haiku:
    liste_haiku.append(i)
def transforme_liste_en_df(liste,clé):
    liste_des_valeurs = []
    for i in liste:
        valeur = i[clé]
        liste_des_valeurs.append(valeur)
    df = pd.DataFrame(liste_des_valeurs,columns=[clé])
    return df


#recuperation de données
df_haiku = transforme_liste_en_df(liste_haiku,"haiku")
df_poem = transforme_liste_en_df(liste_poem,"french_poem")

exsistingcsv_of_haiku = pd.read_csv("dfhaiku.csv")
exsistingcsv_of_poem = pd.read_csv("dfpoem.csv")

final_df_haiku = pd.concat([df_haiku,exsistingcsv_of_haiku])
final_df_poem = pd.concat([df_poem,exsistingcsv_of_poem])

def detecter_theme_mots_cles(poem):
    themes = {
            "nature" : ["ciel bleu", "ondulations douces", "grenouilles croassent", "chant paisible", "brume matinale", "oiseaux chantonnent", "rosée", "herbe"],
            "amour" : ["chant de l'amour", "cœur vibrant", "bonheur", "vive lueur", "écoute battre", "embrasse", "fleur", "s'épanouit"],
            "temps" :["temps", "suspendre", "heures propices", "rapides délices", "ô temps", "vol", "cours"],
            "vanité" : ["vanité", "vains plaisirs", "vains efforts", "triste", "âme de l'homme"],
            "saisons" :["printemps", "été", "automne", "hiver"]
    }

    poem = poem.lower()

    for theme, mots_cles in themes.items():
        for mot_cle in mots_cles:
            if mot_cle in poem:
                return theme

    return "Indéterminé"

# Appliquer la détection de thème sur la colonne prétraitée
final_df_poem["theme"] = final_df_poem["french_poem"].apply(detecter_theme_mots_cles)

# Afficher le DataFrame résultant avec les thèmes détectés
print(final_df_poem[["french_poem", "theme"]])

