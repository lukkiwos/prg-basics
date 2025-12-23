###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x =", x, "y =", y)

# swap the values
z = x
x = y
y = z
print("After swapping: x =", x, "y =", y)



def f(p, l):
    r = 0
    
    r = p
    p = l
    l = r
    return p, l


if __name__ == "__main__":
    print(f"After swapping: {f(6, 9)}")
