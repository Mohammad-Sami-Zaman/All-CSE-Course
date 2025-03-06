from google.colab import drive
drive.mount('/content/drive')

# First, we take 2 numbers as input from the user
# Read 2 numbers as input from the user means taking 2 numbers as input from the user using the input function
var_1 = input('Please enter the first number: ')
var_2 = input('Please enter the second number: ')

#Since input() function converts everything to String,
#for performing any kind of mathematical operation we need to convert them to int.
#For this conversion, we need to use the int() function


#But at first, we may clarify whether the inputs are actually Strings or not. 
print(type(var_1))
print(type(var_2))


#Then we convert the Strings to integer using the int() function
var_3 = int(var_1)
var_4 = int(var_2)

#===============================================================
#Input taking and conversion can be done in a single line as shown below
#var_1 = int(input('Please enter the first number: '))
#var_2 = int(input('Please enter the second number: '))

#===============================================================

#We may then perform Addition
total = var_3 + var_4

#Multiplication 
product = var_3 * var_4

#Substraction 
difference = var_3 - var_4

#And then print all the calculated results
print("Sum =", total)
print("Product =", product)
print("Difference =", difference)

import math 

# taking input from the user, then converting it to float
# since radius can be a floating point value

radius  = float(input("Please enter the radius value:")) 

# squares can be made using these 3 ways, as give in hints
# all 3 ways generates the same result for area

area = math.pi * radius ** 2 
print("Area is:", area)

area = math.pi * math.pow(radius, 2)
print("Area is:", area)

area = math.pi * radius * radius
print("Area is:", area)

#==============================================================
# TODO
# calculate circumference

#==============================================================

var_a = 7
var_b = 3
if(var_a>var_b):
   print('frist is greater')
else:
  print('second is greater')

var_c = -33
var_d = -3
if(var_c<var_d):
   print('second is greater')
else:
   print('first is greater')

var_e = 11
var_f = 11
if(var_e==var_f):
   print('the numbers are equal')
else:
  print('the numbers are not equal')

var_A = -40
var_B = -4
var_X = var_B-var_A
print(var_X)

var_A = 6
var_B = 2
var_Y = var_A-var_B
print(var_Y)

var_A = 5
var_B = 5
var_Z = var_A-var_B
print(var_Z)


var_a = 7
var_b = 2
var_X = var_a%var_b
if(var_X==0):
  print('number is even')
else:
  print('number is odd')

var_c = 10
var_d = 5
var_Y =var_c % var_d
if(var_Y==0):
   print('the number is even')
else:
   print('number is odd')

var_f = -44
var_e = 4
var_Z = var_f % var_e
if(var_Z==0):
  print('number is even')
else:
  print('number is odd')

 var_a= int(input('enter the number='))
var_S = var_a % 2
var_S = var_a % 5
if(var_S==0):
    print('number is multiple to 2 or 5')
    print(var_a)
else:
    print('number is not multiple to 2 or 5')
var_b = int(input('enter the number='))
var_S = var_b % 2
var_S = var_b % 5
if(var_S==0):
    print('number is multiple to 2 or 5')
    print(var_b)
else:
    print('number is not multiple to 2 or 5')
var_c = int(input('enter the number='))
var_S = var_c % 2
var_S = var_c % 5
if(var_S==0):
    print('number is multiple to 2 or 5')
    print(var_c)
else:
    print('number is not multiple to 2 or 5')

var_a = 6
print(var_a)
if(var_a%2==0 or var_a%5==0):
    print('the number is multiple of either 2 or 5')
else:
    print('the number is not multiple either 2 or 5')
var_b = 15
print(var_b)
if(var_b%2==0 or var_b%5==0):
    print('the number is multiple of either 2 or 5')
else:
    print('the number is not multiple either 2 or 5')
var_c = 10
print(var_c)
if(var_c%2==0 or var_c%5==0):
    print('the number is multiple of either 2 or 5')
