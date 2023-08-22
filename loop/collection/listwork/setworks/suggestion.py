allusers=["mohanlal","fahad","dq","vijay","nivin","asif","mamootty"]

dq_friendlist=["mohanlal","fahad","asif","mamootty"]
asif_friendlist=["mohanlal","fahad","vijay","nivin","mamootty"]
# suggestion for dq
# dq=>asif? mutual friends

suggestion=set(allusers).difference(set(dq_friendlist))
suggestion.remove("dq")
# print(suggestion)

mutual_friends=set(asif_friendlist).intersection(dq_friendlist)
print(mutual_friends)



