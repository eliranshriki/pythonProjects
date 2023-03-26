import calculator_art
def add(n1, n2):
  return (n1 + n2)

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  if n2==0:
    return "You can't divide whith 0 !!!"
  return n1 / n2

operetion={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  print(calculator_art.logo)
  num1 = float(input("what is your first number?: "))
  for key in operetion:
    print (key)
  calc_continue = True
  while calc_continue:
    operetion_symbol= input("pick an operation: ")
    num2= float(input("what is your second number?: "))
    calculation_function = operetion[operetion_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operetion_symbol} {num2} = {answer}")
    should_continue = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation.: ").lower()
    if should_continue == "y":
      num1=answer
    else:
      calc_continue=False
      calculator()

calculator()





