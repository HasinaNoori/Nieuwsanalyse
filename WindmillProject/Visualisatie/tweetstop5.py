import csv
import xml.etree.ElementTree as ET

with open('../Data/tweests.csv', 'r', newline='') as csv_file:
    # De 'reader' variabele bevat alle rijen uit het csv bestand en filtert alle cellen met NULL waarde eruit.
    reader = csv.DictReader((l.replace('\0', '') for l in csv_file))
    next(reader)

    tree = ET.parse('../Data/nl-sentiment.xml')
    words = tree.findall('.//word')

    for word in words:
        word = word.get('form')
        print(word)
        for tweet in reader:
            tweet_words = tweet['Content'].split(" ")
            for tweet_word in tweet_words:
                if tweet_word == word:
                    print(f"Gevonden: {word}")
