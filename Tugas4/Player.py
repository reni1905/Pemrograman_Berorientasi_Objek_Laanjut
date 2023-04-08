class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
class Game:
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def daftar_player(self):
        for player in self.player:
            print(player.name, player.number)

player1 = Player("Ronaldo", 7)
player2 = Player("Neymar", 9)

game =  Game("Mobile Legend", [player1, player2])
game.daftar_player()