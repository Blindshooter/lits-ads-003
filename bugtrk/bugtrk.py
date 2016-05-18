import sys


def main():
    input_filename = "bugtrk.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "bugtrk.out" if len(sys.argv) == 1 else sys.argv[2]

    N, W, H = read_input(input_filename)
    #print N,W,H
    result = solve(N,W,H)
    #result =1
    write_output(output_filename, result)


def read_input(filename):
    with open(filename, "r") as input_file:
        array_str = input_file.readline()
        array = [int(item) for item in array_str.split()]
        return array[0], array[1], array[2]

def solve(N, W, H):
    w = 1
    h = 1
    count = 1
    #print ("THIS IS N,H,W", N, W, H)
    while count < N:
        #print w, h, count
        #print ("w+1, W, h+1, H", w + 1, W, h + 1, H)
        if (w + 1) * W <= (h + 1) * H:
            #print ("INCREASE W")
            w += 1
            count += h
        else:
            #print ("INCREASE H")
            h += 1
            count += w
    return max(w*W,h*H)

def write_output(filename, total):
    with open(filename, "w") as output_file:
        output_file.write(str(total))

if __name__ == "__main__":
    main()