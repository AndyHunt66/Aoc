#!/bin/perl

use strict;
use warnings;

#my $inputFileName = "./input";
#my $outputFileName = "./output.txt";

my $cmdLineInput = $ARGV[0];

#open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
#open OUTPUTFILE, ">$outputFileName" or die "Couldn't open outputFile $outputFileName for writing - $!\n";

my $input = $cmdLineInput;

my $total = 0;
my @numbers = split(//,$input);
my $steps = ($#numbers+1)/2;
print "STEPS: ". $steps."\n";
for (my $count=0; $count <=$#numbers; $count++)
{
	print "COUNT:".$count."\n";
		if (($count + $steps) > $#numbers-1)
		{
			if ($numbers[$count] == $numbers[$count-$steps])
			{
				$total = $total+$numbers[$count];
			}
		}
		else
		{
			if ($numbers[$count] == $numbers[$count+$steps])
			{
				$total = $total+$numbers[$count];
			}
		}

}

print "TOTAL : " . $total."\n";