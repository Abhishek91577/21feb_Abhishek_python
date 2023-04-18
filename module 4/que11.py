"""write a python class named circle construct by a radius and two methods which will compute the area and the perimeter of cicle"""
class circle:
    def _init_ (self,r):
        self.radius=r

        def area(self):
            return self.radius**2*3.14

            def perimeter(self):
                return 2*self.radius*3.14
newcircle=circle()
print(newcircle.area())
print(newcircle.perimeter())