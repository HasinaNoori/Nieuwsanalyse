import csv
import xml.etree.ElementTree as ET
import collections

with open('../Data/tweets.csv', 'r', newline='') as csv_file:
    # De 'reader' variabele bevat alle rijen uit het csv bestand en filtert alle cellen met NULL waarde eruit.
    reader = csv.DictReader((l.replace('\0', '') for l in csv_file))
    rows = list(reader)
    tree = ET.parse('../Data/nl-sentiment.xml')
    words = tree.findall('.//word')

    found_words = []
    for word in words:
        word = word.get('form').lower()
        for tweet in rows:
            tweet_words = tweet['Content'].split(" ")
            for tweet_word in tweet_words:
                if tweet_word.lower() == word:
                    found_words.append(word)


counter = collections.Counter(found_words)
print(counter.most_common())