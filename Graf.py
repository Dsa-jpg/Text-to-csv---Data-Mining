import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Načtení dat z CSV souboru
data = pd.read_csv('word_counts.csv')

# Vytvoření sloupcového grafu s mezerou mezi sloupci
plt.bar(data['word'], data['count'], width=0.6)

# Nastavení popisků os
plt.xlabel('Slova')
plt.ylabel('Počet')

# Zvýraznění každého 2. popisku osy X pro lepší čitelnost
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(2))

# Otočení popisků os pro lepší čitelnost
plt.xticks(rotation=90)

# Zobrazení a uložení grafu
plt.tight_layout()
plt.savefig('word_counts_graph.png')
plt.show()
