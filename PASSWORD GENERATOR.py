#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      AMANDEEP SINGH
#
# Created:     09-03-2022
# Copyright:   (c) AMANDEEP SINGH 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
LOWER_CHARACTERS="abcdefghijklmnopqrstuvwxyz"
UPPER_CHARACTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS="1234567890"
SYMBOLS="~!@#$%^&*()_+:><"

a = LOWER_CHARACTERS+UPPER_CHARACTERS+SYMBOLS+NUMBERS
LEN= 8
password = "".join(random.sample(a,LEN))
print("the password generated is :", password)
