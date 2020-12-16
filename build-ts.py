import sys, os

def main():
    os.system('cls')

    clientdir = '../Client/proto'
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize PROTO-BUILD-TS on base path {path}...\n')
    
    os.system(f'yarn run grpc_tools_node_protoc --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts --ts_out=${clientdir} -I {path} {path}/*.proto')

main()