from random import choice


class DeckOfCards:
    def __init__(self, card, symbol):
        self._card = card
        self._symbol = symbol
        self._cd_name = choice([_ for _ in self._card.items()])
        self._cd_sbl = choice([_ for _ in self._symbol.values()])

    def get_card(self):
        return [chr(9484) + (chr(9472) * 9) + chr(9488),
                chr(9474) + ('\033[0;30;47m' + '{:<2}'.format(self._cd_name[0])
                             + '\033[0m')
                + (('\033[0;30;47m' + ' ' + '\033[0m') * 7) + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 4)
                + f"{self._cd_sbl}" + (
                        ('\033[0;30;47m' + ' ' + '\033[0m') * 4) + chr(9474),
                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 7)
                + ('\033[0;30;47m' + '{:>2}'.format(
                    self._cd_name[0]) + '\033[0m') + chr(9474),

                chr(9492) + (chr(9472) * 9) + chr(9496)]
    
    def get_value(self):
        return self._cd_name[1]


class Player:
    def __init__(self, card_list):
        self.cds = card_list

        if len(self.cds) >= 2:
            self.cdl = [[_ for _ in self.cds[0].get_card()],
                    [_ for _ in self.cds[1].get_card()]]

            self.cdv = [self.cds[0].get_value(), self.cds[1].get_value()]
        else:
            self.cdl = [[_ for _ in self.cds[0].get_card()]]
            self.cdv = [self.cds[0].get_value()]

    def get_pl_cards(self):
        return self.cdl

    def get_cards_value(self):
        return self.cdv


def game(plr, dlr):
    p_end_score, d_end_score = 21, 17
    pl_cv, dl_cv = sum(plr.get_cards_value()), 0

    print('-' * 15, 'Карты диллера', '-' * 15)
    for x in zip(*dlr.get_pl_cards()):
        print(*x)

    if dlr.get_cards_value()[0] == 11:
        print(dlr.get_cards_value())

    print('-' * 15, 'Ваши карты', '-' * 15)
    for x in zip(*plr.get_pl_cards()):
        print(*x)

    if sum(plr.get_cards_value()) == p_end_score \
            and dlr.get_cards_value()[0] < 10:
        return f'Блэкджек!\nУ вас {sum(plr.get_cards_value())} очков.'
    
    elif sum(plr.get_cards_value()) == p_end_score \
            and dlr.get_cards_value()[0] == 11:
        while True:
            end_q = input('У диллера первая карта туз, а у вас блэкджек, вы'
                          ' можите закончить игру\nс результатом ничья или'
                          ' продолжить игру:\nПродолжить игру (y/n)?\n>>> ')
            try:
                if end_q != 'y' and end_q != 'n':
                    raise ValueError('Неверная команда.')
                else:
                    break
            except ValueError as v_err:
                print(v_err)
                continue
        
        if end_q == 'n':
            return 'Вы закончили игру с результатом ничья.'
    
    while True:
        try:
            gq = int(input('1. Взять ещё карту.\n2. Хватит\n>>> '))
        except ValueError:
            print('Неверная команда.')
            continue

        if gq == 1:
            plr.cds.append(DeckOfCards(cards, card_symbol))
            plr.cdl.append([_ for _ in plr.cds[len(plr.cds) - 1].get_card()])
            plr.cdv.append(plr.cds[len(plr.cds) - 1].get_value())
            pl_cv = sum(plr.get_cards_value())
            
            for x in zip(*plr.get_pl_cards()):
                print(*x)
            
        elif gq == 2:
            if pl_cv == p_end_score:
                print(f'Блэкджек!\nКоличество очков: {pl_cv}.')
                break
            elif pl_cv > p_end_score:
                print(f'Перебор.\nКоличество очков: {pl_cv}.')
                break
            else:
                print(f'Количество очков: {pl_cv}.')
                break
    
    print('-' * 15, 'Карты диллера', '-' * 15)
    while dl_cv < d_end_score:
        dlr.cds.append(DeckOfCards(cards, card_symbol))
        dlr.cdl.append([_ for _ in dlr.cds[len(dlr.cds) - 1].get_card()])
        dlr.cdv.append(dlr.cds[len(dlr.cds) - 1].get_value())
        dl_cv = sum(dlr.get_cards_value())

        if dl_cv >= d_end_score:
            for x in zip(*dlr.get_pl_cards()):
                print(*x)

            print(f'Количество очков у диллера: {dl_cv}.')
    
    if pl_cv <= p_end_score and dl_cv > p_end_score:
        return 'Вы выиграли!'
    elif pl_cv == p_end_score and dl_cv < p_end_score:
        return 'Вы выиграли!'
    elif pl_cv < p_end_score and dl_cv < p_end_score and pl_cv > dl_cv:
        return 'Вы выиграли!'
    elif pl_cv > p_end_score and dl_cv <= p_end_score:
        return 'Выиграл диллер'
    elif pl_cv < p_end_score and dl_cv == p_end_score:
        return 'Выиграл диллер'
    elif pl_cv < p_end_score and dl_cv < p_end_score and pl_cv < dl_cv:
        return 'Выиграл диллер'
    elif pl_cv == p_end_score and dl_cv == p_end_score:
        return 'Ничья'
    elif pl_cv > p_end_score and dl_cv > p_end_score:
        return 'Ничья'
    else:
        return 'Ничья'


if __name__ == '__main__':
    card_symbol = {
        'spades': '\033[0;30;47m' + chr(9824) + '\033[0m',
        'diamonds': '\033[0;31;47m' + chr(9830) + '\033[0m',
        'hearts': '\033[0;31;47m' + chr(9829) + '\033[0m',
        'clubs': '\033[0;30;47m' + chr(9827) + '\033[0m',
    }

    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    player = Player([DeckOfCards(cards, card_symbol),
                 DeckOfCards(cards, card_symbol)])

    dealer = Player([DeckOfCards(cards, card_symbol)])

    print(game(player, dealer))
