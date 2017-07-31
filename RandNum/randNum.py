import random, string

f = open('Promo_code.txt', 'wb')

for i in range(200):
    chars = string.letters + string.digits
    #print chars
    s = [random.choice(chars) for i in range(10)]
    print s
    f.write(''.join(s) + '\n')
f.close()





