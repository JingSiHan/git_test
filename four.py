def carry(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return carry(n-1) + carry(n-2) + carry(n-3)



if __name__ == "__main__":
    n = int(input("输入物品数："))
    res = carry(n)
    print(res)
