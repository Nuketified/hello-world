# Exponent calculator

# define recursive function
def power(base, exponent):
    if exponent == 1:
       return base
    if exponent > 1:
        return power(base, exponent-1) * base
    if exponent == 0:
        return 1

    
# user program
def exponent():
  
    # get and validate base
    while True:
        try:
            your_base = (input("Please enther the base. "))
            your_base = int(your_base)
            break
           
        except ValueError:
            print("Base must be an integer.")
        
       



    # get and validate exponent
    while True:    
        try:
            your_exponent = input("Please enter the exponent. ")
            your_exponent = int(your_exponent)
            if your_exponent >= 0:
                break
            else:print("No negative exponents.")
        except ValueError:
            print("Exponent must be an integer.")

    # call power function and pass inputs
    your_answer = power(your_base,your_exponent)
    # print the answer
    print(f"\n{your_answer}")


exponent()