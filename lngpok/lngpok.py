import sys


def main():
    input_filename = "lngpok.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "lngpok.out" if len(sys.argv) == 1 else sys.argv[2]

    array = read_input(input_filename)
    result = solve1(array)
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        array_str = input_file.readline()
        array = [int(item) for item in array_str.split()]
        return array


def csort(a, min, max):
    cnt = [0] * (max - min + 1)
    for x in a:
        if x == 0:
            cnt[x - min] += 1
        else:
            cnt[x - min] = 1
    jokers = cnt[0]
    array = [x+1 for x, n in enumerate(cnt[1:], start=min) for i in xrange(n)]
    return array, jokers


def solve(a):
    if sum(a)==0:
        return len(a)
    #print(a)
    w, j = csort(a, 0, max(a))
    #print(w,j)
    w1 = [w[i+1]-w[i]-1 for i in xrange(len(w)-1)]+[j+1]
    #print(w1, len(w1))
    count = 0
    k = 0
    while k <=len(w1)-count:
        cum = 0
        l = 0
        i=k
        while cum<=j and i<len(w1):
            cum+=w1[i]
            l+=1
            i+=1
        if l>count:
            count = l
        k+=1
    return count+j

def solve1(a):
    if sum(a)==0:
        return len(a)
    w, j = csort(a, 0, max(a))
    w1 = [w[i+1]-w[i]-1 for i in xrange(len(w)-1)]+[j+1]
    return lca(w1, j, len(w1), max = len(w1))+1+j

def lca(a, j,len_initial_arr, N = 0, max_len = 1, min=0, max=0):

    if 2**N>len_initial_arr:
        return max_len
    else:
        N+=1
        #print ("N is", N)
        M = max
        m = min
        #print ("Minmax are", min, max)
        pivot = (M+m)//2
        #print ("Pivot is ", pivot)

        for i in xrange(len(a)-pivot+1):
            flag = True
            #print ("Now array", a[i:i+pivot], "compare to", j, "SUM IS",sum(a[i:i+pivot]) )
            if sum(a[i:i+pivot])<=j:
                flag = False

                #print ('should be break', i)
                break
            else:
                i+=1
        if flag==False:
            #print ("PIVOT >=max_len", pivot, max_len)
            max_len = pivot
            #print ("New max_len", max_len)
            m = pivot
            #print("I is", i)
            new_arr = a
            return lca(new_arr, j, len_initial_arr, N, max_len, m, M)
        else:
            M = pivot
            return lca(a, j, len_initial_arr, N, max_len, m, M)



def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()


