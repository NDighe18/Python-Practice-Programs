def greet(name):
    print("Hello {} !".format(name))

greet("Dev")
                                #prints becoz of print statment of function even though it doesn't have a return value!
return_value=greet("Muskan")           

print(return_value)#doesn't return anything since function has no return statement
