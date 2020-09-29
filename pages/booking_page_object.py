from selenium import webdriver

class BookingPageObject:
    def __init__(self, webdriver_engine='CHROME'):
        drivers = {
            'CHROME': webdriver.Chrome,
            'FIREFOX': webdriver.Firefox
        }
        self.driver = drivers[webdriver_engine]()

    def visit(self, url='https://booking.com'):
        self.driver.get(url)