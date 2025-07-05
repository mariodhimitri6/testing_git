class TestingClass():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def _modify_my_name(self, flag=False):
        if flag==True:
            self.fname = "daje"
        return self.fname

    def print_my_name(self):
        print(f"Hello my name is {self.fname} and my last name is {self.lname}")
        flag = self._modify_my_name(flag=True)
        print(f"{self.fname}")


initiate = TestingClass(fname = "John", lname="Smith")

initiate.print_my_name()