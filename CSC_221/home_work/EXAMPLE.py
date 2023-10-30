def int_to_reverse_binary(integer_value):
    
    h = integer_value % 2
    print(h)
    integer_value = integer_value // 2
    return integer_value
    
def string_reverse(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string += char
    return reversed_string

if __name__ == '__main__':
    
    integer = input()
    
    reverse_binary = int_to_reverse_binary(integer)
    binary = string_reverse(integer)
    print(binary)