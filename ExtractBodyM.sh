tail -n +2 $1 | cut -d $3 -f 2-6 | tr -s $3 ' ' | sort -r -n -k 6 > $2 
