#!/bin/sh 

#echo $#
echo "ZIP  -> text"

file *.$1 | grep -q zip
#echo $?
b=$?
echo $b
if [ $b -eq 1 ] 
	then
		echo "Input is not zip file, exit"
		exit 127
fi
#echo "Found"

for f in *.$1; do 
	b=`basename $f $1`; 
	c=${b}ttt; 
	echo $f; 
	mv $f $c 
	#echo $c; 
	gzip -c -d $c > $f; 
	rm $c
done
