import sys

sys.path.insert(1, "D:\CompetitiveProg\Week-01\Day01\SumTwoNumbers")
sys.path.insert(1, "D:\CompetitiveProg\Week-01\Day02")
import DivideTwoNumbers
import MultiplyTwoNumbers
import SumTwoNumber


def calculator():
    operator_choice = input("Press 1 for summation and subtraction, \n"
                            "Press 2 for multiplication, \n"
                            "Press 3 for division: ")
    if operator_choice == "1":
        SumTwoNumber.main()
    elif operator_choice == "2":
        MultiplyTwoNumbers.main()
    elif operator_choice == "3":
        DivideTwoNumbers.main()
    else:
        print("Wrong Choice! Exiting...")


calculator()
