import random

class Die: 
    def __init__(self, sides=6):
        self.sides = sides
        random.seed(0)

    def roll(self):
        return random.randint(1, self.sides)
    
class Player: 
    def __init__(self, name):
        self.name = name
        self.score = 0 
    
    def add_score(self, points):
        self.score += points 
    
    def reset_turn(self):
        return 0 
    
class Game: 
    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player 2")
        self.die = Die()
        self.current_turn = self.player1
    
    def play_turn(self):
        turn_total = 0
        while True: 
            roll = self.die.roll()
            print(f"{self.current_turn.name} rolled: {roll}")
            if roll == 1:
                print(f"Sorry, {self.current_turn.name}, you lose your turn with no points.")
                break
            else:
                turn_total += roll 
                print(f"Turn total: {turn_total}, Total schoe: {self.current_turn.score}")
            choice = input(f"{self.current_turn.name}, would you like to (r)oll or (h)old?")
            if choice.lower() == 'h':
                self.current_turn.add_score(turn_total)
                print(f"{self.current_turn.name}'s total score is now: {self.current_turn.score}")
                break 

    def check_winner(self):
        if self.player1.score >= 100:
            print(f"{self.player1.name} wins!")
            return True
        elif self.player2.score >= 100:
            print(f"{self.player2.name} wins!")
            return True
        return False 
    
    def start_game(self):
        while True:
            self.play_turn()
            if self.check_winner():
                break
            self.current_turn = self.player2 if self.current_turn == self.player1 else self.player1 

if __name__ == "__main__":
    game = Game()
    game.start_game()
    pass
    
