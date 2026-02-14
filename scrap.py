# print("hallo world")

def my_function(title,*args,**kwargs):
    print("title:",title)
    print("positional arguments",args)
    print("keyword argument:",kwargs)
    
my_function('scrapping project',"Emil", "Tobias", age = 25, city = "Oslo")
    
    
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)