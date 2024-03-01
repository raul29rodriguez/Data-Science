'''Exercise 1
You are driving on a highway with your vehicle and in front of you a car is stopped. You are
asked to enter the speed of your vehicle (in km/h) and the distance between your vehicle and
the stopped one (in meters). Using a lambda that accepts the parameters distance and speed,
compute the time to collision (in seconds)
Note: Formula of speed (v): v =s/t, where s is distance and t is time'''
speed=int(input("Enter how fast you are going in km/h: "))
distance=int(input("Enter the distance between you and the vehicle in meters: "))
time = lambda speed,distance: distance/speed
print("time to collision is",time(speed,distance),"seconds")
