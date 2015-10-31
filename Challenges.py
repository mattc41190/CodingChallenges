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
    print "Challenge Nine\nArrange " + strng + " alphabetically"
    originalWordArray = []
    for i in strng:
        originalWordArray.append(i)
    sortedArray = sorted(originalWordArray)
    newWord = "".join(sortedArray)
    print newWord

# alphabeticalOrderOrganizer("werunthenight")

def ABCheck(strng):
    print "Challenge Ten\nValidate that selected letter A or B in " + strng + " is separated by 3 letters to another A or B"
    winner = False
    for i in range(len(strng)):
        if len(strng) > i + 3:
            if strng[i] == "a" or strng[i] == "b":
                if strng[i + 3] == "a" or strng[i + 3] == "b":
                    winner = True
                    break
                else:
                    winner = False
    if winner == True:
        print "True"
    else:
        print "False"

# ABCheck("Laura sobs")

def VowleCheck(strng):
    print "Challenge Eleven\nReturn count of all vowles in " + strng
    vowels = ['a','e','i','o','u']
    vowelCount = 0
    for i in strng:
        i = i.lower()
        if i in vowels:
            vowelCount += 1
    print vowelCount

# VowleCheck("All cows eat grass")


def wordCounter(sentence):
    print "Challenge Eleven\nReturn count of all words in: " + sentence
    spaces = 0
    for i in sentence:
        if i == " ":
            spaces += 1
    print spaces

# wordCounter("All cows eat grass")

def ExOh(strng):
    strng =  strng.lower()
    print "Challenge Twelve\nCheck to see if there are an equal amount of Xs and Os in: " + strng
    Xs = []
    Os = []
    for i in strng:
        if i == "x":
            Xs.append(i)
        elif i == "o":
            Os.append(i)
    if len(Xs) == len(Os):
        print "Equal"
    else:
        print "Not Equal"

# ExOh("xxXOxooxoo")

def Palindrome(strng):
    print "Challenge Thirteen\nCheck to see if the following word is a palindrome: " + strng

    strng =  strng.lower()
    backward = ""
    count = len(strng) - 1
    for i in range(len(strng)):
        backward += strng[count]
        count -= 1
    if backward ==  strng:
        print "Yes " + strng + " is a palindrome"
    else:
        print "No " + strng + " is NOT a palindrome"

# Palindrome("Mom")

ArithArray = [2,4,6,8]
def ArithGeo(arr):
    print "Challenge Fourteen\nCheck to see if a collection follows math rules"
    isArthimetic = True
    isGeometric = True
    arthimeticMeasure = arr[1] - arr[0]
    geometricMeasure = arr[1] / arr[0]
    for i in range(len(arr) -1):
        if arr[i +1] - arr[i] == arthimeticMeasure:
            isArthimetic = True
            print str(arr[i + 1]) + " is " + str(arthimeticMeasure) + " away from " + str(arr[i])
        else:
            isArthimetic = False
            break
    for i in range(len(arr) - 1):
        if arr[i +1] / arr[i] == geometricMeasure:
            isGeometric = True
            print str(arr[i + 1]) + " is " + str(geometricMeasure) + " away from " + str(arr[i])
        else:
            isGeometric = False
            break
    if isArthimetic == True:
        print "Collection Is Arithmetic!"
    elif isGeometric == True:
        print "Collection Is Geometric"
    elif isArthimetic == True and isGeometric == True:
        print "Collection Is Geometric And Arithmetic"
    else:
        "Collection Is Neither Arithmetic Nor Geometric"
# ArithGeo(ArithArray)

arrayForAddition = [26,25,50]
def arrayAdditionOne(arr):
    largest = 0

    for i in arr:
        if i > largest:
            largest = i
    arr.remove(largest)
    def oneAtATime(Narr):
        sum = 0
        for i in Narr:
            sum += i
            if sum > largest:
                print("That is too big")
                first = Narr[0]
                Narr.append(first)
                Narr.pop(0)
                print(Narr)
                oneAtATime(Narr)
                return True
            elif sum == largest:
                print "Great " + str(sum)
                return True
            else:
                print "too small " + str(sum)
                continue

    oneAtATime(arr)

arrayAdditionOne(arrayForAddition)