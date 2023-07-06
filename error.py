# def div(x,y):
  # return x/y
# result = div(4,5)
# print(result)

# Handle 2 possible errors when user divide by zero or enters a string exit the system.
import sys
try:
  x = int(input('x:'))
  y = int(input('y:'))
except ValueError:
  print("error:invalid input type")
#exit the program using the system module 
  sys.exit(1)
try:
  result = x/y
except ZeroDivisionError:
  print("error:can't divide by zero")
  sys.exit(1)

print(f"{x}/{y}= {result}")
