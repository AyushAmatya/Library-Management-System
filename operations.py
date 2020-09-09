def bow_bill(name, date, borrow_now, time):
    from tabulate import tabulate
    import datetime as d
    total=0.0
    for list1 in borrow_now:
        del list1[2]
        total=total+float(list1[2].replace("$",""))
    bill="________________________________________________________________________________\n"
    bill=bill+"Name:"+name+"\nDate of book borrowed: "+str(date)+"\nTime of transaction: "+str(time)
    bill=bill+"\nDate to return the book: "+str(date + d.timedelta(days=10))+"\n\n"    
    print("________________________________________________________________________________")
    print("\nNAME: ", name)
    print("Date of book borrowed: ", date)
    print("Time of transaction: ", time)
    print("Date to return the book: ",date + d.timedelta(days=10),"\n")
    print(tabulate(borrow_now,headers=["Name of book","Auther name","Price"]))
    bill=bill+tabulate(borrow_now,headers=["Name of book","Auther name","Price"])
    print("\nTOTAL PRICE: $",total)
    bill=bill+"\n\nTOTAL PRICE: $"+str(total)+"\n\nNOTICE: If you are late to return the book, $0.1 will be charged for each day late of each book\n________________________________________________________________________________"
    print("\nNOTICE: If you are late to return the book, $0.1 will be charged for each day late of each book\n________________________________________________________________________________")
    return total,bill

def edit_stock(to_do,books_for_borrow,borrow_now):
    if to_do=="REDUCE":
        for book in borrow_now:
            for list1 in books_for_borrow:
                if book[0]==list1[0]:
                    list1[2]=str(int(list1[2])-1)
    elif to_do=="ADD":
        for book in borrow_now:
            for list1 in books_for_borrow:
                if book==list1[0]:
                    list1[2]=str(int(list1[2])+1)
    return books_for_borrow

def store_date(d):
    from datetime import date
    d=d.split("-")
    date1=date(int(d[0]),int(d[1]),int(d[2]))
    return date1

def detailed_returned(db, date, returned_book, name, b_items):
    import datetime as d
    br={"Name of book:":[],"Date borrowed:":[],"Date to return:":[],"Date returned:":[]}
    fine=0.0
    book_items=b_items
    for list1 in book_items:
        if list1[0]==name:
            for b_name in returned_book:
                if b_name in list1:
                    """if b_name+"(RETURNED)" not in list1:"""
                    br["Name of book:"].append(b_name)
                    index_num=db["Name of book:"].index(b_name)
                    br["Date borrowed:"].append(db["Date borrowed:"][index_num])
                    br["Date to return:"].append(db["Date to return:"][index_num])
                    br["Date returned:"].append(date)
                    date_r=store_date(db["Date to return:"][index_num])
                    for index, value in enumerate(list1):
                        if value==b_name:
                            list1[index]=list1[index]+"(RETURNED)"
                    all_returned=True
                    for index in range(4,len(list1)-1):
                        if "(RETURNED)" not in list1[index]:
                            all_returned=False
                    if all_returned==True:
                        for index, value in enumerate(b_items):
                            if value==list1:
                                b_items[index]=""
    while "" in b_items:
        b_items.remove("")
                    
    return br

    
def ret_bill(name,time, date, return_now,returned_details):
    fine_=0.0
    for i in range(len(return_now)):
        date_to_ret=store_date(returned_details["Date to return:"][i])
        if date>date_to_ret:
            fine_days=date-date_to_ret
            fine_=fine_+float(fine_days.days*0.1)
    from tabulate import tabulate
    bill="________________________________________________________________________________"
    bill=bill+"\nNAME: "+name+"\nDate of transaction: "+str(date)
    bill=bill+"\nTime of transaction: "+str(time)+"\n\n"+tabulate(returned_details, headers="keys")
    print("________________________________________________________________________________")
    print("\nNAME: ", name)
    print("Date of transaction: ",date)
    print("Time of transaction: ",time)
    print("\n")
    print(tabulate(returned_details, headers="keys"))
    print("\nFine: $", fine_)
    bill=bill+"\n\nFine: $"+str(fine_)+"\n________________________________________________________________________________"
    print("________________________________________________________________________________")
    return fine_,bill

def list_after_ret(borrower_list,name,return_now):
    for book in return_now:
        for list1 in borrower_list:
            if list1[0]==name and book in list1:
                for index, value in enumerate(list1):
                    if value==book:
                        list1[index]=list1[index]+"(RETURNED)"
            all_returned=True
            for i in range(4,len(list1)-1):
                if "(RETURNED)" not in list1[i]:
                    all_returned=False
            if all_returned==True:
                list1=""
    while "" in borrower_list:
        borrower_list.remove("")
    return borrower_list



def today_date():
    import datetime as d
    date= d.date(d.datetime.now().year, d.datetime.now().month, d.datetime.now().day)
    return date

def time_now():
    import datetime as d
    time= str(d.datetime.now().hour)+":"+ str(d.datetime.now().minute)+":"+ str(d.datetime.now().second)
    return time

def check_borrowed(borrowed_list, books_for_borrow):
    already_borrowed=False
    if books_for_borrow[book_num-1][0] in borrowed_list:
        already_borrowed= True
    return already_borrowed

def books_he_took(name,borrower_list):
    list1=[]
    for line in borrower_list:
        if name == line[0]:
            for book_index in range(4,len(line)-1):
                list1.append(line[book_index])
    return list1


