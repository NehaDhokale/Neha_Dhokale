a= int (input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

if a>=b and b>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest=c
print("Largest number is:",largest)
