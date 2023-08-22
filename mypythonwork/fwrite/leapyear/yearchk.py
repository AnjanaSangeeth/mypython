fread=open("C:\\Users\\anjna\\OneDrive\\Desktop\\mypythoncode\\mypythonwork\\fwrite\\leapyear\\num\\num.txt","r")

fwrite=open("C:\\Users\\anjna\\OneDrive\\Desktop\\mypythoncode\\mypythonwork\\fwrite\\leapyear\\year.txt","w")

for line in fread:
    # line="1890\n"
    year=int(line.rstrip("\n"))

    if(year %100==0 and year %400==0):
        fwrite.write(str(year)+"\n")
    elif(year %100!=0 and year %4==0):
        fwrite.write(str(year)+"\n")
print("finished")