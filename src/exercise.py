def main():
    #write your code below this line
    sum_of_nums = 0
    count = 0
    evens = 0
    odds = 0

    while True:
        number = int(input("Give numbers:"))

        if number == -1:
            break

        sum_of_nums += number
        count += 1

        if number % 2 == 0:
            evens += 1
        else:
            odds += 1

    
    print("Thx! Bye!")
    print("Sum: " + str(sum_of_nums))
    print("Numbers: " + str(count))
    print("Average: " + str(sum_of_nums/count))
    print("Even: " + str(evens))
    print("Odd: " + str(odds))

if __name__ == '__main__':
    main()
