def fizz_buzz(input):
    x=int(input%3)
    y=int(input%5)
    print(x)
    print(y)
    if input==3:
        return 'Fizz'
    elif input ==5:
        return 'Buzz'
    elif input ==0:
        return 0
    elif x+y==0:
        return "FizzBuzz"
    elif x<y:       #The smaller a number is the smaller the remainder
        if x==0:
            return 'Fizz'
        else:
            return input
    elif x>y:
        return 'Buzz'
    else:
        return input

print(fizz_buzz(30))



