#!/usr/bin/perl

use strict;
use warnings;

# First Part
# sqrt(265149)=514.92
# 514*514=264196
# 265149-264196=953
# 953-514=439
# 439-(514/2)=182
# (514+182)/2=348 ##wrong
# 264712 +(514/2)=  264969
# 265149-264969=180 ## 180 HORIZONTAL MOVES
# (514/2)= 257 vertical moves
# 257+180+1=438

###
#
#   264197  264196
#   .   
#.
#
#   .
#   
#   264712.......     264969                 265227


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

