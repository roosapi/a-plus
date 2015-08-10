import unittest

from test_initializer import TestInitializer
from page_objects import TeachersPage, LoginPage, CourseName

class StaffPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = TestInitializer().getFirefoxDriverWithLoggingEnabled()
        LoginPage(self.driver).loginAsAssistant()

    @unittest.skip
    def testShouldOpenAllAssistantsViewSubmissionPages(self):
        linkCount = len(AssistantsPage(self.driver).getSubmissionLinks())

        for x in range(0, linkCount):
            assistantsPage = AssistantsPage(self.driver)
            assistantsPage.clickSubmissionLink(x)
            self.assertTrue('/exercises/' + str(x + 1) + "/submissions/" in str(self.driver.current_url))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
