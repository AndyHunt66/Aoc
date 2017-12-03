#!/usr/bin/perl

use strict;
use warnings;


my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my $total=0;

while (<INPUTFILE>)
{
	my @sides=sort {$a <=> $b} split(/x/,$_);
	$total = $total + ( ( $sides[0]*$sides[1]*3) + ($sides[1]*$sides[2]*2) + ($sides[0]*$sides[2]*2) )
}
print "TOTAL: ".($total)."\n";

