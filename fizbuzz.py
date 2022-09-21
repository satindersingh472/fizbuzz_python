def divide_number(number):
    if(number % 3 == 0 and number % 5 == 0):
        print('FizzBuzz')
    elif(number % 5 == 0):
        print('Buzz')
    elif(number % 3 == 0):
        print('Fizz')

def pick_number(array):
    for number in array:
        divide_number(number)

number_array = [15,30,45,60,75,3,6,9,12,18,5,10,20,25,35]
pick_number(number_array)
