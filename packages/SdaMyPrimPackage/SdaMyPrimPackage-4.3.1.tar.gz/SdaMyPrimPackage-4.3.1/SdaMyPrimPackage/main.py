def generate_prim_numbers(max_num=100):
    for num in range(1, max_num + 1):
        is_prim = True
        for i in range(num - 1, 1, -1):
            if num % i == 0:
                is_prim = False
                break

        if is_prim is True:
            print(f'{num} is a prim numer !!')


generate_prim_numbers(15)

# SdaMyPrimPackage