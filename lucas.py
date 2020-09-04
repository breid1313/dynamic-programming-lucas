import argparse

def lucas(n):
    print("Initializing memoization storage...")
    R = []
    for i in range(0, n+1):
        R.append(-1)
    print("Calculating the Lucas number for n={}".format(n))
    return lucasAux(n, R)

def lucasAux(n,R):
    if R[n] > 0:
        return R[n]
    else:
        if n < 2:
            if n == 1:
                val = 1
            else:
                val = 2
        else:
            val = lucasAux(n-1, R) + lucasAux(n-2, R)
        R[n] = val
        return val

if __name__ == "__main__":
    # initialize the argument parser
    parser = argparse.ArgumentParser()

    # add the argument
    parser.add_argument("-n", "--number", dest="number", type=int, help="Number (counting from 0) in the sequence of Lucas numbers you wish to calculate.")

    # parse the argument
    args = parser.parse_args()

    # calculate the nth Lucas number
    result = lucas(args.number)
    print("The {}th value in the sequence of Lucas numbers is {}".format(args.number, result))
