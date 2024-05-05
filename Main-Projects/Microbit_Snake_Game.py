#fibonacci sequence
def fib():
    a = 0
    b = 1
    n = int(input("How many nums? "))
    for i in range(0, n+1):
        b += a
        a = b - a
        print(a)

#asterisk pyramid
import time
def pyramid(n):
    for i in range(0, n, 2):
        j = int((n-i)/2)
        print(j*" ", i*"*")
        time.sleep(0.1)

#upside down pyramid
def upside_down(n):
    for i in range(n, 0, -2):
        j = int((n-i)/2)
        print(j*" ", i*"*")
        time.sleep(0.1)   

#infinite vertical sine pattern
def v_sine():
    a = int(input("How wide? (even and numbers > 8 look cleaner)  "))
    while True:
        pyramid(a)
        upside_down(a)

#actual sine wave
def sine():
    amp = int(input("Amplitude? "))
    
