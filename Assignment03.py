def is_right_triangle(side1,side2,side3):
    sides=sorted([side1,side2,side3])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
a,b,c = 3,4,5
if is_right_triangle(a,b,c):
    print(f"sides{a},{b},{c} for a right angled triangle")
else:
    print(f"sides{a},{b},{c} for not a right angled triangle")
x,y,z=5,5,5
if is_right_triangle(x,y,z):
    print(f"sides{x},{y},{z} for a right angled triangle")
else:
    print(f"sides{x},{y},{z} for not a right angled triangle")