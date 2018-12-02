#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
#my $inputFileName = "./input_test.txt";

my %patterns;
my @banks;
my $bankSize;
my $steps=0;

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
while (<INPUTFILE>)
{
 @banks = split(/[ \t]/,$_)
}
close INPUTFILE;

$bankSize = scalar @banks;

while(1)
{
	$steps++;
	print "Step $steps \t";

	my $position=0;
  foreach (my $loc = 0; $loc<$bankSize; $loc++)
	{
		if ($banks[$loc] > $banks[$position])
		{
			$position = $loc;
		}
	}
	my $reDist = $banks[$position];
	print " Position: $position \t Size: $reDist . ";
	$banks[$position]=0;
	while ($reDist > 0)
	{
		$position=($position+1) %  $bankSize;
		$banks[$position]++;
		$reDist--;
		#print "Step $steps . Position: $position  Size: $banks[$position]   \n";
	}

	my $pattern = join(',',@banks);
	if ($patterns{$pattern})
	{
		print "Found duplicate pattern in $steps steps: \n". $pattern."\n";
		print "loopsize = $steps - $patterns{$pattern} == ".($steps - $patterns{$pattern})."\n";
		die;
	}
	else
	{
		$patterns{$pattern}=$steps;
		print " $pattern \n";
	}

	#<>;
}
die;

