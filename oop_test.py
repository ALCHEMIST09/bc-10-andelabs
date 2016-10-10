import unittest


from oop import Employee, JuniorDeveloper, SalesManager


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.jd = JuniorDeveloper(
            'Luke', 'Muga', '312-1119', 'A', 15000, {'Transport': 800}, repos=1)
        self.jd2 = JuniorDeveloper(
            'Mark', 'Zuckerberg', '119-4430', 'A', 12000, {}, repos=1)
        self.sm = SalesManager('Beth', 'Wanjiku', '328-1538',
                               'A', 10000, {'Transport': 2000}, turnover=90000)

    def test_cannot_instantiate_base_class(self):
        with self.assertRaises(TypeError):
            Employee()

    def test_junior_developer_is_subclass_of_employee(self):
        """
            Test whether JuniorDeveloper class is sub class of Employee
        """
        self.assertIsInstance(self.jd, JuniorDeveloper,
                              msg="Class not an instance of Employee")

    def test_sales_manager_is_subclass_of_employee(self):
        """
            Test whether SalesManager class is sub class of Employee
        """
        self.assertIsInstance(self.sm, SalesManager,
                              msg="Class not an instance of Employee class")

    def test_returns_full_name(self):
        """
            Test whether classes other than Junior Developer
            class return full names derived from concatenating
            first name and last name
        """
        full_name_sm = self.sm.get_full_name()
        self.assertEqual(full_name_sm, "Beth Wanjiku",
                         msg="Test should return result of joining first and last name")

    def test_developer_returns_custom_name(self):
        """
            Test whether instances of JuniorDeveloper class have
            full names that have a ' - JD ' suffix
        """
        custom_name = self.jd.get_full_name()
        self.assertEqual(custom_name, "Luke Muga - JD",
                         msg="Test should return fullname with a ' -JD' suffix")

    @unittest.skip("Work in Progrss: Figuring how to mock static methods")
    def test_junior_developer_count(self):
        """
            Test for number of JuniorDeveloper objects instantiated
        """
        num_of_devs = self.jd.find_all()
        self.assertEqual(
            2, num_of_devs, msg='Test shoud reurn number of developer objects instantiated in memory')

    def test_raises_error_for_invalid_ssn_number(self):
        """
            Test for invalid format of Social Security Number(SSN)
        """
        ssn_number = '12B-154A-028'
        with self.assertRaises(ValueError):
            self.jd2.set_ssn_number(ssn_number)

    def test_sales_manager_can_take_leave(self):
        sm_mesg = self.sm.take_leave()
        # self.assertEqual(
        #     jd_mesg, "Luke Muga - JD - [Junior Developer] has taken leave")
        self.assertEqual(
            sm_mesg, "Beth Wanjiku - [Sales Manager] has taken leave. Allowance is " + str(self.sm.allowances['paid_leave']))

    def test_junior_developer_can_take_leave(self):
        jd_mesg = self.jd.take_leave()
        self.assertEqual(
            jd_mesg, "Luke Muga - JD - [Junior Developer] has taken leave")


if __name__ == '__main__':
    unittest.main()
