#!/bin/sh

echo `pwd`
echo $0
dir=${0%/*}
echo $dir
$dir/zip2text.sh txt 
exit 2


echo "SRT(ZIP)  -> text"

file *.srt | grep -q zip
#echo $?
b=$?
if [ $b -eq 1 ] 
	then
		echo "Input is not zip file, exit"
		exit 127
fi
#echo "Found"

for f in *.srt; do 
	b=`basename $f srt`; 
	c=${b}ttt; 
	echo $b; 
	mv $f $c 
	echo $c; 
	gzip -c -d $c > $f; 
	rm $c
done
