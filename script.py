import csv
from collections import Counter
import string

# Nastavení vstupního textu
text = "Lyžování je sport, který v posledních desetiletích nabyl obrovské popularity. Tento zimní sport nabízí nejen zábavu a adrenalin, ale také je vynikající formou pohybu pro celé tělo. Lyžovat můžete jak v závodním tempu na sjezdovkách, tak i v klidnějším tempu v přírodě, daleko od civilizace. Kromě fyzických přínosů, jako je posilování svalů a kardiovaskulární trénink, lyžování také nabízí příležitost užít si krásné přírody a příjemně si odpočinout od každodenního shonu. Proto je lyžování oblíbeným sportem mnoha lidí všech věkových kategorií a úrovní fyzické kondice."

# Odstranění interpunkce z textu
text = text.translate(str.maketrans('', '', string.punctuation))

# Rozdělení textu na slova a převedení na malá písmena
words = text.lower().split()

# Spočítání počtu výskytů každého slova
word_counts = Counter(words)

# Zápis výsledků do CSV souboru
with open('filename.txt', 'w', encoding='utf-8') as csv_file:
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in word_counts.items():
        writer.writerow({'word': word, 'count': count})
        
