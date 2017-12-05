#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my @memArray;
my $listSize=0;
my $count=0;
while (<INPUTFILE>)
{
	chomp;
	@memArray[$count]=$_;
	$count++;
}
$listSize=$count;
print "Size of grid = ".$count ."\n";
<>;
my $currentPosition = 0;
my $numSteps=0;
while ($currentPosition <$listSize)
{
	$numSteps++;
	print "Move #".$numSteps;
	$currentPosition = &move($currentPosition);
	if ($currentPosition > $listSize)
	{
		last;
	}
}

print "STEPS TAKEN: ".$numSteps."\n";



sub move
{
	my $start=$_[0];
	my $stepsToTake=$memArray[$start];
	$memArray[$start]=$memArray[$start]+1;
	print " Starting Point:".$start."   Steps:".$stepsToTake."\n";
	return $start + $stepsToTake;
	
}

# Grid Size : 1052