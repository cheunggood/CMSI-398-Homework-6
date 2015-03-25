promt_for_input = True
while promt_for_input:
    try:
        num_int = int(input("Please enter a number of inches: "))
    except ValueError:
        print("\nThat is not a number!\n")
    else:
        print("Number accepted.\n")
        promt_for_input = False

a = num_int//36
b = (num_int%36)//12
c = (num_int%36)%12
print("%d inches are equivalent to %d yard, %d foot, and %d inch."%(num_int,a,b,c))
