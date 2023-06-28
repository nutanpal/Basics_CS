# from hello import square
# for i in range(5):
#   print (f"square of {i} is {square(i)}")

# you can either import specific function or import entire module and use some part.
# import hello
# for i in range(3):
#   print (f"The square of {i} is {hello.square(i)}")

#   ###Objects ## __init__ ######## class
# class Point():
#   def __init__(self, inp1, inp2):
#     self.x = inp1
#     self.y = inp2
# p=Point(2,8)
# print(p.x, p.y)
# create a function for booking flight within capacitoy 
class Flight():
  #method to create new flight with given capacity
  def __init__(self,capacity):
    self.capacity = capacity
    self.passengers =[] # empty list
   # method to return no of open open_seats
  def open_seats(self):
    return self.capacity - len(self.passengers)
#method to add passengers to flight; check capacity is not full
  def add_passengers(self,name):
    if not self.open_seats(): # if self.open_seats == 0;
      return False
    self.passengers.append(name)
    return True
#nb: 0= false, not true. when open_seats return 0, expression will be true.
# create a new flight with capacity 3 and list of people booking
flight = Flight(3)
people = ["H",'E',"L","O"]
for e in people:
  if flight.add_passengers(e):
    print(f"Added {e} to flight ...")
  else:
    print(f"No seat left for {e}.")
