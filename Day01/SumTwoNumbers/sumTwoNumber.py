# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:00:12 2019

@author: Beimnet.Z
"""

#Global Variable
carry = 0

def calculateSum(firstNumber, secondNumber):
    global carry
    firstNumberLength = len(firstNumber)
    secondNumberLength = len(secondNumber)
    length = 0
    result = ""

    if(firstNumberLength > secondNumberLength):
        length = firstNumberLength
        difference = firstNumberLength - secondNumberLength
        secondNumber = makeNumberLengthEqual(difference, secondNumber)
    elif(firstNumberLength == secondNumberLength):
        length = firstNumberLength
    else:
        length = secondNumberLength
        difference = secondNumberLength - firstNumberLength
        firstNumber = makeNumberLengthEqual(difference, firstNumber)

    for index in range(length-1, -1, -1):
        sumAtIndex = int(firstNumber[index]) + int(secondNumber[index]) + carry
        result = str(checkSumAtIndex(index, sumAtIndex)) + result

    return result

def makeNumberLengthEqual(difference, number):
    return "0"*difference + number
        
def checkSumAtIndex(index, sumAtIndex):
    global carry

    if(sumAtIndex > 9 and index != 0):
        carry = sumAtIndex // 10
        return sumAtIndex % 10
    else:
        carry = 0
        return sumAtIndex

def main():    
    num1 = input("Enter Num1: ")
    num2 = input("Enter Num2: ")
    result = calculateSum(num1, num2)
    print("Result: " + result)
    
main()
    

