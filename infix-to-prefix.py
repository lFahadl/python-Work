class Game:
    
    def __init__(self, *level):
        
        level = list(level)
        if not level:
            level.append(0)
        
        value = level[0]
        
        if type(value) != int:
            raise TypeError("The value of level must be of type int.")
    
        if value > 100:
            self._level = 100
        elif value < 0:
            self._level = 0
    
    @property  
    def level(self):
        return self._level
    
    @level.setter
    def level(self, val):
        
        if type(val) != int:
            raise TypeError("The value of level must be of type int.")
        
        if val > 100:
            self._level = 100
        elif val < 0:
            self._level = 0
    
    # @level.default
    # def level(self):
    #     self._level = 0
        

games = [Game(), Game(10), Game(-10), Game(120)]

for i in games:
    print(i)
    game = i
    print(game.level)
    del game

