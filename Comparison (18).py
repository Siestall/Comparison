try:
    n1 = int(input('Enter num 1: '))
    n2 = int(input('Enter num 2: '))
    if n1 != n2:
        res = f'{n1} > {n2}' if n1 > n2 else f'{n2} > {n1}'
    else:
        res = f'{n1} = {n2}'

    print(res)
except:
    print('Enter integer')