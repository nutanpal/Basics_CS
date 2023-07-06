# # Functional programming : decorators are functions that take a function1 as input as any value and modify the function1 as return as new fun2.
# # announce is the decorater function taking function f as input , modify and return as a new wrapper function.
# # Decorators add quickly add additional capabilites to framework like django
# def announce(f):
#   def wrapper():
#     print("About to run the function..")
#     f()
#     print("Done running the function")
#   return wrapper

# @announce # @-adds decorator function (announce) to hello function
# def hello():
#     print("Hello work!")

# hello()

def announce(f):
  def wrapper():
    print("About to run the function..")
    f()
    print("Done running the function")
  return wrapper
@announce
def hello():
  print("Hello work!")
hello()