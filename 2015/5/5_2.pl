#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


sub rule1
{
	my $numVowels=0;
	my $testString=$_[0];
	for (split (//,$testString))
	{
		if (/[aeiou]/)
		{
			$numVowels++;
		}
	}
	if ($numVowels > 2)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

sub rule2
{
	my $testString=$_[0];
	my @chars =  (split (//,$testString));
	for (my $count=0; $count<$#chars;$count++)
	{
		if ($chars[$count] eq ($chars[$count+1]))
		{
			return 1;
		}
	}
	return 0;
}

sub rule3
{
	if ($_[0]=~/ab/)
	{
		return 0;
	}
	if ($_[0]=~/cd/)
	{
		return 0;
	}
	if ($_[0]=~/pq/)
	{
		return 0;
	}
	if ($_[0]=~/xy/)
	{
		return 0;
	}

	return 1;
}
 
sub isItNice
{
	my $testString = $_[0];
	if (rule1($testString) == 0){return 0};	
	if (rule2($testString) == 0){return 0};	
	if (rule3($testString) == 0){return 0};	
	return 1;
	
}

#my $string = "aei";
#my $string = "xazegv";
#my $string = "xazegvo";
#my $string = "aeiouaeiouaeiou";
#my $string = "ugknbfddgicrmopn";
#my $string = "aaa";
#my $string = "jchzalrnumimnmhp";
#my $string = "haegwjzuvuyypxyu";
#my $string = "dvszwmarrgswjxmb";

my $nice = 0;
my $naughty = 0;
while (<INPUTFILE>)
{
	if (isItNice($_) == 1)
	{
		$nice++;
	}
	else
	{
		$naughty++
	}
}

print "NICE: ".$nice."\n";
print "NAUGHTY: ".$naughty."\n";



