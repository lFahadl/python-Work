class Game:
 
    def __init__(self, level=None):
        self.level = level if level else 0
 
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value
 
 
games = [Game(), Game(10), Game(-10), Game(120)]
for game in games:
    print(game.level)
