def write_borrower_list(name, date, time, borrow_now, total,borrower_list):
    import datetime as d
    file= open("borrowed.txt", "w")
    for list1 in borrower_list:
        file.write(",".join(list1))
        file.write("\n")
    if borrow_now!=[]:
        file.write(name+","+ str(date)+ ","+str(time)+","+str(date+d.timedelta(days=10)))
        for list2 in borrow_now:
            file.write(","+list2[0])
        file.write(",Paid: $"+str(total))
    file.close()
    return

def write_books_list(file_name,items):
    file=open(file_name,"w")
    for i in items:
        line=",".join(i)
        file.write(line+"\n")
    file.close()
    return

def write_daily_details(date,topic, daily_record, name, time, borrow_now, tot_price):
    file= open(str(date)+".txt", "w")
    for list1 in daily_record:
        line=",".join(list1)
        file.write(line+"\n")
    file.write(topic+","+name+","+ str(date)+ ","+str(time))
    if topic=="BORROWED":
        for list2 in borrow_now: 
            file.write(","+list2[0])
    else:
        for list2 in borrow_now:
            file.write(","+list2)
    file.write(","+tot_price)
    file.close()
    return


    
    
