
#1
a = int(input('Price of candy for 1 kg: '))
b=1
c=0
for b in range(11):
    print('Price of ' + str(b) + 'kg ' + str(c))
    b+=1
    c+=a
#2
a = int(input('cuantity of number endind with 0: '))
d=0
c=0
b=0
while d<a:
    print(c)
    c+=10
    b+=c
    d+=1
print("The sum of: " + str(b-c))