# Title: vanhessche_myworld.py
# Author:  John Vanhessche
# Date:  5 November 2022
# Description:  First python file, per Exercise 3.2

# Variables

add1 = 4
add2 = 4
sub1 = 10
sub2 = 6
div1 = 8
div2 = 2
mul1 = 10
mul2 = 2

# Functions

def add (a1, a2):
    return int(a1 + a2)

def subtract (s1, s2):
    return int(s1 - s2)

def divide (d1, d2):
    return float(d1/d2)
    
def multiply (m1, m2):
    return int(m1 * m2)

# Main Program
def main():
    results = str(add1) + " + " + str(add2) + " is " + str(add(add1, add2)) + "." + "\n" + str(sub1) + " - " + str(sub2) + " is " + str(subtract(sub1, sub2)) + "." + "\n" + str(div1) + " / " + str(div2) + " is " + str(divide(div1, div2)) + "." + "\n" + str(mul1) + " * " + str(mul2) + " is " + str(multiply(mul1, mul2)) + "." + "\n"  
    print(results)  

main()
