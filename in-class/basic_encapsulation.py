class student:
    def __init__(self, fname, lname):
        self._firstname = fname
        self._lastname = lname

    def show_name(self):
        return f"{self._firstname} {self._lastname} "
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self,fname):
        self.firstname = fname




julie = student("Julie", "Cowley")

print(julie.show_name())
print(julie.firstname)
print(julie)
