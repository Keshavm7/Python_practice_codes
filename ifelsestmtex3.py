# write a pythpn program which will accept any word and check whether it is palindrome or not
word=input("Write any word: ")
if(word==word[::-1]):
    print("{} is Palindrome".format(word))
else:
    print("{} is not Palindrome".format(word))
    