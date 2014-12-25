#!/bin/sh

echo `pwd`
echo $0
dir=${0%/*}
echo $dir
$dir/zip2text.sh srt 
exit 2

echo "123"

for f in *.txt; do 
	b=`basename $f txt`; 
	c=${b}ttt; 
	echo $b; 
	mv $f $c 
	echo $c; 
	gzip -c -d $c > $f; 
	rm $c
done
