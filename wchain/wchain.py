import sys


def main():
    input_filename = "wchain.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "wchain.out" if len(sys.argv) == 1 else sys.argv[2]

    A, N = read_input(input_filename)
    result =  solve (A)
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        N = int(input_file.readline())
        A = []
        for line in input_file:
            A.append(line.split()[0])
        return A, N


def construct_dict(A):
    d = {}
    for x in A:
        key, val = len(x), x
        if key in d.keys():
            d[key].append(val)
        else:
            d[key]=[val]
        order_d = sorted(d.keys())
    return d, order_d

def check_str(string1, string2):
    it1 = iter(string1)
    it2 = iter(string2)
    count_diffs = 0
    c1 = next(it1, None)
    c2 = next(it2, None)
    while True:
        if c1 != c2:
            if count_diffs: return False
            count_diffs = 1
            c1 = next(it1)
        else:
            try:
                c1 = next(it1)
                c2 = next(it2)
            except StopIteration: return True


def solve(A):
    words, order_words = construct_dict(A)
    solution={}
    solution[order_words[0]] = [1]*len(words[order_words[0]])
    #print order_words
    g_max=1

    for l in order_words[1:]:
        #print l
        solution[l]=[]
        for w in words[l]:
            tmp=[]
            if l-1 in words.keys():
                for i in xrange(0,len(words[l-1])):
                    #print (words[l-1])
                    if check_str(w,words[l-1][i]):
                        tmp.append(solution[l-1][i]+1)
                    else:
                        tmp.append(solution[l-1][i])
                solution[l].append(max(tmp))
            else:
                solution[l] = [1] * len(words[l])
        if max(solution[l]) >= g_max:
            g_max = max(solution[l])
    return g_max


def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()