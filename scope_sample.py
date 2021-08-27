def check_scope():
    def do_local():
        test = "local Test"
    def do_non_local():
        nonlocal test
        test = "non local Test"
    def do_global():
        global test
        test = "global Test"


    test="default"
    do_local()
    print("test value after do local:"+test)
    do_non_local()
    print("test value after non local:"+test)
    do_global()
    print("test value after global:"+test)


check_scope()
print("test value after global outside:"+test)