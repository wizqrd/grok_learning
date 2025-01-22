name_colour_dict = {}

while True:
  user_input = input("Enter a name and colour: ")
  if user_input = '':
    break

try:
  name, colour = user_input.split()
  name_colour_dict[name] = colour
except ValueError:
  print("Enter a name and colour.")

for name, colour in name_colour_dict.items():
  print(f"{name}, {colour}")
  

