#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


sub rule1
{
	my @words=@_;
#	print "# Words:".$#words."\n";
	for (my $count=0; $count<$#words; $count++)
	{
		for (my $innerCount = $#words; $innerCount>$count; $innerCount--)
		{
			if ($words[$count] eq $words[$innerCount])
			{
				return 0;
			}
		}
	}
	return 1;
}


my $valid = 0;
my $invalid = 0;
my $lineNo=0;
while (<INPUTFILE>)
{
	chomp;
	print $_. "    ---- ";
	my $lineNo++;
	my @passphrase = split (/ /,$_);
	print $lineNo." -- ".$#passphrase;
		if (rule1(@passphrase) == 1)
	{
		print " -- Valid \n";
		$valid++;
	}
	else
	{
		print " -- Invalid \n";
		$invalid++
	}
}

print "VALID: ".$valid."\n";
print "INVALID: ".$invalid."\n";



