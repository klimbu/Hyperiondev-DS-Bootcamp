def print_values_of(dictionary, keys):
    # got rid of for key in keys:
    print(dictionary[keys]) #kept the print functions changing k to keys

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!", "maggie": " (Pacifier Suck)"}
# Line 5 d'oh - change the '' to "" and add exclamation mark !

print_values_of(simpson_catch_phrases, 'lisa')
print_values_of(simpson_catch_phrases, 'bart')
print_values_of(simpson_catch_phrases, 'homer')

# First Error was that it would only takes 2 positional arguments
# More Error - name 'k' is not defined
    # changed k to keys
# More error - 'dict' object is not callable
    # removed the for loop
# Used print_values_of 3 times to get the desired output below
'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

