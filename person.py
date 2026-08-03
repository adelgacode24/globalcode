def get_age():
  age=int(input("Enter your  age: "))
  return age

def get_name():
  name=input("Enter your  name: ")
  return name
  
result_age=get_age()
result_name=get_name()


print(f"Your name is {result_name}. You are {result_age} years old")


