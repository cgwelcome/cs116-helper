#!/usr/bin/env bash

set -o noclobber

a_no=$(printf '%0.2d' $1)
no_q=$2

for q_no in $(seq $no_q);
do
	perl -pe "s/\\$\{a_no\}/$a_no/;s/\\$\{q_no\}/$q_no/" headingcs116.txt \
	> a${a_no}q${q_no}.py; 
done  

