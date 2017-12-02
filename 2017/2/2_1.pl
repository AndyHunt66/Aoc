#!/usr/bin/perl
use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my $total=0;

while (<INPUTFILE>)
{
	my @numbers=sort {$a <=> $b} split(/[ \t]/,$_);
	$total+=($numbers[$#numbers] - $numbers[0]);
}
print "TOTAL: ".$total."\n";

