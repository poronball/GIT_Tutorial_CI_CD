from payment import calculate as cal

def test(a,b):
    c = cal (a,b)

    test_c = a+b
    assert c == test_c

test(10,10)
test(30,10)
test(20,10)
