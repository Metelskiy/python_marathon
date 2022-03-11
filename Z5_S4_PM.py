class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False
    def play(self, word):
        self.word=word
        if (self.words==[]):
            self.words.append(word)
            return self.words
       # print(self.words)
        if(self.words[-1][-1]==word[0] and (word not in self.words)):
            self.words.append(word)
        else: self.game_over=True
        if(self.game_over==True):
            return "game over"
        else: return self.words
    def restart(self):
        self.words=[]
        self.game_over=False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('over'))
print(my_gallows.game_over)
my_gallows.restart()
my_gallows.play("new word")
print(my_gallows.game_over)