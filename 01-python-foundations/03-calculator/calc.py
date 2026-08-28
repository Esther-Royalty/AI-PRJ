continue_calc = "yes"
print("Hello, lets get started!")

while continue_calc == "yes":
  try:
    num1 = float(input("Enter first number:\n"))
  except:
    print("That\'s not a valid number.")
  try:
    num2 = float(input("Enter second number:\n"))
  except:
    print("That\'s not a valid number.")
  stat = input("Choose operation (+, -, *, /)\n")
  if stat == "+":
    print(num1 + num2)

  elif stat == "-":
    print(num1 - num2)

  elif stat == "*":
    print(num1 * num2)
    
  elif stat == "/":

    if num2 == 0:
        print("Cannot divide by 0")
    else:
        print(num1 / num2)

  else:
    print("Please choose a valid arithmetic operation!")

  continue_calc = input("Would you like to continue? yes/no:\n").lower()
