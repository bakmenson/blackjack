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


def game(plr, dlr, money):
    p_end_score, d_end_score = 21, 17
    pl_cv, dl_cv = sum(plr.get_cards_value()), 0
    pc_cv = 0
    pvl = list()

    while True:
        try:
            bet = float(input('Сделайте ставку:\n>>> '))
        except ValueError:
            print('Неверно указана ствака (кол-во денег).')
            continue

        try:
            if bet > money:
                raise ValueError('Сумма ставки превышает ваши средства.')
            else:
                break
        except ValueError as v_err:
            print(v_err)
            continue
    
    money -= bet

    print('-' * 23, 'Карты диллера', '-' * 23)
    for x in zip(*dlr.get_pl_cards()):
        print(*x)

    print('-' * 24, 'Ваши карты', '-' * 25)
    for x in zip(*plr.get_pl_cards()):
        print(*x)

    if sum(plr.get_cards_value()) == p_end_score \
            and dlr.get_cards_value()[0] < 10:
        money += bet * 1.5
        print('Блэкджек!\nВы выиграли!')
        return money

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
            print('Вы закончили игру с результатом ничья.')
            return None

    sp = 'n'
    if plr.get_cards_value()[0] == plr.get_cards_value()[1]:
        if money - bet >= 0:
            while True:
                sp = input('Разбить пару (сплит)? y/n\n>>> ')
                try:
                    if sp != 'y' and sp != 'n':
                        raise ValueError('Неверная команда.')
                    elif sp == 'y':
                        money -= bet
                        break
                    else:
                        break
                except ValueError as v_err:
                    print(v_err)
        else:
            pass

    if sp == 'y':
        pl = [plr.__class__([plr.cds[0]]), plr.__class__([plr.cds[1]])]

        for pc in pl:
            while True:
                if len(pc.cds) <= 2:
                    pc.cds.append(DeckOfCards(cards, card_symbol))
                    pc.cdl.append(
                        [_ for _ in pc.cds[len(pc.cds) - 1].get_card()]
                    )
                    pc.cdv.append(pc.cds[len(pc.cds) - 1].get_value())
                    
                    for x in zip(*pc.get_pl_cards()):
                        print(*x)

                    pc_cv = sum(pc.get_cards_value())

                    if pc_cv == p_end_score:
                        break

                    if pc.get_cards_value()[0] == pc.get_cards_value()[1]:
                        if money - bet >= 0:
                            while True:
                                sp = input('Разбить пару (сплит)? y/n\n>>> ')
                                try:
                                    if sp != 'y' and sp != 'n':
                                        raise ValueError('Неверная команда.')
                                    elif sp == 'y':
                                        money -= bet
                                        break
                                    else:
                                        break
                                except ValueError as v_err:
                                    print(v_err)
                        else:
                            sp == 'n'
                            break
                    else:
                        break

                    if sp == 'y':
                        pl.append(plr.__class__([pc.cds[1]]))
                        pc.cds.remove(pc.cds[-1])
                        pc.cdl.remove(pc.cdl[-1])
                        pc.cdv.remove(pc.cdv[-1])
                    else:
                        break
                else:
                    break

            while True:
                if pc_cv == p_end_score:
                    print(f'Отлично!\nКоличество очков: {pc_cv}.')
                    break

                try:
                    gq = int(input('1. Взять ещё карту.\n2. Хватит\n>>> '))
                except ValueError:
                    print('Неверная команда.')
                    continue

                if gq == 1:
                    pc.cds.append(DeckOfCards(cards, card_symbol))
                    pc.cdl.append([_ for _
                                   in pc.cds[len(pc.cds) - 1].get_card()])
                    pc.cdv.append(pc.cds[len(pc.cds) - 1].get_value())

                    pl_cv_ct = tuple(x for x in pc.get_cards_value()
                                     if x != 11) \
                        + tuple(1 for x in pc.get_cards_value()
                                if x == 11)

                    pc_cv = sum(pl_cv_ct)

                    for x in zip(*pc.get_pl_cards()):
                        print(*x)
                    
                    if pc_cv == p_end_score:
                        print(f'Отлично!\nКоличество очков: {pc_cv}.')
                        break
                    elif pc_cv > p_end_score:
                        print(f'Перебор.\nКоличество очков: {pc_cv}.')
                        break

                elif gq == 2:
                    print(f'Количество очков: {pc_cv}.')
                    break

            pvl.append(pc_cv)
    
    if sp == 'n':
        while True:
            if pl_cv == p_end_score:
                print(f'Отлично!\nКоличество очков: {pl_cv}.')
                break
            elif pl_cv > p_end_score:
                print(f'Перебор.\nКоличество очков: {pl_cv}.')
                break

            try:
                gq = int(input('1. Взять ещё карту.\n2. Хватит\n>>> '))
            except ValueError:
                print('Неверная команда.')
                continue

            if gq == 1:
                plr.cds.append(DeckOfCards(cards, card_symbol))
                plr.cdl.append(
                    [_ for _ in plr.cds[len(plr.cds) - 1].get_card()]
                )
                plr.cdv.append(plr.cds[len(plr.cds) - 1].get_value())

                pl_cv_ct = tuple(x for x in plr.get_cards_value() if x != 11) \
                    + tuple(1 for x in plr.get_cards_value() if x == 11)

                pl_cv = sum(plr.get_cards_value())

                if pl_cv > p_end_score:
                    pl_cv = sum(pl_cv_ct)

                for x in zip(*plr.get_pl_cards()):
                    print(*x)

            elif gq == 2:
                print(f'Количество очков: {pl_cv}.')
                break

    print('-' * 23, 'Карты диллера', '-' * 23)
    while dl_cv < d_end_score:
        dlr.cds.append(DeckOfCards(cards, card_symbol))
        dlr.cdl.append([_ for _ in dlr.cds[len(dlr.cds) - 1].get_card()])
        dlr.cdv.append(dlr.cds[len(dlr.cds) - 1].get_value())

        dl_cv_ct = tuple(x for x in dlr.get_cards_value() if x != 11) \
            + tuple(1 for x in dlr.get_cards_value() if x == 11)

        dl_cv = sum(dlr.get_cards_value())

        if dl_cv > p_end_score:
            dl_cv = sum(dl_cv_ct)

        if dl_cv >= d_end_score:
            for x in zip(*dlr.get_pl_cards()):
                print(*x)

            print(f'Количество очков у диллера: {dl_cv}.')

    print('-' * 23, 'Игра окончена', '-' * 23)

    if not pc_cv:
        if pl_cv == p_end_score < dl_cv \
                and len(plr.cds) == 2 and len(dlr.cds) == 2:
            print(2)
            money += bet * 1.5
            print('Блэкджек!\nВы выиграли!')
        elif pl_cv <= p_end_score < dl_cv:
            print(3)
            money += bet * 1.5
            print('Вы выиграли!')
        elif pl_cv == p_end_score > dl_cv and len(plr.cds) == 2:
            print(4)
            money += bet * 1.5
            print('Блэкджек!\nВы выиграли!')
        elif pl_cv <= p_end_score > dl_cv < pl_cv:
            print(4.1)
            money += bet * 1.5
            print('Вы выиграли!')
        elif dl_cv < p_end_score > pl_cv > dl_cv:
            print(5)
            money += bet * 1.5
            print('Вы выиграли!')
        elif pl_cv == p_end_score == dl_cv \
                and len(dlr.cds) == 2 and len(plr.cds) > 2:
            print(6)
            print('Выиграл диллер.\nУ диллер блэкджек.')
        elif pl_cv < p_end_score == dl_cv and len(dlr.cds) == 2:
            print(6.1)
            print('Выиграл диллер.\nУ диллер блэкджек.')
        elif pl_cv > p_end_score == dl_cv:
            print(7)
            print('Выиграл диллер.\nУ диллер блэкджек.')
        elif pl_cv > p_end_score > dl_cv:
            print(7.1)
            print('Выиграл диллер.')
        elif pl_cv < p_end_score == dl_cv:
            print(8)
            print('Выиграл диллер.')
        elif pl_cv < p_end_score > dl_cv > pl_cv:
            print(9)
            print('Выиграл диллер.')
        elif pl_cv == p_end_score == dl_cv and len(dlr.cds) == len(plr.cds):
            print(10)
            money += bet
            print('Ничья')
        elif pl_cv == p_end_score == dl_cv:
            print(11)
            money += bet
            print('Ничья')
        elif pl_cv > p_end_score < dl_cv:
            print(12)
            money += bet
            print('Ничья')
        else:
            print(13)
            money += bet
            print('Ничья')
    else:
        win, loss, tie = 0, 0, 0
        for x in pvl:
            if x <= p_end_score < dl_cv:
                win += 1
            elif x == p_end_score > dl_cv:
                win += 1
            elif x < p_end_score > x > dl_cv:
                win += 1
            elif x > p_end_score >= dl_cv:
                loss += 1
            elif x < p_end_score == dl_cv:
                loss += 1
            elif x < p_end_score > dl_cv > x:
                loss += 1
            elif x == p_end_score == dl_cv:
                tie += 1
            elif x > p_end_score < dl_cv:
                tie += 1
            else:
                tie += 1

        print(f'Пар выиграло: {win}\nПар проиграло: {loss}\nНичья: {tie}')
        if win:
            money += (win * bet) * 1.5
        if tie:
            money += tie * bet
    
    return money


