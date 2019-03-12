import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    get_omroepzeeland()


def get_string():
    return 'Hello world!'


def get_omroepzeeland():
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        url = "https://www.omroepzeeland.nl/zoeken?query=windmolens"
        browser.get(url)
        time.sleep(1)

        # click on next page
        element = browser.find_element_by_link_text("Volgende").click()


        body = browser.find_element_by_tag_name('body')

        for i in range(100):
            body.send_keys(Keys.PAGE_DOWN)



        articles = browser.find_elements_by_class_name('description')


        file = open("Data/berichten.csv", mode="w", encoding="utf-16")
        for articles in articles:
            articles = articles.text.replace(',', '').replace('\n', '')
            file.write(articles+'\n')
        file.close()
3

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
