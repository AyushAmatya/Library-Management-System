def read_item(file_name):
    list2=[]
    try:
        file=open(file_name,'r')
        item=file.readlines()
        for content in item:
            list1=[]
            detail=content.replace("\n","").split(",")
            for i in detail:
                list1.append(i)
            list2.append(list1)
        file.close()
    except:
        if file_name=="books_in_store.txt":
            print(">>>please enter the lists of book available in books_in_store.txt\n")
    return list2

def status(name):
    status= False
    try:
        file = open("borrowed.txt","r")
        lines= file.readlines()
        for line in lines:
            detail= line.split(",")
            if name in detail:
                status= True
        file.close()
    except:
        status= False
    return status

