#Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.


def right_justify(s):
    r = " "*70
    print r+s
n = right_justify('alen')
