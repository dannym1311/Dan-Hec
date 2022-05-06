
from re import I


def roman2int (romanstr:str):
    romans = 0
    for i in range(0,len(romanstr)):
        if romanstr[i] == "I":
            if i + 1 < len(romanstr):
                if romanstr[i + 1] == "V" or romanstr[i + 1] == "X":
                    romans -= 1
                else:
                    romans += 1
            else:
                romans += 1
        if romanstr[i] == "V":
            romans += 5
        if romanstr[i] == "X":
            if i + 1 < len(romanstr):
                if romanstr[i + 1] == "L" or romanstr[i + 1] == "C":
                    romans -= 10
                else:
                    romans += 10
            else:
                romans += 10
        if romanstr[i] == "L":
            romans += 50
        if romanstr[i] == "C":
            if i + 1 < len(romanstr):
                if romanstr[i + 1] == "D" or romanstr[i + 1] == "M":
                    romans -= 100
                else:
                    romans += 100
            else:
                romans += 100
        if romanstr[i] == "D":
            romans += 500
        if romanstr[i] == "M":
            romans += 1000
    return romans

print(roman2int("MCMXCIV"))











