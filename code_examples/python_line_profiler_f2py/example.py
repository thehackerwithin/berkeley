@profile
def example_function(myRange):
    # directly convert range to string list
    str_list = []
    for i in myRange:
        str_list.append(str(i))
        
@profile   
def example_function2(myRange):
    # use list comprehension to convert range to string list
    str_list = [str(i) for i in myRange] 
        
example_function(range(1000000))
example_function2(range(1000000))