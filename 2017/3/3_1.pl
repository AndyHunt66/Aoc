#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my $total=0;

while (<INPUTFILE>)
{
#print "LINE: ".$_."\n";
	my @numbers=split(/[ \t]/,$_);
	my $lineMax=$numbers[0];
	my $lineMin=$numbers[0];

	foreach(@numbers)
	{
		my $current = $_;
#		print "NUMBER: ". $current."\n";
		if ($current > $lineMax) {$lineMax=$current}
		if ($current < $lineMin) {$lineMin=$current}
	}
	$total=$total+($lineMax - $lineMin);
}
print "TOTAL: ".$total."\n";

