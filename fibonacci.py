def fibonacci(n):
   
    if n in (0, 1): # base cases
        return n, 1
           
    else:
        f1, n1 = fibonacci(n - 1) 
        f2, n2 = fibonacci(n - 2)
        return f1 + f2, n1 + n2 + 1
               
    
#printfunction calls

fib_10 = fibonacci(10)
fib_20 = fibonacci(20)
fib_30 = fibonacci(30)

print(f"fibonacci(10) = {fib_10}")
print(f"fibonacci(20) = {fib_20}")
print(f"fibonacci(30) = {fib_30}")

fib_3 = fibonacci(3)
print(fib_3)

