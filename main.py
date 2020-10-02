from pages.booking_page_object import BookingPageObject
from tests.test_scenario_1 import TestScenario1
from tests.test_scenario_2 import TestScenario2
import os
import sys

if __name__ == '__main__':
    choose_browser = os.environ.get('BROWSER', 'CHROME')

    if choose_browser not in BookingPageObject.drivers:
        print('{} is not supported. Choose one of {}'.format(choose_browser, ','.join(BookingPageObject.drivers.keys())))
        sys.exit(-1)

    page = BookingPageObject(choose_browser)
    TestScenario1(page).run()
    page = BookingPageObject(choose_browser)
    TestScenario2(page).run()