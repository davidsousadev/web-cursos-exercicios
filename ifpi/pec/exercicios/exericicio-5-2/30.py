def verifica(s):
    if (s.isdecimal()):
        s = False
    elif(s.isalpha()):
        s = False
    else:
        s = True
    return s

def main():
    s = str(input().strip())
    print(verifica(s))
    
if __name__ == '__main__':
    main()
