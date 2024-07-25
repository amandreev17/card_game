import random
import time

class Card:
    
    point_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '8': 8, '9': 9, 'Дама': 10, 'Валет': 10, 'Король': 10, 'Туз': 11}
    
    def __init__(self, nominal, card_suit):
        self.nominal = nominal
        self.card_suit = card_suit
        self.gives_points = self.point_dict.get(nominal)
    
    def __str__(self):
        return f"{self.nominal} {self.card_suit}"


class Deck_of_cards:
    def __init__(self):
        self.deck = []
        self.generate_deck()
    
    def generate_deck(self):
        self.deck.clear()
        for nominal in ['2', '3', '4', '5', '6', '7', '8', '9', 'Дама', 'Король', 'Валет', 'Туз']:
            for card_suit in ['Черви', 'Буби', 'Крести', 'Пики']:
                self.deck.append(Card(nominal, card_suit))
        random.shuffle(self.deck)
    
    def get_card(self):
        return self.deck.pop()
    
    def __str__(self):
        return '; '.join([card.__str__() for card in self.deck])
class Gamer:
    def __init__(self):
        self.cards = []
        self.score = 0
    
    def getCardStr(self):
        return ','.join(card.__str__() for card in self.cards)
    
    def addCard(self, card):
        self.cards.append(card)
        
        if card.gives_points == 11 and self.score > 10:
            self.score += 1
        else:
            self.score += card.gives_points
    
    
    def last_card(self):
        return self.cards[-1]

class Game:
    def __init__(self):
        self.bot = Gamer()
        self.gamer = Gamer()
        self.deck = Deck_of_cards()
    
    def Start(self):
        
        self.gamer.addCard(self.deck.get_card())
        self.gamer.addCard(self.deck.get_card())
        
        while True:
            print(f"Ваши каты {self.gamer.getCardStr()} \nУ вас {self.gamer.score} очков")
            if self.gamer.score > 21:
                print(f'Перебор вы набрали {self.gamer.score} очков')
                break
            
            choice = input('будете брать карту? y/n\n')
            if choice == 'y':
                self.gamer.addCard(self.deck.get_card())
            else:
                while self.bot.score < 19:
                    self.bot.addCard(self.deck.get_card())
                    print(f'Крупье берёт карты {self.bot.last_card()}, у него {self.bot.score}')
                    time.sleep(1)
                
                status = 'Вы победили'
                if self.gamer.score < self.bot.score <= 21:
                    status = 'Вы проиграли'
                elif self.gamer.score == self.bot.score:
                    status = 'ничья'
                
                print(f'{status}, у вас {self.gamer.score} очков, у крупье {self.bot.score} очков')
game = Game()
game.Start()

