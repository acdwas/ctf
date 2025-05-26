

# strace -s 10000 ./flag.sh

```
read(3, "_bcl_verify_dec () \n{ \n    [ \"TEST-VALUE-VERIFY\" != \"$(echo \"$BCV\" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k \"B-${1}-$", 128) = 128
read(3, "{UID}\" -a -A 2> /dev/null)\" ] && return 255;\n    echo \"$1-${UID}\"\n}\n_bcl_verify() { _bcl_verify_dec \"$@\"; }\n_bcl_get () \n{ \n    ", 128) = 128
read(3, "[ -z \"$UID\" ] && UID=\"$(id -u 2> /dev/null)\";\n    [ -f \"/etc/machine-id\" ] && _bcl_verify \"$(cat \"/etc/machine-id\" 2> /dev/null)", 128) = 128
read(3, "\" && return;\n    command -v dmidecode > /dev/null && _bcl_verify \"$(dmidecode -t 1 2> /dev/null | LANG=C perl -ne '/UUID/ && pri", 128) = 128
read(3, "nt && exit')\" && return;\n    _bcl_verify \"$({ ip l sh dev \"$(LANG=C ip route show match 1.1.1.1 | perl -ne 's/.*dev ([^ ]*) .*/\\", 128) = 128
read(3, "1/ && print && exit')\" | LANG=C perl -ne 'print if /ether / && s/.*ether ([^ ]*).*/\\1/'; } 2> /dev/null)\" && return;\n    _bcl_ve", 128) = 128
read(3, "rify \"$({ blkid -o export | LANG=C perl -ne '/^UUID/ && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)\" && return;\n    _bc", 128) = 128
read(3, "l_verify \"$({ fdisk -l | LANG=C perl -ne '/identifier/i && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)\" && return\n}\n_bc", 128) = 128
read(3, "l_gen_p () \n{ \n    local _k;\n    local str;\n    [ -z \"$BC_BCL_TEST_FAIL\" ] && _k=\"$(_bcl_get)\" && _P=\"$(echo \"$1\" | openssl enc ", 128) = 128
read(3, "-d -aes-256-cbc -md sha256 -nosalt -k \"$_k\" -a -A 2> /dev/null)\";\n    [ -n \"$_P\" ] && return 0;\n    [ -n \"$fn\" ] && { \n        u", 128) = 128
read(3, "nset BCL BCV _P P S fn;\n        unset -f _bcl_get _bcl_verify _bcl_verify_dec;\n        return 255\n    };\n    BCL=\"$(echo \"$BCL\" ", 128) = 128
read(3, "| openssl base64 -d -A 2> /dev/null)\";\n    [ \"$BCL\" -eq \"$BCL\" ] 2> /dev/null && exit \"$BCL\";\n    str=\"$(echo \"$BCL\" | openssl b", 128) = 128
read(3, "ase64 -d -A 2> /dev/null)\";\n    BCL=\"${str:-$BCL}\";\n    exec /bin/sh -c \"$BCL\";\n    exit 255\n}\nBCL='aWQgLXUK'\nBCV='93iNKe0zcKfgf", 128) = 128
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=31901, si_uid=1000, si_status=0, si_utime=0, si_stime=0} ---
rt_sigreturn({mask=[]})                 = 128
read(3, "SwQoHYdJbWGu4Dfnw5ZZ5a3ld5UEqI='\nP=llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q=\nS='lRwuwaugBEhK488I'\nC=3eOcpOICWx5iy2UuoJS9gQ==\n", 128) = 128
read(3, "for x in openssl perl gunzip; do\n    command -v \"$x\" >/dev/null || { echo >&2 \"ERROR: Command not found: $x\"; return 255; }\ndone", 128) = 128
read(3, "\nunset fn _err\nif [ -n \"$ZSH_VERSION\" ]; then\n    [ \"$ZSH_EVAL_CONTEXT\" != \"${ZSH_EVAL_CONTEXT%\":file:\"*}\" ] && fn=\"$0\"\nelif [ -", 128) = 128
read(3, "n \"$BASH_VERSION\" ]; then\n    (return 0 2>/dev/null) && fn=\"${BASH_SOURCE[0]}\"\nfi\nfn=\"${BC_FN:-$fn}\"\nXS=\"${BASH_EXECUTION_STRING", 128) = 128
read(3, ":-$ZSH_EXECUTION_STRING}\"\n[ -z \"$XS\" ] && unset XS\n[ -z \"$fn\" ] && [ -z \"$XS\" ] && [ ! -f \"$0\" ] && {\n    echo >&2 'ERROR: Shell", 128) = 128
read(3, " not supported. Try \"BC_FN=FileName source FileName\"'\n    _err=1\n}\n_bc_dec() {\n    _P=\"${PASSWORD:-$BC_PASSWORD}\"\n    unset _ PA", 128) = 128
read(3, "SSWORD \n    if [ -n \"$P\" ]; then\n        if [ -n \"$BCV\" ] && [ -n \"$BCL\" ]; then\n            _bcl_gen_p \"$P\" || return\n        e", 128) = 128
read(3, "lse\n            _P=\"$(echo \"$P\"|openssl base64 -A -d)\"\n        fi\n    else\n        [ -z \"$_P\" ] && {\n            echo >&2 -n \"En", 128) = 128
read(3, "ter password: \"\n            read -r _P\n        }\n    fi\n    [ -n \"$C\" ] && {\n        local str\n        str=\"$(echo \"$C\" | openss", 128) = 128
read(3, "l enc -d -aes-256-cbc -md sha256 -nosalt -k \"C-${S}-${_P}\" -a -A 2>/dev/null)\"\n        unset C\n        [ -z \"$str\" ] && {\n      ", 128) = 128
read(3, "      [ -n \"$BCL\" ] && echo >&2 \"ERROR: Decryption failed.\"\n            return 255\n        }\n        eval \"$str\"\n        unset s", 128) = 128
read(3, "tr\n    }\n    [ -n \"$XS\" ] && {\n        exec bash -c \"$(printf %s \"$XS\" |LANG=C perl -e '<>;<>;read(STDIN,$_,1);while(<>){s/B3/\\n", 128) = 128
read(3, "/g;s/B1/\\x00/g;s/B2/B/g;print}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k \"${S}-${_P}\" 2>/dev/null|LANG=C perl -e \"read(", 128) = 128
read(3, "STDIN,\\$_, ${R:-0});print(<>)\"|gunzip)\"\n    }\n    [ -z \"$fn\" ] && [ -f \"$0\" ] && {\n        zf='read(STDIN,\\$_,1);while(<>){s/B3/", 128) = 128
read(3, "\\n/g;s/B1/\\\\x00/g;s/B2/B/g;print}'\n        prg=\"perl -e '<>;<>;$zf'<'${0}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k '${", 128) = 128
read(3, "S}-${_P}' 2>/dev/null|perl -e 'read(STDIN,\\\\\\$_, ${R:-0});print(<>)'|gunzip\"\n        LANG=C exec perl '-e$^F=255;for(319,279,385", 128) = 128
read(3, ",4314,4354){($f=syscall$_,$\",0)>0&&last};open($o,\">&=\".$f);open($i,\"'\"$prg\"'|\");print$o(<$i>);close($i)||exit($?/256);$ENV{\"LANG", 128) = 128
read(3, "\"}=\"'\"$LANG\"'\";exec{\"/proc/$$/fd/$f\"}\"'\"${0:-python3}\"'\",@ARGV' -- \"$@\"\n    }\n    [ -f \"${fn}\" ] && {\n        unset -f _bcl_get ", 128) = 128
read(3, "_bcl_verify _bcl_verify_dec\n        unset BCL BCV _ P _err\n        eval \"unset _P S R fn;$(LANG=C perl -e '<>;<>;read(STDIN,$_,1", 128) = 128
read(3, ");while(<>){s/B3/\\n/g;s/B1/\\x00/g;s/B2/B/g;print}'<\"${fn}\"|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k \"${S}-${_P}\" 2>/dev", 128) = 128
read(3, "/null|LANG=C perl -e \"read(STDIN,\\$_, ${R:-0});print(<>)\"|gunzip)\"\n        return\n    }\n    [ -z \"$fn\" ] && return\n    echo >&2 ", 128) = 128
read(3, "\"ERROR: File not found: $fn\"\n    _err=1\n}\n[ -z \"$_err\" ] && _bc_dec \"$@\"\nunset fn\nunset -f _bc_dec\nif [ -n \"$_err\" ]; then\n    u", 128) = 128
read(3, "nset _err\n    false\nelse\n    true\nfi\n", 128) = 37
```

