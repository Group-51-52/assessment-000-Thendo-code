
# #Question 1
def get_date_of_birth(id_number:str): 
        """
        STEP 2: Extract the date of birth from the ID number and return it as a string

        return format: DD/MM/YY: 
        """
        birth_of_date = f"{id_number[4:6]}/{id_number[2:4]}/{id_number[0:2]}"
        return birth_of_date

print(get_date_of_birth("0207300680018"))
# #Question 2    
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
       
    if int(id_number[6]) > 4:
     return 'Male'
    else:
     return 'Female'

    
# #Question 3
def get_citizenship(id_number):
      """
      STEP 4: Extract the citizenship from the ID number using the formula below and 
      return it as a string

      Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
      a South African citizen and if it is greater than 01, the person is a non-South 
      African citizen.
      """
      if int(id_number[10]) == 0:
       return 'South African'
      else:
       return 'Non-South African'


# #Question 4

"""
    Fizzbuzz is a programme that prints the numbers from 1 to n, 
    but for multiples of 3, it prints "Fizz" instead of the number, 
    and for multiples of 5, it prints "Buzz" instead of the number. 
    For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
    """
def fizzbuzz(n):
       
        for i in range(1,n+1):
                    if n<0:
                           return "" 
                    elif n%3==0 and n%5==0:
                        print(" FizzBuzz")
                    elif n%5==0:
                            print( "Buzz")
                    elif n%3==0:
                            print( "Fizz")
                    else: print (i)

    
print(fizzbuzz(6))
            

#Question 5
def check_number(n:int):
    """    
    TODO: Using TDD(Test Driven Development), Implement tests for the below functionality. 
    Create a test file called `test_my_tests.py` in the root directory.
    Create a test class called 'MyTestCases' and it should have the following test implementations:
        test_check_number_odd_number: Tests for positive odd numbers.
        test_check_number_even_range_2_to_5: Tests for even numbers in the range 2 to 5, ensuring it returns "Not Weird".
        test_check_number_even_range_6_to_20: Tests for even numbers in the range 6 to 20, ensuring it returns "Weird".
        test_check_number_even_greater_than_20: Tests for even numbers greater than 20, ensuring it returns "Not Weird".
        test_check_number_negative_even_number: Tests for non-positive even numbers.
        test_check_number_negative_odd_number: Tests for non-positive odd numbers.
        test_check_number_neutral`: Tests for numbers that are neutral.


#     TODO: Given an integer n, perform the following conditions actions:
#     non-positive and non-negative digit(s) are 'Neutral'
#     If n is odd, return 'Weird'
#     If n is even and in the inclusive range of 2  to 5 , return 'Not Weird'
#     If n is even and in the inclusive range of 6  to 20 , return 'Weird'
#     If n is even and greater than 20 , return 'Not Weird'
#     If n is non-positive and even then return 'Very weird'
#     If n is non-positive and odd then return 'Extremely Weird'
#     """
    if n<0 : #     If n is non-positive and even then return 'Very weird'
        if n%2==0:
          return 'Very weird'
        else:#     If n is non-positive and odd then return 'Extremely Weird'
            return 'Extremely Weird'
    if n==0:#     If n is odd, return 'Weird'
          return "Weird"
    elif n%2!=0:#     If n is even and in the inclusive range of 2  to 5 , return 'Not Weird'
          return "Weird"
    elif n%2==0 and n in  range(2,5+1):#     If n is even and in the inclusive range of 6  to 20 , return 'Weird'
          return "Not Weird"
    elif n%2==0 and n in range(6,21):#     If n is even and in the inclusive range of 6  to 20 , return 'Weird'
          return "Weird"
    elif n%2==0 and n>21:#     If n is even and greater than 20 , return 'Not Weird'
          return  'Not Weird'
