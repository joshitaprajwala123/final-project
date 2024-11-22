#BMI calculator
height=float(input("enter your height in cm: "))
weight=float(input('enter your weight in kg: '))

height=height/100
BMI=weight/(height*height)
print("your Body Mass Index is: ",BMI)

if BMI>0:
    if BMI<=16:
        print("you are severely underweight")

    elif BMI>16 and BMI<=18.5:
        print("you are underweight")

    elif(BMI<=25):
        print("you are Healthy")

    elif(BMI<=30):
        print("you are overweight")

    else:
        print("you are severely overweight")


