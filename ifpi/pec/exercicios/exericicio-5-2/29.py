def verifica(s):
    if (s.isdecimal()):
        s = True
    elif(s.isalpha()):
        s = True
    else:
        s = False
    return s

def main():
    s = str(input().strip())
    print(verifica(s))
    
if __name__ == '__main__':
    main()
