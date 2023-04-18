"""write python program that user to enter only odd numbers else will raise an exception"""
try:
    even_numbers =[2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("denominator cannot be 0")
except IndexError:
    print("Index out of bond.")