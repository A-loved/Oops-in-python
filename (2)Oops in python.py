#Here inside the non local function we used a keyword nonlocal which specifies that the
#test variable used inside that function is the test variable which is outside the non local function
#which is the check_scope() functions test variable.

def check_scope():
    def local():
        test = "my name is kiran"

    def non_local():
        nonlocal test
        test = "my name is sudesh"

    def globals2():
        test = "my name is sree"

    test = "default"
    local()
    print("ich bin:"+test)
    non_local()
    print("ich bin:"+test)


check_scope()

