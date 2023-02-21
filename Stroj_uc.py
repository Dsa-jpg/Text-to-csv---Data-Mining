from textblob import TextBlob

text = "Lyžování je sport, který v posledních desetiletích nabyl obrovské popularity. Tento zimní sport nabízí nejen zábavu a adrenalin, ale také je vynikající formou pohybu pro celé tělo. Lyžovat můžete jak v závodním tempu na sjezdovkách, tak i v klidnějším tempu v přírodě, daleko od civilizace. Kromě fyzických přínosů, jako je posilování svalů a kardiovaskulární trénink, lyžování také nabízí příležitost užít si krásné přírody a příjemně si odpočinout od každodenního shonu. Proto je lyžování oblíbeným sportem mnoha lidí všech věkových kategorií a úrovní fyzické kondice."

blob = TextBlob(text)

sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Text je pozitivní.")
elif sentiment < 0:
    print("Text je negativní.")
else:
    print("Text je neutrální.")
