# name = input ("Name:")
# print ("Hello," + name)
# print(f"Nice to meet you {name}")
# # conditions
# num = int(input("Number:"))
# if num > 0:
#   print(f"{num} is positive")
# elif num < 0:
#   print(f"{num} is negative")
# else:
#   print(f"{num} is 0")
  ######2-sequences
  #tupple-immutable, list -mutable,set-collection of unique values, dictionary - key-value pairs

# name ="Harry"
# print (name[3])
# # tupple - pair of 2 values representing a point . Cant add new /delete values in same tupple.
# names = ["ron","harry","jj","pary","aj","pj"]
# names.sort()
# names.append("np")
# print (names)
# # create a set
# s= set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.remove(3)
# s.add(5)
#s.add(5)
# print(f"set {s} has{len(s)} elements.")
##########Loops, Range ####
# for i in [1,2,3,4,5]:
#   print(i)
# names = ["ron","harry","jj","pary","aj","pj"]
# for i in range(len(names)):
#   # print (  names[i])
#   print("hello "+ names[i])
#   print(f"hello {(names[i])}. How are you?")
####Dictionary###
# houses={"harry":"Green","ron":"Red","jj":"yellow"}
# print(houses["harry"])
# houses["pj"] = "Red"
# print(houses["pj"])
# name = "jazz"
# for char in name:
#   print(char)

#########Functions ####
def square(x):
  return x*x
  
for i in range (10):
#   print (square(i))
  print (f"The square of {i}is {square(i)}.")
### import - calling functions from othe files
