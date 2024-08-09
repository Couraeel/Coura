from linguagempt1 import *

if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'C':
            create()
        elif op == "R":
            read()
        elif op == "U":
            update()
        elif op == "D":
            delete()
        elif op == "E":
            print("Exit")
        