else:
    print('the number is not multiple either 2 or 5')
var_d = 17
print(var_d)
if(var_d%2==0 or var_d%5==0):
    print('the number is multiple of either 2 or 5')
else:
    print('the number is not multiple either 2 or 5')

var_a = int(input("enter a number="))
print(var_a)
if(var_a%2==0 and var_a%5==0):
   print('number is both multiple to 2 and 5')
else:
  print('number is not multiple both to 2 and 5')

var_b = int(input("enter a number="))
print(var_b)
if(var_b%2==0 and var_b%5==0):
   print('number is both multiple to 2 and 5')
else:
  print('number is not multiple both to 2 and 5')

var_c = int(input("enter a number="))
print(var_c)
if(var_c%2==0 and var_c%5==0):
   print('number is both multiple to 2 and 5')
else:
  print('number is not multiple both to 2 and 5')

Time = 500
Hours = Time // 3600 
seconds1 = Time % 3600
minutes = seconds1 // 60
seconds = seconds1 % 60
print(Hours, end='h ')
print(minutes, end='min ')
print(seconds, end='s')

working_hour= int(input('please enter your working hours='))
print(working_hour)
if(working_hour>0 and working_hour<=40):
    salary1 = working_hour*200
    print(salary1)
elif(working_hour>40 and working_hour<168):
    salary2 = 8000 + (working_hour - 40) * 300
    print(salary2,)
else:
    print('value error')

working_hour= int(input('please enter your working hours='))
print(working_hour)
if(working_hour>0 and working_hour<=40):
    salary1 = working_hour*200
    print(salary1)
elif(working_hour>40 and working_hour<168):
    salary2 = 8000 + (working_hour - 40) * 300
    print(salary2,)
else:
    print('value error')

working_hour= int(input('please enter your working hours='))
print(working_hour)
if(working_hour>0 and working_hour<=40):
    salary1 = working_hour*200
    print(salary1)
elif(working_hour>40 and working_hour<168):
    salary2 = 8000 + (working_hour - 40) * 300
    print(salary2,)
else:
    print('value error')

working_hour= int(input('please enter your working hours='))
print(working_hour)
if(working_hour>0 and working_hour<=40):
    salary1 = working_hour*200
    print(salary1)
elif(working_hour>40 and working_hour<168):
    salary2 = 8000 + (working_hour - 40) * 300
    print(salary2,)
else:
    print('value error')

var_s = float(input('please enter the number='))
if(var_s<100):
    var_L1 =  3000-(125*(var_s**2))
    print(var_L1)
elif(var_s>=100):
    var_L2 = 12000 / (4+(var_s**2 / 14900))
    print(var_L2)
else:
    print('value error')

var_s = float(input('please enter the number='))
if(var_s<100):
    var_L1 =  3000-(125*(var_s**2))
    print(var_L1)
elif(var_s>=100):
    var_L2 = 12000 / (4+(var_s**2 / 14900))
    print(var_L2)
else:
    print('value error')

var_s = float(input('please enter the number='))
if(var_s<100):
    var_L1 =  3000-(125*(var_s**2))
    print(var_L1)
elif(var_s>=100):
    var_L2 = 12000 / (4+(var_s**2 / 14900))
    print(var_L2)
else:
    print('value error')

hour = int(input('please enter the time='))
if(hour>=0 and hour<24):
    if(hour>=4 and hour<=6):
        print('breakfast')
    elif(hour>=12 and hour<=13):
        print('lunch')
    elif(hour>=16 and hour<=17):
        print('snack')
    elif(hour>=19 and hour<=20):
        print('dinner')
    else:
        print('Patience is a virtue')
else:
    print('worng time')

hour = int(input('please enter the time='))
if(hour>=0 and hour<24):
    if(hour>=4 and hour<=6):
        print('breakfast')
    elif(hour>=12 and hour<=13):
        print('lunch')
    elif(hour>=16 and hour<=17):
        print('snack')
    elif(hour>=19 and hour<=20):
        print('dinner')
    else:
        print('Patience is a virtue')
