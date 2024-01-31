#Here we use the global variable test hence what happens is that were the function is first
#called there it takes that test and set value to that and then print it 

def check_scope():
    def local():
        test = "my name is kiran"

    def non_local():
        nonlocal test
        test = "my name is sudesh"

    def globals2():
        global test
        test = "my name is sree"

    test = "default"
    local()
    print("ich bin:"+test)
    non_local()
    print("ich bin:"+test)
    globals2()


check_scope()
print("ich bin:"+test)

