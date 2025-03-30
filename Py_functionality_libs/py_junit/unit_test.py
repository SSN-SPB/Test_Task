# Example code to be tested
def add_numbers(x, y):
    return x + y
 
# Test case
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-2, 2) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 7.0 , "Wrong value add_numbers(1.5, 2.5) == 7.0"
    try:
        assert add_numbers(1.5, 2.5) == 5.0, "Wrong value (1.5, 2.5) == 5.0"
        print("Wrong value:")
    except AssertionError as aer:
        print('catched below')
        print(aer)
    assert add_numbers(1.5, 2.5) == 9.0, "Wrong value add_numbers(1.5, 2.5) == 9.0"

def main():
    try:
        test_add_numbers()
    except AssertionError as ae:
        print(ae)



if __name__ == "__main__":
    main()
