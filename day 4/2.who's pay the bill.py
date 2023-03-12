import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_names=len(names)-1 #the number of item in a list
ran_number=random.randint(0,num_names) # random number between 0 to the number in the list
pay=names[ran_number] #who will pay?
print(f"{pay} is going to buy the meal today!")