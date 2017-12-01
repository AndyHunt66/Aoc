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
my $firstNumber = $numbers[0];
for (my $count=0; $count <=$#numbers; $count++)
{
	#print "COUNT:".$count."\n";
	if ($count<$#numbers)
	{
		if ($numbers[$count] == $numbers[$count+1])
		{
			$total = $total+$numbers[$count];
		}
	}
	else
	{
		if ($numbers[$count] == $numbers[0])
		{
			$total = $total+$numbers[$count];
		}
	}
}

print "TOTAL : " . $total."\n";