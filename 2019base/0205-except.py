while True:#没有异常，跳出循环
    try:
        x = int(input('ent num: '))
        print(x)
    except Exception as e:
        print('invalid num', e)
    else:
        break
    finally:
        print('clean up')