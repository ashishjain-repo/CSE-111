def test_min():
    assert min(7,-3,0,2) == 2

def comparrision(one,two):
    if abs(one-two) < 0.01:
        print("Close Enough")
    else:
        print("Not Equal")

if __name__ == "__main__":
    # test_min()
    # comparrision(1.2,1.201)
    pass
