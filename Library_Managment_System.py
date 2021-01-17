print("               ## Welcome To Library Managment System ## ")
diction1={}
class Library:
    def __init__(self,List_of_books,Library_name):
        self.List_of_Books=List_of_books
        self.Library_Name=Library_name
        pass
    def Displaye_Book(self):
        print(self.List_of_Books)
    def Lend_Book(self,Book,Name):
        global diction1
        self.Book=Book
        self.Name=Name
        asdf=0
        for a in self.List_of_Books:
            if a==self.Book:
                if self.Book in diction1.keys():
                    print("Sorry ! the book is already issued by",diction1[self.Book])
                else:
                    asdf=1
        if asdf==1:
            print(f'Done the book "{self.Book}" is issued on the name of "{self.Name}"')
            a={self.Book:self.Name}
            diction1[self.Book]=self.Name
            # print(diction1)
    def Add_Book(self,name_of_book,don):
        self.name_of_book=name_of_book
        self.don=don
        print(f" Thanks to '{self.don}' for Donating '{self.name_of_book}' book to the Library")
        return (self.List_of_Books).append(self.name_of_book)
    def Return_Book(self,book,name):
        self.book=book
        self.name=name
        del diction1[self.book]
        print(f'Done the book "{self.book}" is Submmited by "{self.name}" to the Library ')
yashlibrary=Library(["The Secret","Immortals of Meluha","The Secret of Nagas",'The Oath of The Vayuputra'],"Mahakal Library")
# yashlibrary.Add_Book("2 States")
# yashlibrary.Displaye_Book()
# yashlibrary.Lend_Book("2 States","Yash")
# yashlibrary.Lend_Book("Immortals of Meluha","Naresh")
#
# yashlibrary.Return_Book("2 States","Yash")
# # Library.
# yashlibrary.Lend_Book("2 States","Suresh")
# print(yashlibrary.Library_Name)
while True:
    print("1. Type 1 if you want to Display all the books of Library\n"
          "2. Type 2 if you want to Lend any books of Library\n"
          "3. Type 3 if you want to Return issued book of Library\n"
          "4. Type 4 if you want to Donate  any books to the Library\n")
    a=int(input())
    if a==1:
        yashlibrary.Displaye_Book()
        pass
    elif a==2:
        print("Please enter the Book name and Your name respectively.")
        b=input()
        c=input()
        yashlibrary.Lend_Book(b,c)
        pass
    elif a==3:
        print("Please enter the Book name and Your name respectively.")
        mk = input()
        lm = input()
        yashlibrary.Return_Book(mk,lm)
        pass
    elif a==4:
        print("Please enter the Book name and Your name respectively.")
        db = input()
        dn = input()
        yashlibrary.Add_Book(db,dn)
        pass
    else:
        print("You have entered somthing wrong !")
        continue
