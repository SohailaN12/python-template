def main():
    name = " Sohaila"
    other_name = " Mr.Franklin"
    function_with_args(name)
    function_with_args(other_name)
    print("hello world")
#main() is defined with no arguments 
#def name_of_function():
#indent for code
#that belongs to function 
#     return variable ---> this is optional, if we don't write return, it will automatically return None 

    number = "5.0"
    number = int(float(number))
    print(type(number))

    print(f"Our output is {number}")
    name_of_function()
    print("all done!")

def name_of_function():
    # sample function to show structure 
    print("good example!")

def function_with_args(name):
    print(f"Hello, thank you for your focus{name}")

def calculate_area(width, height):
    return width * height

# we pass arguments to our function
def greeting(name):
    return f"Hello, {name}"

def make_a_fraction(x,y=1):
    return f"{x}/{y}"

def put_under_one(y,x=1):
    return f"{x}/{y}"

def put_under_one_alt(x):
    return f"1/{x}"

def main():
    # We can store return output into variables for later use
    my_greeting = greeting("Ms. Dinko")
    print(my_greeting)

    # print(make_a_fraction(15,4))
    print(make_a_fraction(15))
    



if __name__ == "__main__":
    main()
