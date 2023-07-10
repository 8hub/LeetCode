global_variable = 1

def f1():
    f_variable = 2
    print(f_variable)
    
    def f2():
        f_variable = max(f_variable, 3)
        print(f_variable)
    
    f2()

f1()
