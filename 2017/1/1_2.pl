#!/bin/perl

use strict;
use warnings;

my $input = $ARGV[0];

my $total = 0;
my @numbers = split(//,$input);
my $steps = ($#numbers+1)/2;

for (my $count=0; $count <=$#numbers; $count++)
{
	#print "COUNT:".$count."\n";
			if ($numbers[$count] == $numbers[($count+$steps)%($#numbers+1)])
			{
				$total = $total+$numbers[$count];
			}
}

print "TOTAL : " . $total."\n";