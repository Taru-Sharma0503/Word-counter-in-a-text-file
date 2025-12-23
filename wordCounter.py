try:
    f=open('file.txt','r')
    count=0
    while True:
        line=f.readline()
        if not line:
            break
        words=list(line.split(" "))
        for i in words:
            count=count+1
    f.close()
    print("Total number of words in the text file:",count)
except Exception as e:
    print(e,"Error has occured")