if __name__ == '__main__':
    end_game = None
    card_symbol = {
        'spades': '\033[0;30;47m' + chr(9824) + '\033[0m',
        'diamonds': '\033[0;31;47m' + chr(9830) + '\033[0m',
        'hearts': '\033[0;31;47m' + chr(9829) + '\033[0m',
        'clubs': '\033[0;30;47m' + chr(9827) + '\033[0m',
    }

    # cards = {'10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    while True:
        try:
            money = float(input('Укажите сумму денег с которой хотите начать'
                                ' игру:\n>>> '))
        except ValueError:
            print('Некорректно указана сумма денег.')
            continue

        try:
            if money == 0:
                raise ValueError('Вы не можите начать игру без денег.')
        except ValueError as v_err:
            print(v_err)
            continue

        break

    while end_game != 'n':
        player = Player([DeckOfCards(cards, card_symbol),
                         DeckOfCards(cards, card_symbol)])

        dealer = Player([DeckOfCards(cards, card_symbol)])
        
        bl_game = game(player, dealer, money)

        money = bl_game

        if not bl_game:
            print('У вас закончились деньги.')
            break
        else:
            print(f'Ваш баланс: {bl_game}')

        while True:
            end_game = input('Продолжить игру? (y/n):\n>>> ')
            try:
                if end_game != 'y' and end_game != 'n':
                    raise ValueError('Неверная команда.')
                else:
                    break
            except ValueError as v_err:
                print(v_err)
