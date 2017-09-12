mylist = ["ABS12", 2,3,"DEF", "###"]
new_list = [str(val) for val in mylist]#LIST COMPREHENSION
#the element is .. and type is
print new_list
for val in new_list:
    if val.isalpha():
        print "{0} is the Data and the the type is {1}".format(val, "ALPHA")
    elif val.isdigit():
        print "{0} is the Data and the the type is {1}".format(val, "DIGIT")
    elif val.isalnum():
        print "{0} is the Data and the the type is {1}".format(val,"ALPHA NUMERIC")
    else:
        print "Unexpected characters encountered..The charactes are {}".format(val)