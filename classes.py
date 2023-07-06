# flight booking function using oops given capacity of flight and passenger list:
# define class flight 
class Flight ():
  def __init__ (self, capacity):
    self.capacity = capacity
    self.passengers = [] # empty list of passengers
 
  # first check if open seats 
  def open_seats(self): 
    return self.capacity - len(self.passengers) 
    
  # method/ function to add new passengers 
  def add_passenger (self, name): 
    if not self.open_seats():
      return False # no open seats- error 
    self.passengers.append(name)
    return True # ALL ok

    
# initialize a flight based on this class 
flight=Flight(3)
people =["John", "Ron", "shawna"]
for person in people:
  success= flight.add_passenger(person)
  if success:
    print (f"Added{person}to flight successfully.")
  else:
    print (f"Failed to add{person}to flight. No seats!")