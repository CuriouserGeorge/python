def double(num1,num2):
    x = "False"
    for i in range(9):
        if "%i%i" % (i,i) in str(num1) and "%i%i" % (i,i) in str(num2):
           x = "True"
    return x


print(double(93339,63332316))
