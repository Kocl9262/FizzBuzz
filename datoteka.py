# -*- coding: utf-8 -*-

fb = "blabla"

while fb != "ne":
    fb = raw_input("Želiš igrati FizzBuzz? (da/ne)")
    if fb == "da":

        z = int(raw_input("Vpiši število od 1 do 100"))

        if z <= 100 and z >= 1:
            for x in xrange(1, z + 1):
                if x % 3 == 0 and x % 5 == 0:
                    print("FizzBuzz")
                elif x % 3 == 0:
                    print("Fizz")
                elif x % 5 == 0:
                    print("Buzz")
                else:
                    print(x)

        else:
            print("Veljavne so samo cifre od 1 do 100")
            print("Poskusi znova")

    elif fb == "ne":
        print("Srečno!")

    else:
        print("Vpiši, da ali ne")
