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
    pc_cv = 0
    pvl = list()

    print('-' * 23, 'Карты диллера', '-' * 23)
    for x in zip(*dlr.get_pl_cards()):
        print(*x)

    print('-' * 24, 'Ваши карты', '-' * 25)
    for x in zip(*plr.get_pl_cards()):
        print(*x)

    if sum(plr.get_cards_value()) == p_end_score \
            and dlr.get_cards_value()[0] < 10:
        rst = f'Блэкджек!\nВы выиграли!\nУ вас {sum(plr.get_cards_value())}' \
            f' очков.'

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
            rst = 'Вы закончили игру с результатом ничья.'

    sp = 'n'
    if plr.get_cards_value()[0] == plr.get_cards_value()[1]:
        while True:
            sp = input('Разбить пару (сплит)? y/n\n>>> ')
            try:
                if sp != 'y' and sp != 'n':
                    raise ValueError('Неверная команда.')
                else:
                    break
            except ValueError as v_err:
                print(v_err)

    if sp == 'n':
        while True:
            if pl_cv == p_end_score:
                print(f'Блэкджек!\nКоличество очков: {pl_cv}.')
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
    else:
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
                        while True:
                            sp = input('Разбить пару (сплит)? y/n\n>>> ')
                            try:
                                if sp != 'y' and sp != 'n':
                                    raise ValueError('Неверная команда.')
                                else:
                                    break
                            except ValueError as v_err:
                                print(v_err)
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
                    print(f'Блэкджек!\nКоличество очков: {pc_cv}.')
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
                        print(f'Блэкджек!\nКоличество очков: {pc_cv}.')
                        break
                    elif pc_cv > p_end_score:
                        print(f'Перебор.\nКоличество очков: {pc_cv}.')
                        break

                elif gq == 2:
                    print(f'Количество очков: {pc_cv}.')
                    break

            pvl.append(pc_cv)

    print('-' * 23, 'Карты диллера', '-' * 23)
    while dl_cv < d_end_score:
        dlr.cds.append(DeckOfCards(cards, card_symbol))
        dlr.cdl.append([_ for _ in dlr.cds[len(dlr.cds) - 1].get_card()])
        dlr.cdv.append(dlr.cds[len(dlr.cds) - 1].get_value())

        dl_cv_ct = tuple(x for x in dlr.get_cards_value() if x != 11) \
            + tuple(1 for x in dlr.get_cards_value() if x == 11)

        if dl_cv < p_end_score:
            dl_cv = sum(dlr.get_cards_value())
        else:
            dl_cv = sum(dl_cv_ct)

        if dl_cv >= d_end_score:
            for x in zip(*dlr.get_pl_cards()):
                print(*x)

            print(f'Количество очков у диллера: {dl_cv}.')

    print('-' * 23, 'Игра окончена', '-' * 23)

    if not pc_cv:
        # if pl_cv <= p_end_score < dl_cv:
        #     rst = 'Вы выиграли!'
        # elif pl_cv == p_end_score > dl_cv:
        #     rst = 'Вы выиграли!'
        # elif dl_cv < p_end_score > pl_cv > dl_cv:
        #     rst = 'Вы выиграли!'
        # elif pl_cv > p_end_score >= dl_cv:
        #     rst = 'Выиграл диллер'
        # elif pl_cv < p_end_score == dl_cv:
        #     rst = 'Выиграл диллер'
        # elif pl_cv < p_end_score > dl_cv > pl_cv:
        #     rst = 'Выиграл диллер'
        # elif pl_cv == p_end_score == dl_cv:
        #     rst = 'Ничья'
        # elif pl_cv > p_end_score < dl_cv:
        #     rst = 'Ничья'
        # else:
        #     rst = 'Ничья'
        if pl_cv <= p_end_score < dl_cv:
            rst = 1
        elif pl_cv == p_end_score > dl_cv:
            rst = 1
        elif dl_cv < p_end_score > pl_cv > dl_cv:
            rst = 1
        elif pl_cv > p_end_score >= dl_cv:
            rst = 2
        elif pl_cv < p_end_score == dl_cv:
            rst = 2
        elif pl_cv < p_end_score > dl_cv > pl_cv:
            rst = 2
        elif pl_cv == p_end_score == dl_cv:
            rst = 3
        elif pl_cv > p_end_score < dl_cv:
            rst = 3
        else:
            rst = 3
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

        rst = f'Пар выиграло: {win}\nПар проиграло: {loss}\nНичья: {tie}'
    
    return rst


if __name__ == '__main__':
    end_game = None
    card_symbol = {
        'spades': '\033[0;30;47m' + chr(9824) + '\033[0m',
        'diamonds': '\033[0;31;47m' + chr(9830) + '\033[0m',
        'hearts': '\033[0;31;47m' + chr(9829) + '\033[0m',
        'clubs': '\033[0;30;47m' + chr(9827) + '\033[0m',
    }

    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    while True:
        try:
            money = int(input('Укажите сумму денег с которой хотите начать'
                              ' игру:\n>>> '))
        except ValueError:
            print('Некорректно указана сумма денег.')
            continue
        break

    while end_game != 'n':
        player = Player([DeckOfCards(cards, card_symbol),
                         DeckOfCards(cards, card_symbol)])

        dealer = Player([DeckOfCards(cards, card_symbol)])
        
        try:
            bet = int(input('Сделайте ставку:\n>>> '))
        except ValueError:
            print('Неверно указана ствака (кол-во денег).')
            continue

        g = game(player, dealer)
        print(g)
        if g == 1:
            money += bet * 1.5
        elif g == 2:
            money -= bet
        elif g == 3:
            pass

        print(f'Ваш баланс: {money}')

        while True:
            end_game = input('Продолжить игру? (y/n):\n>>> ')
            try:
                if end_game != 'y' and end_game != 'n':
                    raise ValueError('Неверная команда.')
                else:
                    break
            except ValueError as v_err:
                print(v_err)
