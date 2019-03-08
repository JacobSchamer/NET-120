#BMI Calculator in Python!
Name = "Guy"
Heightft = 6
Heightin = 4
Weight = 280
ProperBMI = 25.00
ActualHeight = (Heightft * 12) + Heightin
BMI = (Weight * 703) / (ActualHeight * ActualHeight)
print(Name, BMI)
if BMI < ProperBMI: print(Name, "is underweight")
elif BMI == ProperBMI: print("Your doing great!")
else: print(Name, "is overweight")
import webbrowser
new=2;
url="http://www.everydayhealth.com/fitness/";
webbrowser.open(url,new=new);

