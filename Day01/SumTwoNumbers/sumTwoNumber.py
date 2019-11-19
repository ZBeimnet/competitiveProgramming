# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:00:12 2019

@author: Beimnet.Z
"""
#Global Variables
number1 = [9, 1, 3, 1, 1, 1, 1, 1, 1, 1]
number2 = [1, 1, 2, 3, 4, 5, 5, 5, 5, 5]
number1Length = len(number1)
number2Length = len(number2)
length = 0
difference = 0
carry = 0
result = []

def checkNumLength():
    global number1
    global number2
    global length
    
    if(number1Length > number2Length):
        length = number1Length
        difference = number1Length - number2Length
        number1, number2 = makeNumLengthEqual(difference, number2), number1
    elif(number1Length == number2Length):
        length = number1Length
    else:
        length = number2Length
        difference = number2Length - number1Length
        number2, number1 = makeNumLengthEqual(difference, number1), number2

def makeNumLengthEqual(difference, number):
    num = number
    for i in range(difference):
        num.insert(0, 0)
        
    return num
        
def sumIndexes():
    global result
    
    for numIndex in range(length-1, -1, -1):
        indexSum = number1[numIndex] + number2[numIndex] + carry
        result.insert(0, checkSum(numIndex, indexSum))

def checkSum(numIndex, indexSum):
    global carry
    
    strSum = str(indexSum)
    sumLength = len(strSum)
    if(sumLength > 1 and numIndex != 0):
        carry = int(strSum[0])
        return int(strSum[1])
    else:
        carry = 0
        return indexSum

def convertListToString(numberList):
    numberString = ""
    
    for number in numberList:
        numberString += str(number)
        
    return numberString

def main():    
    checkNumLength()
    sumIndexes()
    print(convertListToString(result))
    
main()
    

