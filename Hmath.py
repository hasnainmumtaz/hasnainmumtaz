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
def divide(number, divisor):
    try:
        # Check if the divisor is zero
        if divisor == 0:
            # Handle the case of division by zero and print "Infinity"
            return print("Infinity")
        else:
            # Check if the type of the input number is either int or float
            if type(number) == (type(1) or type(1.1)):
                # If so, perform division and return the result
                return number / divisor
            else:
                # If the type is not int or float, create a list to store results for each element in the input number
                numlist = []
                for i in number:
                    # Divide each element by the divisor and append the result to the list
                    numlist.append(i / divisor)
                # Return the list of results
                return numlist
    except ValueError:
        # Handle the case where an exception occurs (e.g., non-numeric input)
        print("Enter a numeric value!")

## Mean
def mean(lst):
    try:
        # Get the length of the list
        length = len(lst)
        # Initialize a variable to store the sum of the elements in the list
        total = 0
        # Iterate through each element in the list and add it to the total
        for i in lst:
            total += i
        # Calculate and return the mean by dividing the total by the length
        return total / length
    except ValueError:
        # Handle the case where an exception occurs (e.g., non-numeric elements in the list)
        print("The provided list isn't numeric")

## Sum all
def sumall(lst):
    try:
        # Check if all elements in the list are either int or float
        for i in lst:
            if type(i) not in (int, float):
                return print("The provided list isn't numeric")
        
        # If all elements are numeric, initialize a variable to store the sum of the elements in the list
        total = 0
        # Iterate through each element in the list and add it to the total
        for i in lst:
            total += i
        
        # Return the total sum
        return total
        
    except ValueError:
        # Handle the case where an exception occurs (e.g., non-numeric elements in the list)
        print("The provided list isn't numeric")
