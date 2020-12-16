!#/bin/bash

PROTO_DIR=./Protos

# Generate TypeScript code (d.ts)
yarn run grpc_tools_node_protoc \
    --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
    --ts_out=${PROTO_DIR} \
    -I ./Protos \
    Protos/*.proto