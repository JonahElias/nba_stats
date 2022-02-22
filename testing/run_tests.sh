echo "enter variable: \c"
read var
OUT=$(python testing/write_tests.py $var)
echo $OUT
