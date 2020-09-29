class TestScenario1:
    def __init__(self, page_object):
        self.page_object = page_object

    def run(self):
        self.page_object.visit()