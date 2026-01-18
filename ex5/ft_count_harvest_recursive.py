def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(i):
        if (i > days):
            print("Harvest time!")
        elif (i <= days):
            print("Day", i)
            helper(i + 1)
    helper(1)
