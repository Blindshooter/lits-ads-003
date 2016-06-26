import sys


def main():
    input_filename = "career.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "career.out" if len(sys.argv) == 1 else sys.argv[2]

    #print read_input(input_filename)
    A, N = read_input(input_filename)
    result =  solve (A, N)
    #array, discount = read_input(input_filename)
    #total = solve(array, discount)
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        N = int(input_file.readline())
        A = []
        for line in input_file:
            A.append(line.split())
        #array_str = input_file.readline()
        #array = [int(item) for item in array_str.split()]
        #discount = int(input_file.readline())
        return A, N


def solve (A, l):
    solutions = []
    solutions.append([0 for _ in range(0, l + 1)])
    for i in xrange(l):
        s = [int(A[l - i - 1][j]) + max(solutions[i][j], solutions[i][j + 1]) for j in xrange(l - i)]
        solutions.append(s)
    return solutions[l][0]



def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()