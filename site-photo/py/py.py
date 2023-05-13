def ver(e):
    if float(e) <= 0:
        return 'N'
    
    else:
        return 'P'
    

e = input("Digite um numero para ser argumento: ")
print(ver(e))

