
## for i in {0..728}; do objdump -Mintel -d binary$i | grep cmp -B 1 >> file.txt; done
