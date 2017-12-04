#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

sub rule2
{
	my $wordIsDifferent = 0;
	my @words=@_;
	for (my $count=0; $count<=$#words; $count++)
	{
		my @outerWord= sort {$a cmp $b} split(//,$words[$count]);			
		for (my $innerCount = $#words; $innerCount>$count; $innerCount--)
		{
#			print "Outer Word = ". $words[$count]. "  Inner Word: ". $words[$innerCount]."\n";
			my @innerWord=sort {$a cmp $b} split(//,$words[$innerCount]);		
			if ($#innerWord != $#outerWord)	{ next;}
			my $wordIsDifferent = 0;
			for (my $comp = 0; $comp<=$#innerWord; $comp++)
			{
#				print "First Letter : ".$innerWord[$comp]."  Second Letter: ".$outerWord[$comp]."\n";
				if ($innerWord[$comp] ne $outerWord[$comp])
				{
					$wordIsDifferent = 1;
				}
			}
			if ($wordIsDifferent == 0)
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
#	print $_. "    ---- \n";
	$lineNo++;
	my @passphrase = split (/ /,$_);
#	print $lineNo." -- ".$#passphrase;
	if (rule2(@passphrase) == 1)
	{
#		print " -- Valid \n";
		$valid++;
	}
	else
	{
#		print " -- Invalid \n";
		$invalid++
	}
}

print "VALID: ".$valid."\n";
print "INVALID: ".$invalid."\n";
# golnm ltizhd dvwv xrizqhd omegnez nan yqajse lgef
#221 is too low
