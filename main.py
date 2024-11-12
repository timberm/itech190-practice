def main():
    print("hello world")

    answer = True

    if answer:
        print("this is true")
    else:
        print("this is false")


    trees = 10
    leaves = trees * 2

    print("The amount of trees is {} and the amount of leaves is {}".format(trees, leaves))
    print()

    cars = 5
    people = 10 
    print(f"The amount of people in each car is {people / cars}") #division of an integer always ends as a float

    print("Cars>>>People") #shift, alt, down @ end of line to copy n paste
    print(f"Cars plus people is: {cars + people}")
    print(f"Cars minus people is: {cars - people}")
    print(f"Cars times people is: {cars * people}")
    print(f"Cars divided by people is: {cars / people}") #5/10 = 0.5 >float
    print(f"Cars integer divided people is: {cars // people}") #5//10 = 0.5
    print(f"Cars modulo people is: {cars % people}") #5%10 = 5?
    print()
    print("People>>Cars")
    print(f"People plus cars is: {people + cars}")
    print(f"People minus cars is: {people - cars}")
    print(f"People times cars is: {people * cars}")
    print(f"People divided by cars is: {people / cars}") #10/5 = 2.0 >float
    print(f"People integer divided by cars is: {people // cars}") #10//5 = 2
    print(f"People modulo cars is: {people % cars}") #10%5 = 0?
    print()

    a = 5 #int
    b = 5.0 #float
    c = True #bool
    d = None #NoneType

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    

if __name__ == "__main__":
    main()