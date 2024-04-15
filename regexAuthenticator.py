import re

def regex_automator():
    # Ask user to input a regular expression
    regex_input = input("Enter the regular expression: ")
    
    try:
        # Compile the regular expression
        regex = re.compile(regex_input)
    except re.error as e:
        print("Invalid regular expression:", e)
        return
    
    # Main loop to test strings against the regular expression
    while True:
        test_string = input("Enter a string to test (press Enter to exit): ")
        
        # Check if user wants to exit
        if not test_string:
            break
        
        # Test the string against the regular expression
        if regex.match(test_string):
            print("Match found!")
        else:
            print("No match found.")

# Call the function to start the program
regex_automator()
