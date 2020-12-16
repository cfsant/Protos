import sys, os

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize CLIENT on base path {path}...\n')

    if not path.endswith('\\Protos'):
        print(f'ERR: node_modules DIR[{path}] (code:0X001).')
        return

    nodemodules = path.replace('\\Protos', '\\node_modules\\.bin')
    if not os.path.isdir(nodemodules):
        print(f'ERR: node_modules BIN[{nodemodules}] (code:0X002).')
        return

    protoc = f'{nodemodules}\\protoc-gen-ts'
    if not os.path.isfile(protoc):
        print(f'ERR: node_modules PROTOC[{protoc}] (code:0X003).')
        return

    command = f'protoc --plugin="protoc-gen-ts={protoc}" --js_out="import_style=commonjs,binary:{path}" --ts_out="{path}" -I {path} user.proto'
    print(f'Execute command: {command}')
    os.system(command)

    print('Success.')

main()