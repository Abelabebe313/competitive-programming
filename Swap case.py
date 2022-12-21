def swap_case(s):
    final = ''
    
    for i in s:
        if i.isupper():
            final+= i.lower()
        else:
            final+= i.upper()
            
    return final
 
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
