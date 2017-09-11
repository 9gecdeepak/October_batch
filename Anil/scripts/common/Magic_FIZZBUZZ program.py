'''
write a program that prints the number from start to end range. But for multiples of three print "Fizz"
instead of the number and for the multiples five print "Buzz".
For numbers which are multiple of both three and five print "FizzBuzz".
'''
a=input("Enter the start number:")
b=input("Enter the end number:")
for  i in range(a,b):
    if (i%3==0 and i%5==0):
        print  "the value is {} and name is {}".format(i, "FIZZBUZZ")
    elif i%3==0:
        print "the value is {} and name is {}".format(i,"FIZZ")
    elif i%5==0:
        print  "the value is {} and name is {}".format(i,"BUZZ")
    else:
        print  "the value is {} and name is {}".format(i, "NO-NUMBER")
