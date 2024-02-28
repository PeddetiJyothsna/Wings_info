import pytest
def main():
    a = int(input("enter a"))
    print("a square is: ", square(a))
def square(b):
    return b*b
if __name__=="__main__":
    main()
