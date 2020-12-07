#!/usr/bin/perl

use strict;
use warnings;



my $inputFileName = "./input.txt";


open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my @field;
my $fieldXMax = 0;
my $fieldYMax = 0;
my $pointId = 0;
my @pointCoords;

print "Filling the given points into the field \n";
while (<INPUTFILE>)
{
	my $coord = $_;
	$pointId++;
	$coord =~/^(\d*), (\d*)$/;
	$pointCoords[$pointId]=[$1,$2];
	$field[$1][$2]{$pointId}=0;
	$field[$1][$2]{"closest"}=$pointId;
	if ($1>$fieldXMax)
	{
		$fieldXMax=$1;
	}
	if ($2>$fieldYMax)
	{
		$fieldYMax=$2;
	}
}

print "Field size is $fieldXMax by $fieldYMax \n";
print " and the far right corner is ".&dist([0,0],[$fieldXMax,$fieldYMax])." from the origin\n";


print "Calculating the closest neighbour of each point in the field \n";
for ( my $XCount=0;$XCount<=$fieldXMax;$XCount++)
{
	for ( my $YCount=0;$YCount<=$fieldYMax;$YCount++)
	{
		if (defined $field[$XCount][$YCount]{"closest"}) { next;}
		my $closestValue = 1000;
		my $closestId = 0;
		for (my $coordId =1;$coordId<=$#pointCoords;$coordId++)
		{
			my $distance = dist(@pointCoords[$coordId],[$XCount,$YCount] );
			$field[$XCount][$YCount]{$coordId}= $distance;
			if ($distance < $closestValue)
			{
				$closestValue=$distance;
				$closestId=$coordId;
			}
			elsif ($distance == $closestValue)
			{
				$closestId = 0;
			}
		}
		$field[$XCount][$YCount]{"closest"}=$closestId;
	}
}

print "Finding the size of each sub-field \n";
my @areaTotals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
for ( my $XCount=0;$XCount<=$fieldXMax;$XCount++)
{
	for (my $YCount = 0; $YCount <= $fieldYMax; $YCount++)
	{
		$areaTotals[$field[$XCount][$YCount]{"closest"}]++;
	}
}

print "Removing the infinite sub-fields \n";
for ( my $XCount=0;$XCount<=$fieldXMax;$XCount++)
{
	$areaTotals[$field[$XCount][0]{"closest"}]=0;
	$areaTotals[$field[$XCount][$fieldYMax]{"closest"}]=0;
}
for ( my $YCount=0;$YCount<=$fieldYMax;$YCount++)
{
	$areaTotals[$field[$YCount][0]{"closest"}]=0;
	$areaTotals[$field[$YCount][$fieldXMax]{"closest"}]=0;
}

print "Finding the largest sub-field \n";
my $largestField = 0;
my $largestFieldSize = 0;
for(my $count=1;$count<= (scalar @areaTotals); $count++)
{
	if ($areaTotals[$count] > $largestField)
	{
		$largestField = $count;
		$largestFieldSize = $areaTotals[$count];
	}
}

print "Largest Field is $largestField with size $largestFieldSize \n";

sub dist
{
	my @point1=@{ $_[0]};
	my @point2=@{ $_[1]};
	my $distance = abs($point1[0]-$point2[0])+abs($point1[1]-$point2[1]);
	return $distance;
}