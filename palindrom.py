def palindrom(str):
    """
       str - string
    """
    cc=len(str)
    flaga=True
    for i in range(int(cc/2)):
        if str[i]!=str[cc-1-i]:
           flaga=False
    return flaga

print(palindrom('pota atop'))