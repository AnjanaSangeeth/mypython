text="ABBAACD"
# most recursive charater
wc={}   #{A:1}

for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

print(wc)
wc={'A': 3, 'B': 2, 'C': 1, 'D': 1}

print(max(wc , key= lambda k: wc.get (k)))

print(min(wc,key=lambda k: wc.get(k)))