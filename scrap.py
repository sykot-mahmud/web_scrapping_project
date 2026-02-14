# print("hallo world")

def my_function(title,*args,**kwargs):
    print("title:",title)
    print("positional arguments",args)
    print("keyword argument:",kwargs)
    
my_function('scrapping project',"Emil", "Tobias", age = 25, city = "Oslo")
    