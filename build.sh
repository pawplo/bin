#!/bin/sh

set -e

mkdir -p ~/bin/build
cd ~/bin

function run()
{
    echo $@
    $@
}

for i in `ls *.c 2>/dev/null`; do
    f=${i%*.c}
    run gcc $i -o build/$f
done;

for i in `ls *.go 2>/dev/null`; do
    f=${i%*.go}
    run go build -o build/$f $i
done;

