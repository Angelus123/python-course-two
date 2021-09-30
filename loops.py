"""For loop"""
# for x in "Python":
#     print (x)
# for x in ['a', 'b', 'c']:
#     print(x)

for x in range(20):
    print (x) 
for x in range(1, 20):
    print (x) 
print (type(range(3,100,5)))
 
#  For else
# with flag 
# names = ["AJohn", "Mary"]
# found =False
# for name in names:
#     if name.startswith('J'):
#         print(f'{name} found')
#         found =True
#         break
# if not found:
#     print ("Not found")


names = ["John", "Mary"]
for name in names:
    if name.startswith('J'):
        print(f'{name} found')
        break
else:
    print ("Not found")

"""While loops"""
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
print("Done")