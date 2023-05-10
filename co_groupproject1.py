def binaryconverter(number):
    l=[]
    while number!=0:
        rem=str(number%2)
        l.append(rem)
        number=number//2
    l.reverse()        
    while len(l) < 8:
        l.insert(0,'0')
    binary_string = ''.join(l)
    return binary_string
  
  
       
