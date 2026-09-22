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

if __name__ == "__main__":
    main()
