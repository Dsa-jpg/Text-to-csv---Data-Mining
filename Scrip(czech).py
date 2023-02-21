import csv
from collections import Counter
import string
from nltk.stem.snowball import SnowballStemmer

# Nastavení vstupního textu
text = "Tohle je ukázkový text. Tento text bude použit pro demonstraci výstupu."

# Odstranění interpunkce z textu
text = text.translate(str.maketrans('', '', string.punctuation))

# Rozdělení textu na slova a převedení na malá písmena
words = text.lower().split()

# Vytvoření stemmeru pro český jazyk
stemmer = SnowballStemmer("czech")

# Spočítání počtu výskytů každého stemu
stem_counts = Counter(stemmer.stem(word) for word in words)

# Zápis výsledků do CSV souboru
with open('word_counts.csv', mode='w', newline='') as csv_file:
    fieldnames = ['stem', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for stem, count in stem_counts.items():
        writer.writerow({'stem': stem, 'count': count})