else:
    print('worng time')

hour = int(input('please enter the time='))
if(hour>=0 and hour<24):
    if(hour>=4 and hour<=6):
        print('breakfast')
    elif(hour>=12 and hour<=13):
        print('lunch')
    elif(hour>=16 and hour<=17):
        print('snack')
    elif(hour>=19 and hour<=20):
        print('dinner')
    else:
        print('Patience is a virtue')
else:
    print('worng time')

hour = int(input('please enter the time='))
if(hour>=0 and hour<24):
    if(hour>=4 and hour<=6):
        print('breakfast')
    elif(hour>=12 and hour<=13):
        print('lunch')
    elif(hour>=16 and hour<=17):
        print('snack')
    elif(hour>=19 and hour<=20):
        print('dinner')
    else:
        print('Patience is a virtue')
else:
    print('worng time')


student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')

student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')

student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')

student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')

student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')

student_marks= int(input('please enter the marks='))
print(student_marks)
if(student_marks>=0 and student_marks<=100):
    if(student_marks<50):
        print('F')
    elif(student_marks>=50 and student_marks<=59):
        print('E')
    elif(student_marks>=60 and student_marks<=69):
        print('D')
    elif(student_marks>=70 and student_marks<=79):
        print('C')
    elif(student_marks>=80 and student_marks<=89):
        print('B')
    elif(student_marks>=90 and student_marks<=100):
        print('A')
else:
    print('invalid mark')


degrees_fahrenheit= int(input('please enter the temperature='))
degrees_celsius= ((degrees_fahrenheit) - 32) * 0.56
print(degrees_celsius)
if(degrees_celsius<20):
    print('winter')
elif(degrees_celsius>=20 and degrees_celsius<25):
    print('autumn')
elif(degrees_celsius>=25 and degrees_celsius<30):
    print('spring')
elif(degrees_celsius>30):
    print('summer')

degrees_fahrenheit= int(input('please enter the temperature='))
degrees_celsius= ((degrees_fahrenheit) - 32) * 0.56
print(degrees_celsius)
if(degrees_celsius<20):
    print('winter')
elif(degrees_celsius>=20 and degrees_celsius<25):
    print('autumn')
elif(degrees_celsius>=25 and degrees_celsius<30):
    print('spring')
elif(degrees_celsius>30):
    print('summer')

degrees_fahrenheit= int(input('please enter the temperature='))
degrees_celsius= ((degrees_fahrenheit) - 32) * 0.56
print(degrees_celsius)
if(degrees_celsius<20):
    print('winter')
elif(degrees_celsius>=20 and degrees_celsius<25):
    print('autumn')
elif(degrees_celsius>=25 and degrees_celsius<30):
    print('spring')
elif(degrees_celsius>30):
    print('summer')

degrees_fahrenheit= int(input('please enter the temperature='))
degrees_celsius= ((degrees_fahrenheit) - 32) * 0.56
print(degrees_celsius)
if(degrees_celsius<20):
    print('winter')
elif(degrees_celsius>=20 and degrees_celsius<25):
    print('autumn')
elif(degrees_celsius>=25 and degrees_celsius<30):
    print('spring')
elif(degrees_celsius>30):
    print('summer')


distance1 = int(input('enter the distance='))
distance= distance1/1000
time1 = int(input('enter the time='))
time= time1/3600
velocity= distance/time
print(velocity)
if(velocity<60):
    print('Too slow. Needs more changes.')
elif(velocity>=60 and velocity<=90):
    print('Velocity is okay. The car is ready!')
elif(velocity>90):
    print('Too fast. Only a few changes should suffice.')
else:
    print('problem')

