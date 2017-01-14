class cat(object):
    """docstring for cat."""
    def __init__(self, colour, sound):
        super(cat, self).__init__()
        self.colour = colour
        self.sound = sound

    def meow(self):
        print self.sound * 15

pablo = cat('Ginger', 'HRAOW')

print pablo.colour
pablo.meow()

holly = cat('Tabby', 'wack')

print holly.colour
print holly.sound
holly.meow()

pablo.sound = "WHWOUK"

pablo.meow()
