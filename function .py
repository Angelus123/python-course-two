# function

# def increment(number: int, by:int = 1) -> tuple:
#     return(number, number +by)


# print(increment(2))


"""args. wait, what?"""

# def multiply(a, b):
#     return a*b

# print(multiply(2,5))


# def multiply(*list):
#     total = 1 
#     for item in list:   
#         total *= item
#     return total

# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user)

# save_user(id=1, name="admin")

message = "a"
def greet():
    global message # bad practice evil
    message = "b"
   

greet()
print(message) 


    