# decode.sh

```bash
#!/bin/bash

_bcl_verify_dec () 
{ 
    [ "TEST-VALUE-VERIFY" != "$(echo "$BCV" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "B-${1}-${UID}" -a -A 2> /dev/null)" ] && return 255;
    echo "$1-${UID}"
}

_bcl_verify() 
{ 
    _bcl_verify_dec "$@"; 
}

_bcl_get () 
{ 
    [ -z "$UID" ] && UID="$(id -u 2> /dev/null)";
    [ -f "/etc/machine-id" ] && _bcl_verify "$(cat "/etc/machine-id" 2> /dev/null)" && return;
    command -v dmidecode > /dev/null && _bcl_verify "$(dmidecode -t 1 2> /dev/null | LANG=C perl -ne '/UUID/ && print && exit')" && return;
    _bcl_verify "$({ ip l sh dev "$(LANG=C ip route show match 1.1.1.1 | perl -ne 's/.*dev ([^ ]*) .*/\1/ && print && exit')" | LANG=C perl -ne 'print if /ether / && s/.*ether ([^ ]*).*/\1/'; } 2> /dev/null)" && return;
    _bcl_verify "$({ blkid -o export | LANG=C perl -ne '/^UUID/ && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)" && return;
    _bcl_verify "$({ fdisk -l | LANG=C perl -ne '/identifier/i && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)" && return
}

_bcl_gen_p () 
{ 
    local _k;
    local str;
    [ -z "$BC_BCL_TEST_FAIL" ] && _k="$(_bcl_get)" && _P="$(echo "$1" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "$_k" -a -A 2> /dev/null)";
    [ -n "$_P" ] && return 0;
    [ -n "$fn" ] && { 
        unset BCL BCV _P P S fn;
        unset -f _bcl_get _bcl_verify _bcl_verify_dec;
        return 255
    };

    BCL="$(echo "$BCL" | openssl base64 -d -A 2> /dev/null)";
    [ "$BCL" -eq "$BCL" ] 2> /dev/null && exit "$BCL";
    str="$(echo "$BCL" | openssl base64 -d -A 2> /dev/null)";
    BCL="${str:-$BCL}";
    exec /bin/sh -c "$BCL";
    exit 255
}

BCL='aWQgLXUK'
BCV='93iNKe0zcKfgfSwQoHYdJbWGu4Dfnw5ZZ5a3ld5UEqI='
P='llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q='
S='lRwuwaugBEhK488I'
C='3eOcpOICWx5iy2UuoJS9gQ=='

for x in openssl perl gunzip; do
    command -v "$x" >/dev/null || { echo >&2 "ERROR: Command not found: $x"; return 255; }
    done

unset fn _err
if [ -n "$ZSH_VERSION" ]; then
    [ "$ZSH_EVAL_CONTEXT" != "${ZSH_EVAL_CONTEXT%":file:"*}" ] && fn="$0"
    elif [ -n "$BASH_VERSION" ]; then
        (return 0 2>/dev/null) && fn="${BASH_SOURCE[0]}"
fi

fn="${BC_FN:-$fn}"
XS="${BASH_EXECUTION_STRING:-$ZSH_EXECUTION_STRING}"
[ -z "$XS" ] && unset XS
[ -z "$fn" ] && [ -z "$XS" ] && [ ! -f "$0" ] && {
    echo >&2 'ERROR: Shell not supported. Try "BC_FN=FileName source FileName"'
        _err=1
}

_bc_dec() 
{
    _P="${PASSWORD:-$BC_PASSWORD}"
    unset _ PASSWORD
    
    if [ -n "$P" ]; then
        if [ -n "$BCV" ] && [ -n "$BCL" ]; then
            _bcl_gen_p "$P" || return
        else
            _P="$(echo "$P"|openssl base64 -A -d)"
        fi
    else
        [ -z "$_P" ] && {
        echo >&2 -n "Enter password: "
        read -r _P
        }
    fi

    [ -n "$C" ] && {
        local str
        str="$(echo "$C" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "C-${S}-${_P}" -a -A 2>/dev/null)"
        unset C
        [ -z "$str" ] && {
            [ -n "$BCL" ] && echo >&2 "ERROR: Decryption failed."
            return 255
            }
        eval "$str"
        unset str
    }

[ -n "$XS" ] && {
    exec bash -c "$(printf %s "$XS" |LANG=C perl -e '<>;<>;read(STDIN,$_,1);while(<>){s/B3/\\n/g;s/B1/\\x00/g;s/B2/B/g;print}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "${S}-${_P}" 2>/dev/null|LANG=C perl -e "read(STDIN,\\$_, ${R:-0});print(<>)"|gunzip)"
    }

[ -z "$fn" ] && [ -f "$0" ] && {
    zf='read(STDIN,\\$_,1);while(<>){s/B3/\\n/g;s/B1/\\\\x00/g;s/B2/B/g;print}'
    prg="perl -e '<>;<>;$zf'<'${0}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k '${S}-${_P}' 2>/dev/null|perl -e 'read(STDIN,$_, ${R:-0});print(<>)'|gunzip"
    LANG=C exec perl '-e$^F=255;for(319,279,385,4314,4354){($f=syscall$_,$",0)>0&&last};open($o,">&=".$f);open($i,"'"$prg"'|");print$o(<$i>);close($i)||exit($?/256);$ENV{"LANG"}="'"$LANG"'";exec{"/proc/$$/fd/$f"}"'"${0:-python3}"'",@ARGV' -- "$@"
    }

[ -f "${fn}" ] && {
    unset -f _bcl_get _bcl_verify _bcl_verify_dec
    unset BCL BCV _ P _err
    eval "unset _P S R fn;$(LANG=C perl -e '<>;<>;read(STDIN,$_,1);while(<>){s/B3/\\n/g;s/B1/\\x00/g;s/B2/B/g;print}'<"${fn}"|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "${S}-${_P}" 2>/dev/null|LANG=C perl -e "read(STDIN,\\$_, ${R:-0});print(<>)"|gunzip)"
    return
    }

[ -z "$fn" ] && return
    echo >&2 "ERROR: File not found: $fn"
    _err=1
    }

[ -z "$_err" ] && _bc_dec "$@"
unset fn
unset -f _bc_dec
if [ -n "$_err" ]; then
    unset _err
        false
    else
    true
fi
```

# bclVerifyDec.sh

```bash
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
```
### arg1 = hello
### arg2 = 1338

## hello-1338


# crack_password.sh

```bash
#!/bin/bash

P='llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q='

echo "$P" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "hello-1338" -a -A 2> /dev/null
```

### password = QHh4K9JfgoACd2f4

# export PASSWORD=QHh4K9JfgoACd2f4

### ./flag.sh 
### flag{f2ea4caf879bde891f0174f528c20682}
### Congraulations!



# FLAG

**`flag{f2ea4caf879bde891f0174f528c20682}`**








