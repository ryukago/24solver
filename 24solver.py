import time

num1 = input()
while (eval(num1) < 0):
    num1 = input()
num2 = input()
while (eval(num2) < 0):
    num2 = input()
num3 = input()
while (eval(num3) < 0):
    num3 = input()
num4 = input()
while (eval(num4) < 0):
    num4 = input()

num = ([num1,num2,num3,num4])
op = (['+','-','*','/'])
x = list()
count = 0

start = time.time()

idx1 = 0
for a in num:
    idx2 = 0
    for b in num:
        idx3 = 0
        if (idx2 != idx1):
            for c in num:
                idx4 = 0
                if (idx3 != idx2) and (idx3 != idx1):
                    for d in num:
                        if (idx4 != idx3) and (idx4 != idx2) and (idx4 != idx1):
                            for op1 in op:
                                for op2 in op:
                                    for op3 in op:
                                        str = "((" + a + op1 + b + ')' + op2 + c + ')' + op3 + d
                                        try:
                                            hasil = eval(str)
                                        except Exception as e:
                                            hasil = 0
                                        if (hasil == 24) and ((str in x) == False):
                                            print(str)
                                            x.append(str)
                                            count = count + 1
                                        str = '(' + a + op1 + '(' + b + op2 + c + "))" + op3 + d
                                        try:
                                            hasil = eval(str)
                                        except Exception as e:
                                            hasil = 0
                                        if (hasil == 24) and ((str in x) == False):
                                            print(str)
                                            x.append(str)
                                            count = count + 1
                                        str = '('+ a + op1 + b + ')' + op2 + '(' + c + op3 + d + ')'
                                        try:
                                            hasil = eval(str)
                                        except Exception as e:
                                            hasil = 0
                                        if (hasil == 24) and ((str in x) == False):
                                            print(str)
                                            x.append(str)
                                            count = count + 1
                                        str = a + op1 + '(' + b + op2 + '(' + c + op3 + d + "))"
                                        try:
                                            hasil = eval(str)
                                        except Exception as e:
                                            hasil = 0
                                        if (hasil == 24) and ((str in x) == False):
                                            print(str)
                                            x.append(str)
                                            count = count + 1
                                        str = a + op1 + "((" + b + op2 + c + ')' + op3 + d + ')'
                                        try:
                                            hasil = eval(str)
                                        except Exception as e:
                                            hasil = 0
                                        if (hasil == 24) and ((str in x) == False):
                                            print(str)
                                            x.append(str)
                                            count = count + 1
                        idx4 = idx4 + 1
                idx3 = idx3 + 1
        idx2 = idx2 + 1
    idx1 = idx1 + 1

print(count)
print("waktu eksekusi = %s detik" % (time.time() - start))
y = input()
