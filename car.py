"""You are curious about the most popular and least popular colours of cars and decide to write a program to calculate the frequency of car colours.

Your program should read in the colour of each car until a blank line is entered, and then print out (in any order) all the different colours of car with counts.

For example:

Car: red
Car: white
Car: blue
Car: green
Car: white
Car: silver
Car: 
Cars that are red: 1
Cars that are white: 2
Cars that are blue: 1
Cars that are green: 1
Cars that are silver: 1"""

car_colour_counts = {}

while True:
  car_color = input("Car: ").strip()
  if car_color = '':
    break


car_color_counts[car_color] = car_color_counts.get(car_color, 0)+1

for color, counts in car_color_counts.items():
  
                    
