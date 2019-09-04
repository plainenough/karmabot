def roll(**kwargs: dict) -> str:
    """rolls a dice: roll d20 Optional value: confirm"""
    import random
    user = kwargs.get('user')
    channel = kwargs.get('channel')
    msg_text = kwargs.get('text')
    #  msg_text should be in this format. "roll d20 confirm"
    #  confirm is optional
    _commands = []
    msg = ''
    confirm = False
    for com in msg_text.split():
        if com == 'roll' or '':
            continue
        if com == "confirm":
            confirm = True
            continue
        _commands.append(com)
    for com in _commands:
        if 'd' not in com:
            continue
        upper = int(com.split('d')[1])
        msg += "\nYour {0} roll is {1}".format(com, random.randrange(1, upper+1))
        if confirm:
            msg += " with a confirmation of {0}".format(
                    random.randrange(1, upper+1))
    return msg


if __name__ == '__main__':
    # standalone test
    user, channel, text = 'bob', '#general', 'roll d20 d10 d12 confirm'
    kwargs = dict(user=user,
                  channel=channel,
                  text=text)
    output = roll(**kwargs)
    print(output)
