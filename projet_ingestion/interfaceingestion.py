import json
import random
import pymongo

# Load haikus data from the json file
with open('db.json', 'r', encoding='utf-8') as file:
    poems_data = json.load(file)

# Load French poems from the json file
with open("Frenchpoems3.json", "r", encoding="utf-8") as file:
    french_poems = json.load(file)


#Mongoclient pour me servir a créer une base de donnée sur un lien ou elle sera hebergé
myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
#creer une base de données et une collection
mydb =  myclient["projectDatabase"]
first_collection = mydb["collectionPoem"]
second_collection = mydb["collectionhaiku"]

# Function to count syllables in a word
def count_syllables(word):
    d = cmudict.dict()
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

# Function to generate a random French poem
def generate_random_french_poem():
    random_poem = random.choice(french_poems)
    lines = random_poem["Content"].split("\n")
    random.shuffle(lines)
    a = " ".join(lines)
    lista = list(a)
    derniere_occ = len(lista)
    if (lista[derniere_occ-1] == ".") or (lista[derniere_occ-1] ==","):
        lista[derniere_occ-1]=""
    a_transformé = "".join(lista)
    dict = {"french_poem":a_transformé}
    first_collection.insert_one(dict)
    return "\n".join(lines)

"""# Function to translate a poem to English
def translate_to_english(poem):
    print(poem)
    translator = Translator()
    translated_lines = [translator.translate(line, dest='en').text for line in poem.split("\n")]
    return "\n".join(translated_lines)"""

# Function to generate a random haiku
def generate_random_haiku(data):
    author = random.choice(list(data.keys()))
    haikus = data[author]['haikus']
    poem_lines = random.sample(haikus, 3)
    concat = ''
    for i in poem_lines:
        concat = concat + i.replace("\n"," ") + ' '
    generatedDict = {"haiku":concat}
    second_collection.insert_one(generatedDict)
    return poem_lines

# Function to validate syllables in a haiku
"""def validate_syllables(poem_lines):
    syllables_per_line = [5, 7, 5]
    for i in range(3):
        words = word_tokenize(poem_lines[i])
        syllable_count = sum(count_syllables(word) for word in words)
        if syllable_count != syllables_per_line[i]:
            return False
    return True"""

# Generate a random haiku
random_haiku = generate_random_haiku(poems_data)
french_poem = generate_random_french_poem()
#print(random_haiku)

# Display the original haiku
print("Original Haiku:")
"""for line in random_haiku:
    print(line)"""

# Translate the haiku to English
#translated_haiku = translate_to_english("\n".join(random_haiku))

# Display the translated haiku
"""print("\nTranslated Haiku:")
print(translated_haiku)"""
