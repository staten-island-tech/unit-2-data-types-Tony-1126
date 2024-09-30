""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" x = input("type something") """

""" use the print function in order to put the amount of words. Use the len function to count the amount of words and input to tell the commenter to write something """

""" print(len(input("Write Something:").split())) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" x = int(input("Enter A Number"))
if x % 2 == 0:
    print("Even")
else:
    print("Odd") """
""" word_values = {
    "Bad": 0.0,
    "Mediocore": 0.15,
    "Great": 0.20,
    "Excellent": 0.25
}
x = int(float(input("Enter Your Bill:")))
y = float(input("How was your service, Excellent, Great, Mediocore, Bad:"))
print(Bill*y)

word_values = {
    "Bad": 0.0,
    "Mediocore": 0.15,
    "Great": 0.20,
    "Excellent": 0.25
} """   
""" bill = (input("Enter Your Bill:"))
x = float(bill)

tip = input("How Much Would You Like To tip? 0, 15, 20 , 25 Percent?:")

tip0 = x*0
tip15 = x*.15
tip20 = x*.20
tip25 = x*.25

if tip == "0":
    print(f"You little cheapskate only tipping, ${tip0}")
if tip == "15":
    print(f"Could've tipped more than, ${tip15}")
if tip == "20":
    print(f"Thanks for the tip of, ${tip20}")
if tip == "20":
    print(f"Wow!, TYSM for the tip of, ${tip25}")
 """
""" a = int(input("Enter an integer:"))
for i in range(2,a):
    if a%i == 0:
        print(f"Factors,:{i}") """

a = int(input("Enter an integer"))
b = int(input("Enter an integer"))
for i in range(2,a+1):
    if a%i == 0 and b%i == 0:
        gcf = i
        print(f"Factors of {a} and {b} is {gcf}")

       
    





   




    