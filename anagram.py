# ascii = american standard code for information interchange
str1 = input("enter the first string ")
str2 = input("enter the second string ")

if(sorted(str1)==sorted(str2)):
    print("there are anagrams")
else:
    print("these are not anagrams")