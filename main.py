from pages.booking_page_object import BookingPageObject
from tests.test_scenario_1 import TestScenario1

if __name__ == '__main__':
    page = BookingPageObject()
    TestScenario1(page).run()