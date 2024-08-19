class word:
    def __init__(self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer

    def show_question(self):

        print("="*30,"\n신조어 퀴즈")
        print("="*30)
        print("{}을/를 맞추어 보세요??".format(self.word))
        print("1, " + "{}".format(self.ex1))
        print("2, " + "{}".format(self.ex2))

    def check_answer(self, user_input):
        if user_input == self.answer:
            print("맞았어요!")
        else:
            print("틀렸어요!")
            print("정답은 {}이예요.".format(self.answer))

Word = word("얼죽아", "얼어 죽어도 아이스 아메리카노", "얼어 죽어도 아기피부", 1)
Word.show_question()#In here, you have to make sure that you write text which is you made(변수)
Word.check_answer(int(input("=>  ")))