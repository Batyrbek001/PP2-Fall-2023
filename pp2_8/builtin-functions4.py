import time
import math
 
def square_root(number):
    return math.sqrt(number)
 
number = float(input("Sample Input:\n "))
milliseconds = int(input("Sample Output:\n "))
time.sleep(milliseconds / 1000.0)
result = square_root(number)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")