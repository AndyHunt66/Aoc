#!/usr/bin/perl

use strict;
use warnings;


my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my $total=0;

while (<INPUTFILE>)
{
	my @numbers=sort {$a <=> $b} split(/[ \t]/,$_);
	
	for(my $count=$#numbers; $count>=0;$count--)
	{
		my $dividend = $numbers[$count];
		for (my $innerCount = 0; $innerCount < $count; $innerCount++)
		{
			my $divisor = $numbers[$innerCount];
			if (($dividend % $divisor)==0)
			{
				$total += ($dividend/$divisor);
				last;
			}
		}
	}
}
print "TOTAL: ".$total."\n";

