from selenium import webdriver
from selenium.webdriver.support import wait

class BookingPageObject:
    guests_number_button_xpath = '//*[@id="xp__guests__toggle"]/span[2]'
    child_number_button_xpath = '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]'
    child_age_button_xpath = '// select[ @ name = "age"]'
    city_choose_field_xpath = '//*[@id="ss"]'
    kyiv_city_xpath = '//*[@id="frm"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    calendar_button_xpath = '//*[@id="frm"]/div[1]/div[2]/div[2]/div'
    calendar_date_xpath = '//td[@data-bui-ref="calendar-date"]'
#   booking_dates_class_name = 'class="bui-calendar__date bui-calendar__date--selected"'
    view_price_button_xpath = '//*[@id="frm"]/div[1]/div[4]/div[2]/button'
    calendar_open_view_xpath = '//*[@id="frm"]/div[3]/div/div[2]/div'
    first_date_calendar_xpath = '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[4]'
    second_date_field_xpath = '//*[@id="frm"]/div[3]/div/div[1]/div[2]/div/div/div/div[2]'
    second_date_calendar_xpath = '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[6]'
    hotel_field_xpath = '//*[@data-hotel-id]'
    hotel_field_class = 'room_details'
    search_button_xpath = '//*[@id="frm"]/div[5]/div[2]/button'
    drivers = {
        'CHROME': webdriver.Chrome,
        'FIREFOX': webdriver.Firefox
    }

    def __init__(self, webdriver_engine='CHROME'):
        self.driver = BookingPageObject.drivers[webdriver_engine]()

    def visit(self, url='https://booking.com'):
        self.driver.get(url)

    def choose_number_guests(self):
        driver = self.driver
        guests_count_button = driver.find_element_by_xpath(BookingPageObject.guests_number_button_xpath)
        guests_count_button.click()

#  def random_number_children(self):
#       number_children = random.randint(1,10)
#        return number_children


    def choose_number_children(self, random_number_children):
        driver = self.driver
        children_count_button = driver.find_element_by_xpath(BookingPageObject.child_number_button_xpath)
        i = 0
        while i != random_number_children:
            children_count_button.click()
            i = i + 1

    def get_age_selects_count(self):
        driver = self.driver
        count_fields_age = driver.find_elements_by_xpath(BookingPageObject.child_age_button_xpath)
        driver.implicitly_wait(30)
        return len(count_fields_age)

    def choose_city(self):
        driver = self.driver
        choose_city_button = driver.find_element_by_xpath(BookingPageObject.city_choose_field_xpath)
        choose_city_button.click()

    def kyiv_city(self):
        driver = self.driver
        kyiv_city_button = driver.find_element_by_xpath(BookingPageObject.kyiv_city_xpath)
        kyiv_city_button.click()
        print('Kyiv is a city')
        city = 'Kyiv is a city'
        return city

    def checking_open_calendar(self):
        driver = self.driver
        calendar_button = driver.find_element_by_xpath(BookingPageObject.calendar_button_xpath)
        if calendar_button.is_displayed():
            return 1

    def not_booking_date(self):
        driver = self.driver
        booking_dates_class_name = 'class="bui-calendar__date bui-calendar__date--selected"'
        calendar_dates = driver.find_elements_by_xpath(BookingPageObject.calendar_date_xpath)
        booking_dates_calendar = calendar_dates.count(booking_dates_class_name)
        if booking_dates_calendar == 0:
            result = 'no result entry containing booking price or booking status \n'
            print('no result entry containing booking price or booking status')
        else:
            result = 'result entry containing booking price or booking status \n'
            print('result entry containing booking price or booking status')
        return result

    def view_price(self):
        driver = self.driver
        view_price_button = driver.find_element_by_xpath(BookingPageObject.view_price_button_xpath )
        view_price_button.click()

    def calendar_open(self):
        driver = self.driver
        driver.implicitly_wait(10)
        calendar_view = driver.find_element_by_xpath(BookingPageObject.calendar_open_view_xpath)
        if calendar_view.is_displayed():
            result = 'calendar for specifying check in date is opened \n'
            print('calendar for specifying check in date is opened')
        else:
            result = 'calendar for specifying check in date is not opened \n'
            print('calendar for specifying check in date is not opened')
        return result


    def list_hotels_open(self):
        driver = self.driver
        find_hotels = driver.find_elements_by_xpath(BookingPageObject.hotel_field_xpath)
        if len(find_hotels) < 1:
            result = 'page with listed hotels is empty \n'
            print('page with listed hotels is empty')
        else:
            result = 'page with listed hotels is opened \n'
            print('page with listed hotels is opened')
        return result

    def select_dates(self):
        driver = self.driver
        first_date_field = driver.find_element_by_xpath(BookingPageObject.first_date_calendar_xpath)
        in_date_selected = first_date_field.get_attribute('data-date')
        print('First date:' + first_date_field.get_attribute('data-date'))
        first_date_field.click()
        second_date_field = driver.find_element_by_xpath(BookingPageObject.second_date_field_xpath)
        second_date_field.click()
        second_date_select = driver.find_element_by_xpath(BookingPageObject.second_date_calendar_xpath)
        out_date_selected = second_date_select.get_attribute('data-date')
        print('Second date:'+ second_date_select.get_attribute('data-date'))
        second_date_select.click()
        return in_date_selected, out_date_selected

    def search_result(self):
        driver = self.driver
        search_hotels_result = driver.find_element_by_xpath(BookingPageObject.search_button_xpath)
        search_hotels_result.click()

    def information_about_room(self):
        driver = self.driver
#        find_hotels = driver.find_elements_by_xpath(BookingPageObject.hotel_field_xpath)
        find_hotels = driver.find_elements_by_class_name(BookingPageObject.hotel_field_class)
        if len(find_hotels) < 26:
            result = 'each result entry has booking price or banner saying no free places \n'
            print('each result entry has booking price or banner saying no free places')
        else:
            result = 'not each result entry has booking price or banner saying no free places \n'
            print('not each result entry has booking price or banner saying no free places')
        return result

    def browser_close(self):
        driver = self.driver
        driver.quit()




































