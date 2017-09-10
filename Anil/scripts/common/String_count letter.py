'''
Program to count no of  any letter  in the string any in string
'''


word=raw_input("Enter the  any String:").lower()
letter_count=raw_input("Enter the count letter : ")
count=0
for letter in word:
    if  letter == letter_count:
        count=count+1
print count
