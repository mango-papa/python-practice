fib = [0, 1]

def get(n):
    global fib

    if n <= 1:
        return fib[n]

    try:
        len(fib)
        print('value already exists {}'.format(fib[n]))
        return fib[n]
    except IndexError:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]
