#A variable which is used inside a function definition is a local variable and can be used
#only inside it

def check_scope():
    def local():
        test = "my name is kiran"

    def non_local():
        test = "my name is sudesh"

    def globals2():
        test = "my name is sree"

    test = "default"
    local()
    print("ich bin:"+test)


check_scope()

