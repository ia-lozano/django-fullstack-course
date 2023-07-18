import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other'

for p in patterns:
    print("I'm searching for: ", p)

    if re.search(p,text):
        print('Match!')
    else: print('No Match!')

# re.search returns a special match type,  not a boolean value

string = 'this is a string'
pattern = 'is'
match = re.search(pattern, string)
print(match)
print(type(match))
# Where is the first match
print(match.start())
# How many concidences are there?
print(re.findall(pattern, string))

def multi_re_find(patterns, phrase):

    for p in patterns:
        print('Searching for pattern {}'.format(p))
        print(re.findall(p, phrase))
        print('\n')

test_string = 'sdsd..sssddd..sdddsddd...dsds...dssss...sddddd'
# * searches for 's' followed with a 'd' reapeated 0 or more times
test_patterns0 = ['sd*']
multi_re_find(test_patterns0, test_string)

# + searches for 's' followed with one or more 'd'
test_patterns1 = ['sd+']
multi_re_find(test_patterns1, test_string)

# ? searches for 's' followed by one or zero 'd'
test_patterns2 = ['sd?']
multi_re_find(test_patterns2, test_string)

# Use curly brackets to search for a specific number or number of 'd'
test_patterns3 = ['sd{1,3}'] # if you want a specific number of d, use just one number
multi_re_find(test_patterns3, test_string)

# Use square brackets to group more than one coincidence, for example:
# ['s[sd]+'] this searches for an 's' followed by one or more 's' or one or more 'd'
test_patterns4 = ['s[sd]+']
multi_re_find(test_patterns4, test_string)

# To exclude specific characters, use curly brackets and the ['^'] symbol.
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns4 = ['[^!.?]+']

multi_re_find(test_patterns4, test_phrase)

# Search for sequences of lower case and upper case characters:
test_patterns5 = ['[a-z]+']
multi_re_find(test_patterns5, test_phrase)

# Searching for digits (\d) and non digits (\D)
text_with_digits = 'This is 0123 a text 879 with digits 000'
digit_finder = [r'\d+']
multi_re_find(digit_finder, text_with_digits)

# Searching for (\s) or non spaces (\S)
text_with_spaces = 'This is a normal text with spaces'
space_finder = [r'\s+']
multi_re_find(space_finder, text_with_spaces)

# Searching for alphanumeric (\w) or non alphanumeric (\W) characters
text_with_alphanumeric = 'This &** is a text with @##$$ alphanumeric and non (* alphanumeric characters'
alpha_finder = [r'\W+']
multi_re_find(alpha_finder, text_with_alphanumeric)

