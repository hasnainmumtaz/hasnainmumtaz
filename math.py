## Test lists
evennums = [2,4,6,8,10]
oddnums = [1,3,5,7,9]
nums = [0,1,2,3,4,5,6,7,8,9]

## Power
def power(number, power):
    try:
        # Check if the length of the input number is 1
        if type(number) == (type(1) or type(1.1)) :
            # If so, raise the number to the specified power and return the result
            return number ** power
        else:
            # If the length is not 1, create a list to store results for each element in the range of the input number
            numlist = []
            for i in range(len(number)):
                # Raise each element to the specified power and append the result to the list
                numlist.append(number[i] ** power)
            # Return the list of results
            return numlist
    except:
        # Handle the case where an exception occurs (e.g., non-numeric input)
        print("Enter a numeric value!")

## Multiply
def multiply(number, times):
    try:
        # Check if the type of the input number is either int or float
        if type(number) == (type(1) or type(1.1)):
            # If so, multiply the number by the specified times and return the result
            return number * times
        else:
            # If the type is not int or float, create a list to store results for each element in the range of the input number
            numlist = []
            for i in range(len(number)):
                # Multiply each element by the specified times and append the result to the list
                numlist.append(number[i] * times)
            # Return the list of results
            return numlist
    except:
        # Handle the case where an exception occurs (e.g., non-numeric input)
        print("Enter a numeric value!")

## Division
def division(number, divisor):
    try:
        # Check if the divisor is not equal to zero
        if divisor != 0:
            # Use the multiply function to divide the number by the divisor
            # by multiplying the number with the reciprocal of the divisor (divisor raised to the power of -1)
            return multiply(number, power(divisor, -1))
        else:
            # Handle the case where the divisor is zero and print an error message
            return print("Cannot Divide by Zero!")
    except:
        # Handle the case where an exception occurs (e.g., non-numeric input)
        print("Enter a numeric value!")