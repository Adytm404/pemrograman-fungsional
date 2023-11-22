def uppercase_decorator(function):
    def wrapper():
        func = function() #so that function can access upper() 
        return func.upper() 
    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
result = decorate()
print(result)