distance1 = int(input('enter the distance='))
distance= distance1/1000
time1 = int(input('enter the time='))
time= time1/3600
velocity= distance/time
print(velocity)
if(velocity<60):
    print('Too slow. Needs more changes.')
elif(velocity>=60 and velocity<=90):
    print('Velocity is okay. The car is ready!')
elif(velocity>90):
    print('Too fast. Only a few changes should suffice.')
else:
    print('problem')


CGPA= float(input('please enter the CGPA='))
print(CGPA)
if(CGPA>=3.8 and CGPA<=3.89):
    print('waiver percentige is 25 percent')
elif(CGPA>=3.90 and CGPA<=3.94):
    print('waiver percentige is 50 percent')
elif(CGPA>=3.95 and CGPA<=3.99):
    print('waiver percentige is 75 percent')
elif(CGPA==4.00):
    print('waiver percentige is 75 percent')
elif(CGPA<3.89):
    print('The students is not eligible for a waiver')
else:
    print('not pass')


CGPA= float(input('please enter the CGPA='))
print(CGPA)
if(CGPA>=3.8 and CGPA<=3.89):
    print('waiver percentige is 25 percent')
elif(CGPA>=3.90 and CGPA<=3.94):
    print('waiver percentige is 50 percent')
elif(CGPA>=3.95 and CGPA<=3.99):
    print('waiver percentige is 75 percent')
elif(CGPA==4.00):
    print('waiver percentige is 75 percent')
elif(CGPA<3.89):
    print('The students is not eligible for a waiver')
else:
    print('not pass')


var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 or var_a%5==0):
    print('no')
else:
    print("it is a multiple of NEITHER 2 NOR 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 or var_a%5==0):
    print('no')
else:
    print("it is a multiple of NEITHER 2 NOR 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 or var_a%5==0):
    print('no')
else:
    print("it is a multiple of NEITHER 2 NOR 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 or var_a%5==0):
    print('no')
else:
    print("it is a multiple of NEITHER 2 NOR 5.")



var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 and var_a%5==0):
    print('it is multiple to both 2 and 5')
else:
    print("it is not a multiple of  2 OR  not a multiple of 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 and var_a%5==0):
    print('it is multiple to both 2 and 5')
else:
    print("it is not a multiple of  2 OR  not a multiple of 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 and var_a%5==0):
    print('it is multiple to both 2 and 5')
else:
    print("it is not a multiple of  2 OR  not a multiple of 5.")

var_a= int(input('please enter the number='))
print(var_a)
if(var_a%2==0 and var_a%5==0):
    print('it is multiple to both 2 and 5')
else:
    print("it is not a multiple of  2 OR  not a multiple of 5.")


canvas= int(input('total amount of canvas='))
print(canvas)
paint_tube= int(input('total amount of paint tube='))
print(paint_tube)
sum= (canvas*120)+(paint_tube*75)
if(sum>=0 and sum<=299):
    discount= sum - 0
    print(discount)
elif(sum>=300 and sum<=499):
   discount1= sum - 10
   print(discount1)
elif(sum>=500 and sum<=749):
    discount2= sum - 20
    print( discount2)
elif(sum>=750 and sum<=999):
    discount3= sum - 50
    print(discount3)
elif(sum>=1000):
    discount4= sum - 150
    print(discount4)
else:
    print('error')

canvas= int(input('total amount of canvas='))
print(canvas)
paint_tube= int(input('total amount of paint tube='))
print(paint_tube)
sum= (canvas*120)+(paint_tube*75)
if(sum>=0 and sum<=299):
    discount= sum - 0
    print(discount)
elif(sum>=300 and sum<=499):
   discount1= sum - 10
   print(discount1)
elif(sum>=500 and sum<=749):
    discount2= sum - 20
    print( discount2)
elif(sum>=750 and sum<=999):
    discount3= sum - 50
    print(discount3)
elif(sum>=1000):
    discount4= sum - 150
    print(discount4)
else:
    print('error')


