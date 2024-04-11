input = ('Hello', 'World', 'from', 'Python')
def concatenate_strings(input_tuple):
    concatenated_string = ' '.join(input_tuple)
    return concatenated_string
print(concatenate_strings(input))