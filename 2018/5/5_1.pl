#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
my $chunksize = 10;

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


my $full = <INPUTFILE>;
chomp($full);
my @full = split //,$full;
my $combined = 0;
while (1)  
{
	for (my $count = 0;$count < $#full;)
	{
	#	for(0..5)
	#	{
	#		print $full[$count+$_];
	#	}
	#	print "\n";#<>;
		if (($full[$count] =~ /$full[$count+1]/i) &&
		     ($full[$count] !~ /$full[$count+1]/))
		{
			splice(@full,$count,2);	 
			$combined++;
		}
		else
		{
			$count++;
		}
	}
	print "Finished pass - $combined combined\n";
	if ($combined == 0)
	{
		print "Final string: ";
		foreach (@full)
		{
			print;
		}
		print "\n";
		print "Size: ". scalar @full."\n";
		die;
	}
	$combined = 0;
}
