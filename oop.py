import re, abc


class Employee(object):
    """Base Class for Employees"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, fname, lname, SSN, job_group, salary, allowances={}):
        self.fname = fname
        self.lname = lname
        self.__SSN = SSN
        self.job_group = job_group
        self.salary = salary
        self.allowances = allowances
        for k, v in self.allowances.items():
            self.allowances[k] = v

    def __str__(self):
        return "{0} {1}".format(self.fname, self.lname)

    @abc.abstractmethod
    def promote(self, job_group):
        """
            Raise employee's salaray and/or change job group
        """
        raise NotImplementedError

    def get_full_name(self):
        return self.fname + " " + self.lname

    def get_ssn_number(self):
        if self.__SSN is not None:
            return self.__SSN

    def set_ssn_number(self, ssn_number):
        """
            Set Social Security Number(SSN) of employee
        """
        if self.is_valid_ssn_number(ssn_number):
            self.__SSN = ssn_number
        else:
            raise ValueError("Invalid Social Security Number")

    def is_valid_ssn_number(self, number):
        """
            Check if number passed as an argument for setting
            employee Social Security Number(SSN) is of valid format
            Valid format (3 digits)-(4 digits)-[2-4 optional characters]
        """
        valid_ssn = re.compile(r'^\d{3}-\d{4}(-[A-Z0-9]{2,4})?$')
        match_object = valid_ssn.search(number)
        return True if match_object is not None else False


class JuniorDeveloper(Employee):
    """Junior Developer Class"""

    number_of_developers = 0

    def __init__(self, fname, lname, SSN, job_group, salary, allowances, repos):
        super(JuniorDeveloper, self).__init__(fname, lname, SSN, job_group, salary, allowances)
        self.repos = repos
        JuniorDeveloper.increment_count()

    def promote(self):
        if self.repos >= 3 and self.repos < 5:
            self.salary += 12000
        elif self.repos > 5 and self.repos < 10:
            self.salary += 21000
            self.allowances['house'] = 6000
        else:
            self.job_group = 'B'
            self.salary += 32000
            self.allowances['house'] = 9000
            self.allowances['commuter'] = 6000

    def take_leave(self):
        fullname = self.get_full_name()
        return fullname + " - [Junior Developer] has taken leave"

    def get_full_name(self):
        """
            Overide the default method from parent class
        """
        return self.fname + " " + self.lname + " - JD"

    @staticmethod
    def increment_count():
        JuniorDeveloper.number_of_developers += 1

    @staticmethod
    def find_all():
        """
            Find all Junior Developers
        """
        return JuniorDeveloper.number_of_developers


class SalesManager(Employee):
    def __init__(self, fname, lname, SSN, job_group, salary, allowances={}, turnover=0):
        super(SalesManager, self).__init__(fname, lname, SSN, job_group, salary, allowances)
        self.turnover = turnover

    def promote(self):
        if self.turnover < 100000:
            self.salary += 3000
        elif self.turnover > 100000 and self.turnover < 300000:
            self.salary += 7000
            self.allowances['house'] = 12000
        else:
            self.salary += 11000
            self.allowances['house'] = 20000
            self.allowances['commuter'] = 15000
            self.allowances['entertainment'] = 10000

    def take_leave(self):
        fullname = self.get_full_name()
        self.allowances['paid_leave'] = 1000
        leave_pay = self.allowances['paid_leave']
        return fullname + " - [Sales Manager] has taken leave. Allowance is " + str(leave_pay)


# jd = JuniorDeveloper("Luke", "Olali", "431-2228-AB32", "A", 15000, {"Travel": 3000}, repos=1) 

# jd2 = JuniorDeveloper("Larry", "Page", "111-231", "A", 15000, allowances={}, repos=2)


# sm = SalesManager("Sergey", "Brin", "312-656-CT7", "D", 30000, {"Commuter": 10000}, turnover=150000)

# print(jd.get_full_name())
# print()
# print(jd2)
# print(jd.get_full_name())
# print()
# print(sm)

# employees = [jd, jd2, sm]
# print()
# for staff in employees:
#     print(staff.take_leave())
# print()
# developer_count = JuniorDeveloper.find_all()
# print("Number of developers in Cohort X: " + str(developer_count))
# num_devs = jd.find_all()
# print('Number of developers from instance: ' + str(num_devs))
