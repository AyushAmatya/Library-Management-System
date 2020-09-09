import read as r
import write as w
import operations as o
import display as d
import datetime
new='y'
bill=''
while new=='y':
    print("\t\t\t\tWelcome to BookStore: ")
    name=input("Enter your full name: ").upper()
    date= o.today_date()
    time= o.time_now()
    books_for_borrow=r.read_item("books_in_store.txt")
    daily_record= r.read_item(str(date)+".txt")
    borrower_list= r.read_item("borrowed.txt")
    if r.status(name)== True:
        borrowed_already= o.books_he_took(name,borrower_list)
        r_b= d.input_r_b()
    else:
        r_b= 'b'
        borrowed_already=[]
    if r_b=='b':
        borrow_now=d.display_available(books_for_borrow,borrowed_already)
        books_for_borrow=o.edit_stock("REDUCE",books_for_borrow,borrow_now)
        w.write_books_list("books_in_store.txt",books_for_borrow)
        if borrow_now==[]:
            print("\n>>>No books remains")
        else:
            total,bill=o.bow_bill(name, date, borrow_now, time)
            w.write_borrower_list(name, date, time, borrow_now, total, borrower_list)
            w.write_daily_details(date, "BORROWED", daily_record, name, time, borrow_now, "Paid: $"+str(total))
            
    else:
        list_to_return=d.display_books_took(borrower_list, name)
        return_now= d.books_returned(list_to_return)
        returned_details = o.detailed_returned(list_to_return, date, return_now, name, borrower_list)
        books_for_borrow=o.edit_stock("ADD",books_for_borrow,return_now)
        w.write_books_list("books_in_store.txt",books_for_borrow)
        fine_,bill = o.ret_bill(name,time, date, return_now,returned_details)
        borrower_list= o.list_after_ret(borrower_list,name,return_now)
        w.write_borrower_list(name, date, time, [], 0, borrower_list)
        w.write_daily_details(date, "RETURNED", daily_record, name, time, return_now, "Fine: $"+str(fine_))
        
    print("\nTHANK YOU FOR YOUR VISIT! \nPLEASE VISIT AGAIN.")
    file=open(name+".txt","w")
    file.write(bill)
    file.close()
    new=input("\n>>>New costomer?(y/n): ").lower()
    while new!='y' and new!='n':
        new=input("Please enter y or n in above asked question.").lower()





        
