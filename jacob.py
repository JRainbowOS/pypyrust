def make_list_to_n(n: int) -> list:
    return [i for i in range(n)]

def main():
    n = 10
    my_list = make_list_to_n(n)
    print(my_list)
    
if __name__ == '__main__':
    main()