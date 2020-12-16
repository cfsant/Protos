import sys, os

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize CLIENT on base path {path}...\n')

    nodemodules = path.replace('/Client/', '')
    print(nodemodules)

main()