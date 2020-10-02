from random import randint
import os


class TestScenario1:
    def __init__(self, page_object):
        self.page_object = page_object
        self.report_path = os.path.join(os.environ.get('REPORT_DIR', '.'), '{}.txt'.format(self.__class__.__name__))

    def run(self):
        report_file = open(self.report_path, 'w')
        try:
            report_file.write("Test_scenrio_1 start \n")
            self.page_object.visit()
            self.page_object.choose_number_guests()
            number_children = randint(1, 10)
            report_file.write('Number of Children = {}\n'.format(number_children))
            self.page_object.choose_number_children(number_children)
            count_age_fields = self.page_object.get_age_selects_count()
            if number_children == count_age_fields:
                print('The number of age inputs is equal to number of children \n')
                report_file.write('The number of age inputs is equal to number of children \n')
            else:
                print('The number of age inputs is not equal to number of children \n')
                report_file.write('The number of age inputs is not equal to number of children \n')
            self.page_object.browser_close()
            report_file.write("Test Scenario_1 finished")
        finally:
            report_file.close()