import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    get_twitter()


def get_string():
    return 'Hello world!'


def get_twitter():
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        url = "https://twitter.com/search?q=%23Windmolens&src=typd&lang=nl"
        browser.get(url)
        time.sleep(1)

        body = browser.find_element_by_tag_name('body')

        for i in range(100):
            body.send_keys(Keys.PAGE_DOWN)

        tweets = browser.find_elements_by_class_name('tweet-text')

        file = open("Files/tweets.csv", mode="w", encoding="utf-16")
        for tweet in tweets:
            tweet = tweet.text.replace(',', '').replace('\n', '')
            file.write(tweet+'\n')
        file.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
