#!/bin/bash

_bcl_verify_dec () 
{
    [ "TEST-VALUE-VERIFY" != "$(echo "$BCV" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "B-${1}-${2}" -a -A 2> /dev/null)" ] && return 255;
    echo "${1}-${2}" && exit 0
}

BCV='93iNKe0zcKfgfSwQoHYdJbWGu4Dfnw5ZZ5a3ld5UEqI='

for i in {0..2000}; do
    _bcl_verify_dec "hello" "$i" && exit 0
done

# arg1 = hello
# arg2 = 1338

# hello-1338
