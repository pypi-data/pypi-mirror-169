import os
import argparse
from svtter_config import config


parser = argparse.ArgumentParser(description='svtter config.')

parser.add_argument('cmd', help='command to run. zsh/vim/alias')

args = parser.parse_args()

if args.cmd == 'alias':
    if os.getenv('SHELL') == 'zsh':
        config_filepath = '~/.zshenv'
    else:
        config_filepath = '~/.profile'
    with open(config_filepath, 'w+') as f:
        f.write(config.zshenv)
elif args.cmd == 'zsh':
    with open('~/zsh_install.sh', 'w') as f:
        f.write(config.zsh_install)
elif args.cmd == 'vim':
    for cmd in config.vim:
        os.system(cmd)
else:
    print('NOT a valid cmd')
    import sys
    sys.exit(-1)
