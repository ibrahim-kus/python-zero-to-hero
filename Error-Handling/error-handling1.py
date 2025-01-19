# google search python exeption hierarcy

while True:
    try:
        x = int(input('x:'))
        print(x/3)
    except Exception as ex:
        print('yanlış bilgi girildi.', ex)
    else:
        break
    finally:
        print('try except sonlandı')


if x > 5:
    raise Exception("x  den büyük değer olamaz")