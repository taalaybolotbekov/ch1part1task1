def is_even(b):
    if b % 2 == 0:
        return True
    else:
        return False
    # for i in range (25):

def test_is_even():
    assert is_even(2) == True 
    assert is_even(3) ==False 
    assert is_even(8) == True 
    assert is_even(100) == True 
    assert is_even(101) == False
print("YOUR CODE IS CORRECT!") 
