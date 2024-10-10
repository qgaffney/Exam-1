for i in range(1, 51):
    if i%5==0:
        print("HiFive")
    elif i%2 ==0:
        print("HiTwo")
    else:
        if i%3==0 & i%7==0:
            print("HiThreeOrSeven")