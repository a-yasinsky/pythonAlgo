
def binary_search(input_array, value):
    start_value = 0
    end_value = len(input_array)
    middle = 0
    length = end_value - start_value
    print(start_value, end_value, length)
    while length > 0:
        if length == 1:
            middle = end_value
        elif length % 2 > 0:
            middle = start_value + length // 2 + 1
        else:
            middle = start_value + length // 2
        if input_array[middle - 1] == value:
            return middle - 1
        elif input_array[middle - 1] > value:
            end_value = middle - 1
        else:
            start_value = middle
        length = end_value - start_value

        print(middle, start_value, end_value, length)
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
