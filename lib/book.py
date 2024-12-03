#!/usr/bin/env python3

class TestBook:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count=page_count
    @decorater
    def title(self):
        pass
    @decorater
    def page_count(self):
        pass    
book= TestBook("And Then There Were None", 272)
print(book.title)
print(book.page_count)
    
        