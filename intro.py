from subprocess import call 
from time import sleep
noOver = True
while noOver:
    _ = call("clear")
    print("Bievendino")
    print("1. decir hola mundo")
    print("2. salir")
    op = raw_input("elejir opcion: ")

    if op == "1":
        print("hola mundo")
        sleep(2)
    if op == "2":
        noOver = False