time = input("What time is it? ").strip() # -------> Ask user input
# make a list of user input
def main():
  tick = []
  for i in time:
    tick.append(i)
  return tick

# set up convert function
def convert(time):
# Check the lenght condition (if lenght == 4) ---> breakfast time
  if len(time) == 4:

    # Convert string to float
    def convert1():
      time_2_1 = float(time[0])
      time_2_2 = float(time[2])
      time_2_3 = float(time[3])
      return time_2_1, time_2_2, time_2_3
    time_1, time_2, time_3 = convert1()

# Check the condition for breakfast time
    if time_1 == 7 and 0 <= time_2 <= 5 and 0 <= time_3 <= 9:
      print("breakfast time")

    elif time_1 == 8 and time_2 == 0 and time_3 == 0:
      print("breakfast time")

# check the lenght condition (if lenght == 5) -------> lunch time or dinner time
  elif len(time) == 5:
    
    # Convert string to float
    def convert2():
      time_4_1 = float(time[0])
      time_4_2 = float(time[1])
      time_4_3 = float(time[3])
      time_4_4 = float(time[4])
      return time_4_1, time_4_2, time_4_3, time_4_4
    time_4, time_5, time_6, time_7 = convert2()

# Check the condition for lunch time
    if time_4 == 1 and time_5 == 2 and 0 <= time_6 <= 5 and 0 <= time_7 <= 9:
      print("lunch time")
    elif time_4 == 1 and time_5 == 3 and time_6 == 0 and time_7 == 0:
      print("lunch time")

# Check the condition for dinner time
    elif time_4 == 1 and time_5 == 8 and 0 <= time_6 <= 5 and 0 <= time_7 <= 9:
      print("dinner time")

    elif time_4 == 1 and time_5 == 9 and time_6 == 0 and time_7 == 0:
      print("dinner time")

convert(main())