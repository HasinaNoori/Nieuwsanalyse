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
        #chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        url = "https://www.omroepzeeland.nl/zoeken?query=windmolen"
        browser.get(url)
        time.sleep(1)

        body = browser.find_element_by_tag_name('body')

        total_articles = []

        for i in range(100):
            scroll_button = browser.find_element_by_link_text('Volgende')
            browser.execute_script("arguments[0].click();", scroll_button)
            articles = browser.find_elements_by_class_name('description')

            for article in articles:
                total_articles.append(article)

            body.send_keys(Keys.END)

        file = open("Data/berichten.csv", mode="w", encoding="utf-16")
        for total_articles in total_articles:
            total_articles = total_articles.text.replace(',', '').replace('\n', '')
            file.write(total_articles+'\n')
        file.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()