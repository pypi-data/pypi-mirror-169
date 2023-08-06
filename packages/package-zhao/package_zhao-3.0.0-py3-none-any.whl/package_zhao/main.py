def multi_table():

    nums = int(input("请输入一个任意的正整数："))

    out_num = 1
    while out_num <= nums:
        inner_num = 1
        while inner_num <= out_num:
            print(f"{out_num}*{inner_num}={out_num*inner_num} ", end="")
            inner_num += 1
        print()
        out_num += 1