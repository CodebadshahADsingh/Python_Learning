#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      AMANDEEP SINGH
#
# Created:     03-03-2022
# Copyright:   (c) AMANDEEP SINGH 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first=int(input("enter 1st no. : "))
second=int(input("enter 2nd no. : "))
choose=input("chose the operator among the following (+,-,*,/)")

if choose == "+":
    print(first + second)
elif choose == "-":
    print(first - second)
elif choose == "*":
    print(first * second)
elif choose == "/":
    print(first / second)