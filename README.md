# Abominator

Inspired by a Tweet by https://moonbase.lgbt/

## Usage

Requires python3 and a Linux based operating system to run

Tested with GCC 13.3.0 on Linux 6.10.1-zen1 kernel.

```
echo "hello world" | python abominator.py > abomination.c
gcc abomination.c -o abomination
./abomination
```

## Rebuild the print function

```sh
gcc -c print.S
objdump -d print.o | grep -E "^\s+[a-f0-9]+:" | sed -E "s/^ +[a-z0-9]+:\t+//" | sed -E "s/\t+.*//" | sed -E "s/([0-9a-f]+)/0x\1,/g"
```

Then copy the output to the template
