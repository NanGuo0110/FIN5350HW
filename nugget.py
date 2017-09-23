def is_nugget_number(target, small=6, medium=9, large=20):
    for i in range(target// small + 1):
        for j in range(target// medium + 1):
            for k in range(target// large + 1):
                if (small * i + medium * j + large * k == target):
                    return True

    return False



def main():
    small = 6
    count = 0
    largest = small - 1
    target= small

    while count != small:
        if is_nugget_number(target):
            count += 1
        else:
            largest = target
            count = 0
        target += 1
    print("the highest number of nugget that you can not purchase is",largest)
    




main()

