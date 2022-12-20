from random import randint


def move(card_):
    if card_.rect.y == 575:
        # If card was not deployed on the field yet
        return None
    in_right_part = card_.rect.x >= 400
    in_left_part = not in_right_part
    if hasattr(card_, "acceleration"):
        # Keeping on movement if acceleration was accured
        card_.rect.x += card_.acceleration
        return card_.rect.x
    if in_left_part:
        card_.acceleration = 1
    elif in_right_part:
        card_.acceleration = -1
    card_.rect.x += card_.acceleration


def damage_adjacent(some_card, card_list: list):
    for card in card_list:
        if all([abs(some_card.rect.y - card.rect.y) < 80, card.rect.y != 575, card is not some_card, not card.damaged]):
            some_card.damage(card)
            print(f"Type of card : {type(card)}, "
                  f"Strt pos: {card.pos}, Curr Pos: {card.rect.x, card.rect.y}"
                  f"Card's health: {card.health}", sep='\n', end='\n\n')
            print(f"Type of some card : {type(some_card)}, "
                  f"Strt pos: {some_card.pos}, Curr Pos: {some_card.rect.x, some_card.rect.y}"
                  f"Some Card's health: {some_card.health}", sep='\n', end='\n\n')


if __name__ == "__main__":
    pass
