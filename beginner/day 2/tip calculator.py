print("welcome to the tip calculator")
bill=int(input("wat was the total bill? "))
percent=int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("how many people to split the bill? "))
cost=(bill+bill*percent/100)/people
print(f"each person should pay: {cost}")
