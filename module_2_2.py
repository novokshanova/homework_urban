first = int(input("первое число: "))
second = int(input("второе число: "))
third = int(input("третье число: "))
if first == second == third:
    print (3)
elif first == second or second == third or first == second:
    print (2)
else: print(0)