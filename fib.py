def fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1 :
        return 1
    elif n > 1:
        a: int = 0
        b: int = 1
        i: int = n - 1
        while i:
            a_new: int = b
            b_new: int = a + b 
            # a, b = a_new, b_new 
            a = a_new
            b = b_new
            i -= 1
        return b

def main():
    for i in range(10):
        print(fib(i))

if __name__ == '__main__':
    main()