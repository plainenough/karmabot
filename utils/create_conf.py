#!/usr/bin/python3
import yaml

TEMPLATE = '''\
'BOTNAME': 'karmabot'
'ADMINS':
  - 'UEMN5QPLM'
'ADMIN_COMMANDS':
  'top_karma': 'top_karma'
  'ban': 'ban_user'
  'unban': 'unban_user'
  'unbanall': 'unban_all'
'USER_COMMANDS':
  'help': 'create_commands_table'
  'karma': 'get_karma'
'TEXT_FILTER_REPLIES':
  'cheers': ':beers:'
  'braces': '`SyntaxError: not a chance`'
'''


def create_config():
    with open('config.yaml', 'w') as config_file:
        for line in TEMPLATE:
            config_file.write(line)

if __name__ == '__main__':
    try: 
        with open('config.yaml', 'r') as config:
            yaml.load(config.read())
            print("Config is valid yaml")
    except FileNotFoundError:
        print("Config doesn't exist: Creating config")
        create_config()
    except yaml.scanner.ScannerError as e: 
        print(e)
        print("Config invalid check your config")
    except: 
        print("Unknown error: check permissions")
