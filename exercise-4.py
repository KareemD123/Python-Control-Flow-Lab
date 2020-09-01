# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Please enter the three lengths of a triangle")
length1 = input("length a: ")
length2 = input("length b: ")
length3 = input("length c: ")

if length1 == length2 and length2 == length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is an equilateral triangle")
elif length1 != length2 and length1 != length3 and length2 != length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is a scalene triangle")
elif length1 == length2 or length2 == length3 or length1 == length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is an isosceles triangle")
