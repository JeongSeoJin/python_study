# -*- coding : uft-8 -*-

class head():
    def __init__(self, head_type):
        self.head_type = head_type

class about_snake(head):
    def __init__(self):
        print("이 뱀의 머리는 {}이예요".format(self.head_type))

snake = about_snake("삼각형")
