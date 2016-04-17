import sys


def main():
    input_filename = "discnt.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "discnt.out" if len(sys.argv) == 1 else sys.argv[2]

    array, discount = read_input(input_filename)
    total = solve(array, discount)
    write_output(output_filename, total)


def read_input(filename):
    with open(filename, "r") as input_file:
        array_str = input_file.readline()
        array = [int(item) for item in array_str.split()]
        discount = int(input_file.readline())
        #print discount
        #print array
        return array, discount


def solve(array, discount):

    if len(array)>1:
        array_s = mergesort(array)
        l = len(array_s)
        #print l
        #print array_s[l-l//3:]
        #print discount
        #print float((100-discount)/100)
        #print array_s[:l-l//3]
        total = sum(array_s[l-l//3:])*(100-float(discount))/100 + sum(array_s[:l-l//3])
        #total =1
        print total
    else:
        #total = 1
        total = sum(array)
    return total

def mergesort(array):
    results = [None] * len(array)
    mergesort_recursive(array, 0, len(array) - 1, results)
    return results


def mergesort_recursive(array, left, right, merge_results):
    if left < right:
        middle = (left + right) // 2
        mergesort_recursive(array, left, middle, merge_results)
        mergesort_recursive(array, middle + 1, right, merge_results)
        merge(array, merge_results, left, middle + 1, right)


def merge(array, merge_results, left_begin, right_begin, right_end):
    left_end = right_begin - 1
    left_read_pos = left_begin
    right_read_pos = right_begin
    result_write_pos = left_begin

    while left_read_pos <= left_end and right_read_pos <= right_end:
        if array[left_read_pos] < array[right_read_pos]:
            merge_results[result_write_pos] = array[left_read_pos]
            left_read_pos += 1
        else:
            merge_results[result_write_pos] = array[right_read_pos]
            right_read_pos += 1

        result_write_pos += 1

    while left_read_pos <= left_end:
        merge_results[result_write_pos] = array[left_read_pos]
        left_read_pos += 1
        result_write_pos += 1

    while right_read_pos <= right_end:
        merge_results[result_write_pos] = array[right_read_pos]
        right_read_pos += 1
        result_write_pos += 1

    array[left_begin:right_end + 1] = merge_results[left_begin:right_end + 1]



def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write("{total:.2f}".format(**locals()))

if __name__ == "__main__":
    main()
