
def input_r_b():
    r_b= input("\n>>>Do you want to return the book or borrow another book?(r/b): ").lower()
    while r_b!='r' and r_b!='b':
        r_b=input(">>>Please enter r or b for above asked question: ").lower()
    return r_b




def display_books_took(borrower_list, name):
    from tabulate import tabulate
    i=1
    list_to_return={"S.N":[],"Name of book:":[],"Date borrowed:":[],"Date to return:":[]}
    for lists in borrower_list:
        if lists[0]== name:
            for index in range(4,len(lists)-1):
                if "(RETURNED)" not in lists[index]:
                    list_to_return["S.N"].append(i)
                    list_to_return["Name of book:"].append(lists[index])
                    list_to_return["Date borrowed:"].append(lists[1])
                    list_to_return["Date to return:"].append(lists[3])
                    i=i+1
    print("\nName: ", name,"\n")
    print(tabulate(list_to_return, headers="keys"))
    return list_to_return

def books_returned(list_to_return):
    i=len(list_to_return["S.N"])+1
    return_now=[]
    sucess=False
    while sucess==False:
        try:
            rt=input("\n>>>WHICH BOOK DO YOU WANT TO RETURN[if multiple books, then seperate the numbers with comma(,)](eg:1,2,3,...):")
            print("\n")
            rt=rt.split(",")
            rt=list(set(rt))
            for j in rt:
                sucess=False
                if int(j)>0 and len(rt)<i and int(j)<i:
                    sucess=True
                else:
                    print("Please input the numbers given in above list.")
                    break
        except:
            print("Please input the numbers given in above list.")
            sucess=False
    for num in rt:
        return_now.append(list_to_return["Name of book:"][int(num)-1])
    return return_now



def display_available(books_for_borrow,borrowed_already):
    print("\n>Here are the lists of the books that we have in store:")
    for i in range(len(books_for_borrow)):
        print(i+1,") ",books_for_borrow[i][0]," by ",books_for_borrow[i][1])
    sucess=False
    borrow_now=[]
    while sucess==False:
        try:
            num=input("\n>>> Which number book do you want to borrow?[If nore than one then seperate numbers with comma(,)(1, 2, 3...): ")
            num=num.split(",")
            num=list(set(num))
            choosed_num=[]
            for n in num:
                choosed_num.append(int(n))
                if int(n)>0 and int(n)<len(books_for_borrow)+1:
                    sucess=True
                else:
                    sucess=False
                    print("\nPlease enter the numbers shown in the list")
        except:
            sucess=False
            print("\nPlease enter numbers, not string.")
    for choosed in choosed_num:
        borrow_now.append(books_for_borrow[choosed-1])
        if books_for_borrow[choosed-1][0] in borrowed_already:
            print("\nYou have already borrowed book name: ",books_for_borrow[choosed-1][0])
            ans=input("\n>>>Do you want to borrow other ordered books?(y/n)").lower()
            while ans!='y' and ans!='n':
                ans=input(">>>Please input y or n in above asked question: ")
            if ans=='n':
                borrow_now="no"
                break
            else:
                borrow_now.remove(books_for_borrow[choosed-1])
        if int(books_for_borrow[choosed-1][2])<1:
            print("\nSORRY!!!",books_for_borrow[choosed-1][0]," is out of stock.")
            ans=input("\n>>>Do you want to borrow other ordered books?(y/n)").lower()
            while ans!='y' and ans!='n':
                ans=input(">>>Please input y or n in above asked question: ")
            if ans=='n':
                borrow_now="no"
                break
            else:
                borrow_now.remove(books_for_borrow[choosed-1])
    return borrow_now
    
