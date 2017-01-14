class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def hello_world(self):
        print "Hello World!"

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

thelyrics = ["When I get older", "Losing my hair"]

when_im_64 = Song(thelyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

when_im_64.sing_me_a_song()

for line in when_im_64.lyrics:
    print line
dog = Song(["Dog"])

dog.hello_world()
