# movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}

# q1 print all movies names
# q2 print top rated move
# q3 sort movie wrt rating order by dec
# print(movies.keys())

# print(max(movies,key=lambda k: movies.get(k)))

# out=sorted(movies,reverse=True,key=lambda k:movies.get(k))
# print(out)


movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]

#q1 print all movie name


# for m in movies:
#     print(m.get("name"))

# movie_name=[m.get("name")for m in movies]
# print(movie_name)


# [return  loop  condition]


#q2 print filter movies with genre=mystery


# for m in movies:
#     if "mystery" in m.get ("genres"):
#         print(m.get("name"))

# movies_mystery=[m.get("name")for m in movies if "mystery" in m.get("genres")]
# print(movies_mystery)



#q3 top rated movie names

print(max(movies,key=lambda m:m.get("rating")))



#q4 print malayalam movie names

#q5 movies names relased in 2023

#q6 order movies wrt rating order by desc
















