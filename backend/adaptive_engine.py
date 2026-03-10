def update_ability(current_ability, is_correct):

    if is_correct:
        current_ability += 0.1
    else:
        current_ability -= 0.1

    if current_ability > 1:
        current_ability = 1

    if current_ability < 0.1:
        current_ability = 0.1

    return current_ability