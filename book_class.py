class e_book():
    def __init__(self,title,author,number_of_pages):
       self.title = title
       self.author = author
       self.number_of_pages=number_of_pages
       self.page=1
       self.is_open=False
    def open_b(self):
        self.is_open=True
    def close_b(self):
        self.is_open=False
    def show_status(self):
        if self.is_open==True:
            print(f"title: {self.title}\nauthor: {self.author}\nnumber of pages: {self.number_of_pages}\ncurrent page: {self.page}")
        else:
            print(f"title: {self.title}\nauthor: {self.author}\nnumber of pages: {self.number_of_pages}\ncurrent page: book is closed, but last was: {self.page}")
    def read_page(self):
        if  self.is_open==True:
            if self.page<self.number_of_pages : self.page+=1
        else: print("book is closed")
    def last_page(self):
        if  self.is_open==True:
            if self.page>1: self.page-=1
        else: print("book is closed")
