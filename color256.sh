#/bin/sh

function i3()
{
    if test $1 -lt 10; then
        echo -n " 00"$1" "
        return
    fi

    if test $1 -lt 100; then
        echo -n " 0"$1" "
        return
    fi

   echo -n " "$1" "
}

for i in `seq 0 255`; do
    echo -en "\033[48;5;${i}m\033[38;5;15m"
    i3 $i
    echo -en "\033[33;5;0m\033[38;5;${i}m"
    i3 $i
    i_plus_1=`expr $i + 1`
    i_plus_1_mod_16=`expr $i_plus_1 % 16`
    if test $i_plus_1_mod_16 -eq 0; then
        echo -e "\033[0m"
    fi
done

