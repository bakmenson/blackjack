from random import choice


class DeckOfCards:
    """Класс описывает колоду карт
         Args:
            card - словарь, key - название карты, value - значение
            symbol- словарь, key - название масти, value - символ и цвет

    """
    def __init__(self, card, symbol):
        self._card = card
        self._symbol = symbol
        self._cd_name = choice([_ for _ in self._card.items()])
        self._cd_symbol = choice([_ for _ in self._symbol.values()])

    def get_card(self):
        """Метод возвращает случайно выбранную карту"""
        return [chr(9484) + (chr(9472) * 9) + chr(9488),
                chr(9474) + ('\033[0;30;47m' + '{:<2}'.format(self._cd_name[0])
                             + '\033[0m')
                + (('\033[0;30;47m' + ' ' + '\033[0m') * 7) + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 9)
                + chr(9474),

                chr(9474) + (('\033[0;30;47m' + ' ' + '\033[0m') * 4)
                + f"{self._cd_symbol}" + (
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
        """Метод возвращает значение случайно выбранной карты"""
        return self._cd_name[1]


class Player:
    """Класс описывает игрока
         Args:
            card_list - список розданных карт игроку
    """
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
        """Метод возвращает полученные карты"""
        return self.cdl

    def get_cards_value(self):
        """Метод возвращает значение полученных карт"""
        return self.cdv


def title(name, start, end):
    print('-' * start, name, '-' * end)


def print_cards(player_cards):
    """Функция отрисовывает карты игроков"""
    for x in zip(*player_cards.get_pl_cards()):
        print(*x)


def add_card(plr):
    """
        Функция добовляет (раздает) карту игрокам и возвращает ее
        заначение
    """
    plr.cds.append(DeckOfCards(cards, card_symbol))
    plr.cdl.append([_ for _ in plr.cds[len(plr.cds) - 1].get_card()])
    plr.cdv.append(plr.cds[len(plr.cds) - 1].get_value())

    pl_cv_ct = tuple(x for x in plr.get_cards_value() if x != 11) \
        + tuple(1 for x in plr.get_cards_value() if x == 11)

    plr_cdv = sum(plr.get_cards_value())

    if plr_cdv > 21:
        plr_cdv = sum(pl_cv_ct)

    return plr_cdv


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

    # указывает сумму с которой начинаем игру
    while True:
        try:
            money = float(input('Укажите сумму денег с которой хотите начать'
                                ' игру:\n>>> '))
        except ValueError:
            print('Некорректно указана сумма денег.')
            continue

        try:
            if money == 0:
                raise ValueError('Вы не можете начать игру без денег.')
        except ValueError as v_err:
            print(v_err)
            continue

        break

    # цикл отвечает за процесс игры
    while end_game != 'n':

        # создаем игрока
        player = Player([DeckOfCards(cards, card_symbol),
                         DeckOfCards(cards, card_symbol)])

        # создаем диллера
        dealer = Player([DeckOfCards(cards, card_symbol)])

        # очки, которые нужно набрать, диллер обязан набирать минимум 17
        p_end_score, d_end_score = 21, 17

        # текущее кол-во очков диллера
        dl_cv = 0

        # список для хранения очков игрока после сплита
        pvl = list()

        # переменная для страховки
        insurance = 0

        bl = None

        # если у игрока после раздачи 2 туза (сумма превышает 21), то
        # значение туза меняется с 11 на 1
        cv_ct = tuple(x for x in player.get_cards_value() if x != 11) \
            + tuple(1 for x in player.get_cards_value() if x == 11)

        pl_cv = sum(player.get_cards_value())

        if pl_cv > p_end_score:
            pl_cv = sum(cv_ct)

        # ставка на партию
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

        # вычитаем ставку из денег
        money -= bet

        # выводим карты игроков после раздачи
        title('Карты диллера', 23, 23)
        print_cards(dealer)
        title('Ваши карты', 24, 25)
        print_cards(player)

        # если у игрока блэкджек, а карта диллера значением менее 10,
        # то игрок выигрывает
        if sum(player.get_cards_value()) == p_end_score \
                and dealer.get_cards_value()[0] < 10:
            bl = True

        # если у игрока блэкджек, а у диллера туз, игроку предлогается
        # закончить игру ничьей или продолжить
        elif sum(player.get_cards_value()) == p_end_score \
                and dealer.get_cards_value()[0] == 11:
            while True:
                end_q = input('У диллера первая карта туз, а у вас блэкджек,'
                              ' вы можете закончить игру\nс результатом ничья'
                              ' или продолжить игру:\nПродолжить игру (y/n)?'
                              '\n>>> ')
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
                money += bet

        # если у игрока менее 21, а у диллера туз, игроку предлогается
        # сделать страховку
        elif sum(player.get_cards_value()) < p_end_score \
                and dealer.get_cards_value()[0] == 11 and money - bet / 2 >= 0:
            while True:
                insurance_q = input('У диллера первая карта туз, вы'
                                    ' можете сделать страховую ставку,\nравную'
                                    ' половине первоначальной. В случае, если'
                                    ' у дилера\nбудет блэкджек, то игрок'
                                    ' проигрывает свою основную игровую\n'
                                    'ставку, но выигрывает страховочную в'
                                    ' размере 2 к 1. y/n\n>>> ')
                try:
                    if insurance_q != 'y' and insurance_q != 'n':
                        raise ValueError('Неверная команда.')
                    elif insurance_q == 'y':
                        insurance = bet / 2
                        break
                    else:
                        break
                except ValueError as v_err:
                    print(v_err)
                    continue

        # если у игрока после раздачи карт, значение обоих карт равны
        # игроку предлогается разбить пару
        sp = 'n'
        if player.get_cards_value()[0] == player.get_cards_value()[1] \
                and money - bet >= 0:
            while True:
                sp = input('Разбить пару (сплит)? y/n\n>>> ')
                try:
                    if sp != 'y' and sp != 'n':
                        raise ValueError('Неверная команда.')
                    elif sp == 'y':
                        # разбиваем пару карт и делаем еще ставку
                        money -= bet
                        break
                    else:
                        break
                except ValueError as v_err:
                    print(v_err)

        # если разбиваем пару
        if sp == 'y':

            # список содержит разбитые пары карт
            pl = [player.__class__([player.cds[0]]),
                  player.__class__([player.cds[1]])]

            # проходим по списку разбитых пар карт и добовляем карты
            for pc in pl:
                while True:
                    if len(pc.cds) <= 2:
                        pl_cv = add_card(pc)
                        print_cards(pc)

                        if pl_cv == p_end_score:
                            break

                        # если после добавления карт значение карт равно
                        # снова предлогается разбить пары
                        if pc.get_cards_value()[0] == pc.get_cards_value()[1] \
                                and money - bet >= 0:
                            while True:
                                sp = input('Разбить пару (сплит)?'
                                           ' y/n\n>>> ')
                                try:
                                    if sp != 'y' and sp != 'n':
                                        raise ValueError('Неверная команда.')
                                    elif sp == 'y':
                                        # разбиваем пару карт и
                                        # делаем еще ставку
                                        money -= bet
                                        break
                                    else:
                                        break
                                except ValueError as v_err:
                                    print(v_err)
                        else:
                            break

                        # если разбиваем пару
                        if sp == 'y':
                            # добавленую карту добавляем в список
                            # разбитых пар карт
                            pl.append(player.__class__([pc.cds[1]]))

                            # добавленую карту удаляем (разбиваем пару)
                            pc.cds.remove(pc.cds[-1])
                            pc.cdl.remove(pc.cdl[-1])
                            pc.cdv.remove(pc.cdv[-1])
                        else:
                            break
                    else:
                        break

                while True:
                    if len(pc.cds) == 7:
                        print(f'Количество очков: {pl_cv}.')
                        break

                    # если сумма значения двух карт ровна 21, то переходим к
                    # другой паре карт
                    if pl_cv == p_end_score:
                        print(f'Отлично!\nКоличество очков: {pl_cv}.')
                        break

                    try:
                        gq = int(input('1. Взять ещё карту.\n2. Хватит\n>>> '))
                    except ValueError:
                        print('Неверная команда.')
                        continue

                    if gq == 1:
                        # присваиваем функция добавления карт переменной
                        pl_cv = add_card(pc)

                        print_cards(pc)

                        if pl_cv == p_end_score:
                            print(f'Отлично!\nКоличество очков: {pl_cv}.')
                            break
                        elif pl_cv > p_end_score:
                            print(f'Перебор.\nКоличество очков: {pl_cv}.')
                            break

                    elif gq == 2:
                        print(f'Количество очков: {pl_cv}.')
                        break

                # добавляем суммы разбитых пар карт в список
                pvl.append(pl_cv)

        # если не разбиваем пару карт
        if sp == 'n' and not pvl and not bl:
            # счетчик для удвоения и утроения стваки
            # делать удвоения и утроения стваки можно по одному разу
            db_count = 0

            # присваиваем переменной для удвоения и утроения ствавок
            # значение ставки
            db_bet = bet

            while True:
                if len(player.cds) == 7:
                    if db_count:
                        bet = db_bet
                    print(f'Количество очков: {pl_cv}.')
                    break

                if pl_cv == p_end_score:
                    if db_count:
                        bet = db_bet
                    print(f'Отлично!\nКоличество очков: {pl_cv}.')
                    break
                elif pl_cv > p_end_score:
                    if db_count:
                        bet = db_bet
                    print(f'Перебор.\nКоличество очков: {pl_cv}.')
                    break

                if pl_cv >= 10 and db_count == 0 and money - bet >= 0:
                    try:
                        gq = int(input('1. Взять ещё карту.\n2. Хватит\n'
                                       '3. Удвоить ставку.\n>>> '))
                    except ValueError:
                        print('Неверная команда.')
                        continue
                elif db_count == 1 and money - bet >= 0:
                    try:
                        gq = int(input('1. Взять ещё карту.\n2. Хватит\n'
                                       '3. Утроить ставку.\n>>> '))
                    except ValueError:
                        print('Неверная команда.')
                        continue
                else:
                    while True:
                        try:
                            gq = int(input('1. Взять ещё карту.'
                                           '\n2. Хватит.\n>>> '))
                        except ValueError:
                            print('Неверная команда.')
                            continue

                        try:
                            if gq > 2:
                                raise ValueError('Неверная команда.')
                        except ValueError as v_err:
                            print(v_err)
                            continue

                        break

                if gq == 1 or gq == 3:
                    # добавляем карту
                    pl_cv = add_card(player)

                    # выводим карты
                    print_cards(player)

                elif gq == 2:
                    if db_count:
                        bet = db_bet
                    print(f'Количество очков: {pl_cv}.')
                    break

                if gq == 3:
                    money -= bet
                    db_bet += bet
                    db_count += 1

                if db_count == 2:
                    bet = db_bet
                    print(f'Количество очков: {pl_cv}.')
                    break

        if not bl:
            title('Карты диллера', 23, 23)

            # код отвечает за работу с картами диллера
            while dl_cv < d_end_score and len(dealer.cds) < 7:
                dl_cv = add_card(dealer)

                if dl_cv >= d_end_score:
                    print_cards(dealer)
                    print(f'Количество очков у диллера: {dl_cv}.')

                if len(dealer.cds) == 7:
                    print_cards(dealer)
                    print(f'Количество очков у диллера: {dl_cv}.')

        title('Игра окончена', 23, 23)

        # выводим результат партии
        if not pvl:
            # если не было разбития пары
            if pl_cv == p_end_score < dl_cv \
                    and len(player.cds) == 2 and len(dealer.cds) == 2:
                money += bet * 1.5 - insurance
                print('Блэкджек!\nВы выиграли!')
            elif pl_cv <= p_end_score < dl_cv:
                money += bet * 1.5 - insurance
                print('Вы выиграли!')
            elif pl_cv == p_end_score > dl_cv and len(player.cds) == 2:
                money += bet * 1.5 - insurance
                print('Блэкджек!\nВы выиграли!')
            elif pl_cv <= p_end_score > dl_cv < pl_cv:
                money += bet * 1.5 - insurance
                print('Вы выиграли!')
            elif dl_cv < p_end_score > pl_cv > dl_cv:
                money += bet * 1.5 - insurance
                print('Вы выиграли!')
            elif pl_cv == p_end_score == dl_cv \
                    and len(dealer.cds) == 2 and len(player.cds) > 2:
                money += insurance * 2
                print('Выиграл диллер.\nУ диллер блэкджек.')
            elif pl_cv < p_end_score == dl_cv and len(dealer.cds) == 2:
                money += insurance * 2
                print('Выиграл диллер.\nУ диллер блэкджек.')
            elif pl_cv > p_end_score == dl_cv:
                money += insurance * 2
                print('Выиграл диллер.\nУ диллер блэкджек.')
            elif pl_cv > p_end_score > dl_cv:
                money -= insurance
                print('Выиграл диллер.')
            elif pl_cv < p_end_score == dl_cv:
                money -= insurance
                print('Выиграл диллер.')
            elif pl_cv < p_end_score > dl_cv > pl_cv:
                money -= insurance
                print('Выиграл диллер.')
            elif pl_cv == p_end_score == dl_cv \
                    and len(dealer.cds) == len(player.cds):
                money += bet - insurance
                print('Ничья')
            elif pl_cv == p_end_score == dl_cv:
                money += bet - insurance
                print('Ничья')
            elif pl_cv > p_end_score < dl_cv:
                money += bet - insurance
                print('Ничья')
            else:
                money += bet - insurance
                print('Ничья')
        else:
            # если было разбитие пары карт
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
                money += (win * bet) * 1.5 - insurance
            if tie:
                money += tie * bet - insurance
            if loss:
                money -= insurance

        # проверяем остаток средств, если не осталось, конец игры
        if not money:
            print('У вас закончились деньги.')
            break
        else:
            print(f'Ваш баланс: {money}')

            # предлогаем продолжить игру
            while True:
                end_game = input('Продолжить игру? (y/n):\n>>> ')
                try:
                    if end_game != 'y' and end_game != 'n':
                        raise ValueError('Неверная команда.')
                    else:
                        break
                except ValueError as v_err:
                    print(v_err)
