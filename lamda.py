# lambda functions in python
def square(x):
  return x*x
print(square(20))
# funname lambda input : output 
squarex = lambda x:x**2
print (squarex(9))
# sorting objects based on name 
people=[
  {"name":"a","house":"K"},
  {"name":"t","house":"G"},
  {"name":"b","house":"J"}
  ]
#key argument to the sort function, which specifies which part of the dictionary we wish to use to sort:
def f(person):
  return person['name']
people.sort(key =f)
print (people)
# shortcut lambda function
people.sort(key=lambda person:person["house"])
print (people)