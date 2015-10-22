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
    print "Challnege Four\nShift letters forward and capitalize vowels in following string:\n"+strng+""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
            newStrng = newStrng.replace(newStrng[i],newStrng[i].upper())
    print(newStrng)

# letterChanges("hello ziggy marley you are such cool guy")

def numberAdder(num):
    print "Challnege Five\nAdd all numbers leading up to: "+str(num)+""
    total = 0
    for i in range(num):
        total += i
    print total

# numberAdder(10)


def firstLetterCapitalizer(strng):
    print "Challnege Five\nCapitalize first letter in following string:\n "+strng+""
    newString = ""
    for i in range(len(strng)):
        if i == 0:
            newString += strng[i].upper()
            continue
        elif strng[i-1] == " ":
            newString += strng[i].upper()
            continue
        newString += strng[i]
    print(newString)

# firstLetterCapitalizer("a lowercase sentence is bad news bears")

def simpleSymbols(strng):
    print "Challnege Six\nAll letters in passed String: "+strng+" must be delmited by '+' or '=' signs"
    preAndPostCharacters = ["+","="]
    for i in range(len(strng)):
        if strng[i] in preAndPostCharacters:
            continue
        elif strng[i + 1] not in preAndPostCharacters or strng[i - 1] not in preAndPostCharacters:
            assert False, "Function expects a valid sentence you entered: " + strng
        else:
            assert True, "Yay!!"

# simpleSymbols("+++=f+f+=r+b+")
# simpleSymbols("+++=ff+f+=r+b+")

def numberComparator(num1,num2):
    print "Challnege Seven\nValidate that "+ str(num2) +" is greater than " + str(num1)
    if num2 > num1:
        return True
    elif num1 == num2:
        return "-1"
    else:
        return False

# numberComparator(5,7)

def timeConversion(num):
    print "Challnege Eight\nconvert " + str(num) + " into hours and minutes."
    count = 0
    if num >= 60:
        counting = True
        while counting is not False:
            if num % 60 == 0:
                num /= 60
                counting = False
            else:
                num -= 1
                count += 1
        print str(num) + ":" + str(count)
    else:
        print "0:" + str(num)

# timeConversion(145)

def alphabeticalOrderOrganizer(strng):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    reorderedWord = []
    for i in strng:
        alphabeticalIndex = alphabet.index(i)
        for j in strng:
            if alphabeticalIndex > alphabet.index(j):
                reorderedWord.append(i)
    print(reorderedWord)



alphabeticalOrderOrganizer("hello")