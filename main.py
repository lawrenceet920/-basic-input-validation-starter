# Braden Leach & Ethan Lawrence
# dec 10 2024
# Validating String Input (Tiered Assignment)

# Are you and your partner working on Level 1, Level 2 or Level 3 today?
# Working on Level...

while True: # repeat code
    # Input
    userinput = input('Please enter a 6-10 digit number:        ')

    # Process
    if userinput.isdigit():
        if  5 < len(userinput) < 11:
            output = f'Valid input: {userinput}'
            break
        else:
            output = 'Input must be between 6 and 10 characters long.'
    else:
        output = 'Input must be numeric'

    # Output
    print(output)