# This loop will allow the inner if and else statements to keep iterating untill the appropriate condition is met.
while True:
# Allows the user to input a value and stores it in the variable user_input
        user_input = input('Enter input string: \n')
# Checks to see if the user inputted value is not equal to q and allows the program to iterate to the next sequence unless True.
        if user_input != 'q':
# Replaces the specific values of the user_input variable with the specified value.
            user_input = user_input.replace(' ', '')
# Checks to see if a comma was used in the user input and if that condition was met, splits the user inputed values at there comma.
# It also prints the user inputed values at position 0 and 1. If the condition is not met then informs the user of a syntax format error.
            if ',' in user_input:
                user_input = user_input.split(',')
                print ('First word: ' + user_input[0])
                print ('Second word: ' + user_input[1])
                print("")
                print("")
            else:
                print('Error: No comma in string.')
# Allows the program to stop if the users input equals True
        else:
          break
