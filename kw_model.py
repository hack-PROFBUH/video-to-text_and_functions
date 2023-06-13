
import yake
text = "Лондон - столица великобритании, там есть река, река длинная и широкая"
kw_extractor = yake.KeywordExtractor(lan="ru", n=1, top=5)
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)

#############################################################################################################
'''
from rake_nltk import Rake

text = "Лондон - столица великобритании, там есть река, река длинная и широкая"

# Извлечение ключевых слов с помощью RAKE
r = Rake()
r.extract_keywords_from_text(text)
keywords = r.get_ranked_phrases()

print("  ")
for word in text.split():
    if word in keywords:
        print("- " + word)


text = text.lower()

for word in keywords:
    if word in text:
        print(word)
'''
##################################################################################################################
'''
import spacy


nlp = spacy.load('ru_core_news_lg')     #эта модель названия определяет

text = """Лондон - столица и самый густонаселенный город Англии и
Соединенного Королевства. Расположенный на реке Темзе на юго-востоке
острова Великобритания, Лондон был крупным поселением
на протяжении двух тысячелетий. Он был основан римлянами, которые назвали его Лондиниум.
"""

doc = nlp(text)

for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")

'''
