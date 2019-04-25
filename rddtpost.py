#receive python yada yada
msg = input()
string = 'abcdefghijklmnopqrstuvwxyz'
amap = {}
length = len(string)
out = ''

#for a in length:
#    amap[string[a]] = string[a]
for a in range(0,26):

    for b in range(0, 26):
        amap[string[b]] = string[(b + a) % 26]
    
    for c in range(0,len(msg)):
        out += amap[msg[c]]


    print(out)
    out = ''