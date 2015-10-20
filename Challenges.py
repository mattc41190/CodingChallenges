__author__ = 'mattc_000'
import string




def reverseString(strng):
    print "Challnege One\nPrint "+strng+" backwards"
    length =  len(strng)
    counter =  length - 1
    newString = ''
    for i in strng:
        newString += strng[counter]
        counter = counter - 1
    print newString

# reverseString("Hi Matt")


def factorialPresenter(number):
    print "Challnege Two\nPrint factorial for "+str(number)+""
    number = number + 1
    total = 0
    for i in range(number):
        if total == 0:
            total = i
            continue
        total = total * i
    print total

# factorialPresenter(4)

def longestWord(sentence):
    print "Challnege Three\nPrint longest word in sentence:\n"+sentence+""
    longestWord = ""
    words = sentence.split(" ")
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    print longestWord


# longestWord("I am a monkey from the jungles of Africa")

def letterChanges(strng):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newAlphabet = ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    vowels = ["a","e","i","o","u"]
    newStrng = ""
    for i in strng:
        if i == " ":
            newStrng += i
            continue
        if i == "z":
            i = "a"
            newStrng += i
            continue
        i = string.lowercase.index(i) + 1
        newStrng += alphabet[i]
    for i in range(0, len(newStrng)):
        if newStrng[i] in vowels:
            newStrng[i].replace(newStrng[i],newStrng[i].upper())
    print(newStrng)


letterChanges("hello ziggy marley you cool guy")