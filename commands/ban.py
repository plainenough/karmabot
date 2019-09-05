def ban_user(**kwargs: dict) -> str:
    """ban_user will ban a user from giving or taking karma"""
    # kwargs will hold user, channel, text (from a Slack message object)
    # use them like this, or just delete these line:
    user = kwargs.get('user')
    channel = kwargs.get('channel')
    _payload = kwargs.get('text').strip()
    banned_users = _payload.translate({ord(i): None for i in '<>@'}).split()
    # removing the word ban from the baned user command.
    banned_users.remove('ban')
    if kwargs.get('test') == True:
        return 'User {0} is banned.\n'.format(banned_users[0])
    with open('data/BANNED', 'a') as banned_list:
        for new_user in banned_users:
            banned_list.write('{0}\n'.format(new_user))
    msg_text = ''
    for user in banned_users:
        msg_text += 'User {0} is banned.\n'.format(user)
    return msg_text


def unban_all(**kwargs: dict) -> str:
    """unban_all will lift existing bans for all users"""
    user = kwargs.get('user')
    channel = kwargs.get('channel')
    if kwargs.get('test') == True:
        return 'Cleared the ban list'
    with open('data/BANNED', 'w') as banned_list:
        banned_list.write('')
    msg_text = 'Cleared the ban list'
    return msg_text


def unban_user(**kwargs: dict) -> str:
    """unban_user will lift an existing user ban"""
    user = kwargs.get('user')
    channel = kwargs.get('channel')
    _payload = kwargs.get('text').strip()
    unbanned_users = _payload.translate({ord(i): None for i in '<>@'}).split()
    unbanned_users.remove('unban')
    if kwargs.get('test') == True:
        return 'User {0} is unbanned.\n'.format(unbanned_users[0])
    with open('data/BANNED', 'r') as banned_list:
        temp_list = banned_list.readlines()
    with open('data/BANNED', 'w') as banned_list:
        for line in temp_list:
            for user in unbanned_users:
                if line.strip('\n') != user:
                    banned_list.write(line)
    msg_text = ''
    for user in unbanned_users:
        msg_text += 'User {0} is unbanned.\n'.format(user)
    return msg_text


if __name__ == '__main__':
    print('RTFM')
