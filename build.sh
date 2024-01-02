#!/bin/sh

go build gohttps
go build goserver
gcc color256.c -o color256
gcc esc_exit.c -o esc_exit
