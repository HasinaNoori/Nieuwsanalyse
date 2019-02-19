# alle urls zoeken met article list pak de url zet onder elkaar en dan alles open

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    get_nu_nl()


def get_nu_nl():
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        url = "https://www.nu.nl/tag/windmolens"
        browser.get(url)
        time.sleep(1)

        scroll_button = browser.find_element_by_link_text('Laad meer artikelen')
        browser.execute_script("arguments[0].click();", scroll_button)
        containers = browser.find_elements_by_xpath("//div[@class='block-content clearfix']")
        for i in containers:
            print(i)

        url_list = []

        for container in containers:
            urls_con = container.find_elements_by_class_name('trackevent')
            for url_con in urls_con:
                url_list.append(url_con.get_attribute('href'))

        for url in url_list:
            browser.get(url)

            time.sleep(1)



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
