
# 1
firstname = input('Your First name: ')
lastname = input('Your Last name: ')
age = input('How old are you: ')
phone = input('Phone number: ')
print('Your last name is: ' + lastname + ' Your first name is: ' + firstname + ' Your age is: ' + age + ' Your Phone number is: ' + phone)
# 2
a = int(input("Enter a: "))
b = int(input("Enter b: "))
S = a * b
print('Area is: ' + str(S))
# 4
import math

a = int(input('Enter number: '))
b = math.pow(a, 2) / 3
c = (math.pow(a, 2) + 4) / 6
d = math.sqrt(math.pow(a, 2) + 4) / 4
e = math.sqrt(math.pow(math.pow(a, 2) + 4, 3)) / 4
Y = b + c + d + e
print(float(Y))
# 5
import math

a = int(input('Pls, do 3 steps: 1) think any number multiply it to 5 2)add 8 3) multiply to 2 '))
b = (((a / 2) - 8) / 5)
print('Your number is: ' + str(b))
# 2.1
import math

a = int(input('First number: '))
oper = str(input('Operation (+,-,/,*): '))
b = int(input('Second number: '))
if oper == '+':
    print(a + b)
elif oper == '-':
    print(a + b)
elif oper == '*':
    print(a * b)
else:
    print(a / b)
# 2.2
import math

a = int(input('First number: '))
oper = str(input('Operation (+,-,/,*): '))
b = int(input('Second number: '))

if oper == '+':
    print(a + b)
elif oper == '-':
    print(a + b)
elif oper == '*':
    print(a * b)
else:
    if b == 0:
        print("It's impossible")
    else:
        print(a / b)
# 2.3
a = 5


def myfunction(a):
    if a > 10 and a != 12 and a <= 15:
        return True
    elif a == 18:
        return True
    else:
        return False


print(bool(myfunction(a)))
# 2.4
a = 34
while a < 67:
    if a % 2 == 0:
        print(int(a))
    a += 1
# 2.6
a = 1
while a <= 100:
    if a >= 1 and a < 50 or a == 100:
        print(int(a))

    a += 1
a = 1
for a in range(101):
    if a >= 1 and a < 50 or a == 100:
        print(a)
# 2.7
a = str(input('Enter the word: '))
b = int(input('Enter the number: '))
for a in a:
    print(str(a) * b)

