#!/bin/bash
echo "=======STARTED SCANS======"
file="subdomains.txt"
if test -d "subs"
	then
		echo ""
	else
		mkdir subs
	fi
while read -r line
do
	echo "=======SCANNING $line"
	if test -f "subs/$line/vuln.nmap"
		then
			echo "Already have data for $line"
		else
			mkdir subs/$line
			nmap -sV -sC --script=vuln -vv -Pn -oA subs/$line/vuln $line
	fi
done < "$file"
echo "========FINISHED SCANS======"
