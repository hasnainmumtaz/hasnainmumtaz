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

