import sys


def main():
    input_filename = "sigkey.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "sigkey.out" if len(sys.argv) == 1 else sys.argv[2]
    alph = 'abcdefghijklmnopqrstuvwxyz'
    asc = []
    for i in xrange(1, len(alph) + 1):
        asc.append(sum(bytearray(alph[:i])))

    N, d = read_input(input_filename)
    #print d
    #print len(d[0])
    result =  solve (d, asc)
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        N = int(input_file.readline())
        d = []
        for line in input_file:
            d.append(line.split()[0])
        return N, d

def split_array(array):
    a = [e for e in array if e.find("a") != -1]
    b = [e for e in array if e.find("a") == -1]
    #print a, b
    return a, b

def check_elig(st1, st2, asc):
    #print st1+st2
    #print len(st1+st2)
    #print sum(bytearray(st1+st2))
    #print asc[len(st1+st2)-1]
    if sum(bytearray(st1+st2))==asc[len(st1+st2)-1]:
        return 1
    else:
        return 0

def find_missing(s):
    x = ''.join(sorted(s))
    alpha = map(chr, range(97, 1+ord(s[-1])))

    missing = ''
    for s in alpha:
        if x.find(s) == -1:
            missing +=s
    return missing

def solve(array, asc):
    x = dict()
    for e in array:
        x[''.join(sorted(e))]= find_missing(e)
    #print x
    count = 0
    for value in x.values():
        if value in x.keys():
            count+=1
    return count

def solve1 (array, asc):
    a, b = split_array(array)
    count = 0
    for st1 in a:
        for st2 in b:
            #print st1, st2
            if len(st1+st2)>26:
                pass
            else:
                count+=check_elig(st1, st2, asc)
    return count

def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()
