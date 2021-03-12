# 递归的小例子

def countdown(i:int):
    if i < 1:
        return
    else:
        print(i)
        countdown(i-1)

def fact(i:int):
    if i ==1:
        return 1
    else:
        return i * fact(i-1)



if __name__ == "__main__":
    print(f"{countdown(10)}")
    print(f"fact:{fact(4)}")