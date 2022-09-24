def divide_number(number):
    if(number % 3 == 0 and number % 5 == 0):
        print('FizzBuzz')
    elif(number % 5 == 0):
        print('Buzz')
    elif(number % 3 == 0):
        print('Fizz')

number_array = [3,5,15,30,45,60,75,3,6,9,12,18,5,10,20,25,35]
for number in number_array:
    divide_number(number)