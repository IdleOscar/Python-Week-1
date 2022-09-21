# 1
import math

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
h = int(input("Enter 3rd value: "))
S = (((a ** 2 + b) * h) / (2 * (a - b) + 4))
print("S={0:.2f}".format(S))
# 2
import math

x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))
h = (math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(math.e ** x + math.e ** (-x))) / (
            ((math.e ** -x + math.e ** x) ** 3) + (math.sin(4 * y) + math.cos(2 * y) - 2) ** 2))
print("H={0:.2f}".format(h))
# 3(1)
import math

x = 2
y = 1
S = (((x ** y) ** x) + ((x ** x) ** y) - x ** 4)
print("S={0:.2f}".format(S))
# 3(2)
import math

x = 1
y = 4
z = 3
S = ((math.fabs((1 / math.tan(x)) + 6)) ** (1 / 3) + math.sqrt(((x + 1) ** 3) / (4 * y - 2 * z)))
print("S={0:.2f}".format(S))
# 3(3)
import math

x = 3
y = 0.2
S = (((5 * x * y) / ((x ** 3) - 4)) + math.exp(x ** 2) + math.sqrt((math.cos(y)) ** 2 - y ** 2))
print("S={0:.2f}".format(S))
# 3(4)
import math

x = 3
y = 5
S = (math.sqrt(math.fabs(y)) + ((math.atan(math.log(x)) ** 3) / ((x * y) - y + 1)))
print("S={0:.2f}".format(S))
# 3(2.1)
import math

x = 3
y = 1
z = 2
S = (4) ** x * y - (x) ** y * z + (x * y) ** z
print("S={0:.2f}".format(S))
# 3(2.2)
import math

x = 2
y = 2
z = 1
S = (4 * abs(x) - x * y * ((z) ** 2)) / (x + math.exp(y * x) - 2 * y * z)
print("S={0:.2f}".format(S))
# 3(2.3)
import math

x = 0.8
y = 0.1
z = 4
S = math.sqrt((1 - x + (1 / math.atan(x - 7 * y))) / (4 * x * z - (math.log(y)) ** 2))
print("S={0:.2f}".format(S))
# 3(2.4)
import math

x = 3
y = 1
z = 3
S = (2 * 3 * 4) / (math.pow(math.sin(x), 3) + math.pow(math.tan(y), 3)) - math.sqrt(math.pow(z, x - y))
print("S={0:.2f}".format(S))
# 3(3.1)
import math

x = 4
S = (math.pow(math.log(x - 3), 4)) + math.pow(2, x) * math.pow(math.sin(3 * x), 2) / (4 * x - 5.2))
print("S={0:.2f}".format(S))
# 3(3.2)
import math

x = 2
y = 2
z = 1
S = math.sqrt(0.6 * x * y * z) + math.pow(math.pow(y, x), 2) - math.exp(math.sin(2 * (x ** 2))))
print("S={0:.2f}".format(S))
# 3(3.3)
import math

x = 0.5
y = 2
S = (math.asin(x ** 3) - 6) / (8 * (math.cos(4 * y) - math.sin(4 * x))))
print("S={0:.2f}".format(S))
#3(3.4)
import math

x = 2
y = 1
z = 3
S = (abs(math.log(x ** 3)) + math.exp(2 * x)) / (x + 3.4) - (1 / math.pow(math.tan(3 / (x * y * z), 3)
                                                             print("S={0:.2f}".format(S))
# 2(Mistake in the pdf should be 4)
import math

a = int(input("Enter 1st side of triangle"))
b = int(input("Enter 2nd side of triangle"))
S = a * b / 2
c = math.sqrt(math.pow(a) + math.pow(b))
P = a + b + c
print("area is: " + str(S))
print("third side is: " + str(c))
print("Perimetr is: " + str(P))
# 3(Mistake in the pdf should be 5)
import math

a = int(input('Enter a by quadratic equation is ax2+bx+c=0: ')
x = int(input('Enter x by quadratic equation is ax2+bx+c=0: ')
b = int(input('Enter b by quadratic equation is ax2+bx+c=0: ')
c = int(input('Enter c by quadratic equation is ax2+bx+c=0: ')
D = b ** 2 - 4 * a * c
first = 0
second = 0
if D > 0:
    first = (b - math.sqrt(D)) / a
second = (b + math.sqrt(D)) / a
print('First value is: ' + first)
print('Second value is: ' + second)

elif D == 0:
first = (b - math.sqrt(D)) / a
print('Algorithm have 1 value: ' + first)
else:
print('Algorithm doesnt have any value')
# 4(Mistake in the pdf should be 6)
import math

Figure = int(input('What figures area you gonna execute choose 1-3 where 1 is rectangle, 2 is triangle, 3is cycle '))
if Figure == 1:
    a = int(input('input 1st side')
b = int(input('input 2nd side')
print('Area is: ' + str(a * b))
elif Figure == 2:
a = int(input('input 1st side')
b = int(input('input 2nd side')
c = int(input('input 3rd side')
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Area is:' + str(S))
elif Figure == 3:
a = int(input('input a radius of cycle'))
S = math.pi * math.pow(a, 2)
print('Area is:' + str(S))
else:
print('Enter the correct number')
