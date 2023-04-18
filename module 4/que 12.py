"""what is relationship appopriate for course and faculty."""
class course:
    id=0
    sub=""

    def getdata(self):
        self.id=input("Enter ID:")
        self.sub=input("Enter subject:")

class faculty(course):
    def printdata(self):
        print("ID:",self.id)
        print("subject",self.sub)
fn=faculty()
fn.getdata()
fn.printdata()