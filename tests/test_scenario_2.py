import os

class TestScenario2:
    def __init__(self, page_object):
        self.page_object = page_object
        self.report_path = os.path.join(os.environ.get('REPORT_DIR', '.'), '{}.txt'.format(self.__class__.__name__))

    def run(self):
        report_file = open(self.report_path, 'w')
        try:
            report_file.write("Test_scenrio_2 start \n")
            self.page_object.visit()
            self.page_object.choose_city()
            report_file.write(self.page_object.kyiv_city())
            if_open_calendar = self.page_object.checking_open_calendar()
            if if_open_calendar == 1:
                print('calendar for specifying check in date is opened')
                report_file.write("calendar for specifying check in date is opened \n")
            else:
                print('calendar for specifying check in date is not opened')
                report_file.write("calendar for specifying check in date is not opened \n")
            report_file.write(self.page_object.not_booking_date())
            self.page_object.view_price()
            report_file.write(self.page_object.calendar_open())
            report_file.write(self.page_object.list_hotels_open())
            report_file.write(','.join(self.page_object.select_dates()) + '\n')
            self.page_object.search_result()
            report_file.write(self.page_object.information_about_room())
            self.page_object.browser_close()
            report_file.write("Test Scenario_2 finished")
        finally:
            report_file.close()









