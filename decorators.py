
def decorator(func):
    def wrapper(*args, **kwrgs):
        print(f"Hello {args[0]} its secret!!")
        func(*args, **kwrgs)
    return wrapper

@decorator
def secret(name):
    print(f"{name} The Treasure is hidden below the bed")

secret("Bushra")


# Learning how to use decorators in Python can be very useful for adding functionality to existing functions without modifying their structure. In the example 
# we have a simple decorator called `decorator` that takes a function as an argument and defines a wrapper function inside it. The wrapper function adds some additional
# behavior (printing a message) before calling the original function.

def cal_bal(func):
    def wrapper(*args, **kwrgs):
        print("Calculating balance...")
        funct = func(*args, **kwrgs)
        for names, bal in funct.items():
            raw = f"${bal:.2f}"
            print(f"{names} has balance of {raw} ")
        
    return wrapper

@cal_bal
def Balance(account):
     return account

Balance({"Rahul":50, "vijay":80})


