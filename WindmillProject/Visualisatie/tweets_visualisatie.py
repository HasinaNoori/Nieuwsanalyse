import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np
import seaborn as sns
sns.set(style="darkgrid")


def plot_tweets():
    with open('../Data/tweets.csv', 'r') as csv_file:
        # De 'reader' variabele bevat alle rijen uit het csv bestand en filtert alle cellen met NULL waarde eruit.
        reader = csv.reader((l.replace('\0', '') for l in csv_file))
        next(reader)

        # De map hieronder zet alle uren, minuten, seconden en milliseconden uit de datum om naar 0.
        dates = map(lambda dt: dt.replace(hour=0, minute=0, second=0, microsecond=0),
                    # De map hieronder zet alle resultaten uit de vorige filter om in een datum.
                    # De seconden variabele is de eerste index uit elke rij -> u[0]
                    map(lambda u: datetime.datetime.fromtimestamp(int(u[0])),
                        # De filter hieronder filtert alle lege rijen eruit.
                        filter(lambda i: i != [], reader)))

        # Met numpy worden alle datums bij elkaar opgeteld die vaker voorkomen en in de 'y' variabele gestopt.
        x, y = np.unique(list(dates), return_counts=True)

        # Vervolgens wordt er een plot van gemaakt.
        plt.plot(x, y)

        # Als laatste wordt de plot weergegeven.
        plt.show()


def plot_nu_nl():
    with open('../Data/nu_nl.csv', 'r') as csv_file:
        reader = csv.reader((l.replace('\0', '') for l in csv_file))
        next(reader)

        dates = map(lambda dt: dt.replace(hour=0, minute=0, second=0, microsecond=0),
                    map(lambda u: datetime.datetime.fromtimestamp(u),
                        map(lambda o: int(o[0].split(".")[0]),
                            filter(lambda i: i != [], reader))))

        x, y = np.unique(list(dates), return_counts=True)
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    plot_tweets()
