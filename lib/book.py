#!/usr/bin/env python3

class TestBook:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count=page_count
        self.page_count = None
    @decorater
    def title(self):
        pass
    @decorater
    def page_count(self):
     
        pass 
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self.turn_page = value
        else:
            print("page_count must be an intege") 
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  
book= TestBook("And Then There Were None", 272)
print(book.title)
print(book.page_count)
    
        