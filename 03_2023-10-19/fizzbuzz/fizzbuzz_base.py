max_count=10
for i in [x+1 for x in range(max_count)]:
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)