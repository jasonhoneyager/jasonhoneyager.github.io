def counter():
    x = 0
    print (x)
    while x < 100:
        x = x + 1
        if x % 3 == 0 and x % 5 == 0:
            print ("FizzBuzz")
            continue
        if x % 5 == 0:
            print ("Buzz")
            continue
        if x % 3 == 0:
            print ("Fizz")
            continue
        print (x)
counter()