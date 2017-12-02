#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2


sub decompress
{
	my $line = $_[0];
	my $plaintext = "";
	chomp $line;
	#print "INCOMING LINE: ".$line."\n";
	#print "LENGTH: ".length($line)."\n";
	$_ = $line;
	if (!/\(/)
	{
		return $line;
	}
	

	for (my $count=0;$count<length($line);$count++)
	{
		if (substr($line,$count,1) ne "(")
		{
			$plaintext = $plaintext.substr($line,$count,1);
			next;
		}		
		else
		{
			## Find the closing brackets
			for (my $innerCount = 1; $innerCount<length($line)-$count;$innerCount++)
			{
				if (substr($line, $count+$innerCount,1) eq ")")
				{
					my ($reach, $multiplier) = split ("x", substr($line, $count+1, $innerCount-1) ) ;
					#print "Reach: $reach , Multiplier: $multiplier \n";
					for(1..$multiplier)
					{
						#print "Count: $count   innerCount: $innerCount   Reach: $reach\n";
						$plaintext = $plaintext . substr($line,$count+$innerCount+1,$reach);
					}
					$count= $count+$innerCount + $reach;
					last;
				}
			}
			
		}
	}
	#print "Plaintext: $plaintext\n";
	#return length($plaintext);
	return $plaintext;
}

sub runTest
{
	my $compText = "ADVENT";
	my $len = decompress($compText);
	if (length($len) == 6) {print "Test 1 passed!\n"}else{print "Test 1 failed - ".$len." should be 6\n";}
	$len = decompress("A(1x5)BC");
	if (length($len) == 7) {print "Test 2 passed!\n"}else{print "Test 2 failed - ".$len." should be 7\n";}
	$len = decompress("(3x3)XYZ");
	if (length($len) == 9) {print "Test 3 passed!\n"}else{print "Test 3 failed - ".$len." should be 9\n";}
	$len = decompress("A(2x2)BCD(2x2)EFG");
	if (length($len) == 11) {print "Test 4 passed!\n"}else{print "Test 4 failed - ".$len." should be 11\n";}
	$len = decompress("(6x1)(1x3)A");
	if (length($len) == 6) {print "Test 5 passed!\n"}else{print "Test 5 failed - ".$len." should be 6\n";}
	$len = decompress("X(8x2)(3x3)ABCY");
	if (length($len) == 18) {print "Test 6 passed!\n"}else{print "Test 6 failed - ".$len." should be 18\n";}
	
	
	
	
	die;
}

if ($star =~ /[\\\/](\d+)-go.pl/)
{
	$star=$1;
}
else
{
	die "I don't even know what day it is... $0 \n";
}
if (defined $ARGV[0])
{
	$task=$ARGV[0];
}	

if ($task eq "test") { runTest();}

my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

## Single line reading
my $input = <INPUT>;
chomp $input;
my $plaintext = decompress($input);
print "Plaintext Length: ".length($plaintext)."\n";
for  (1..3)
{
	if ($plaintext=~/\(/)
	{
		$plaintext=decompress($plaintext);
		print "Plaintext Length: ".length($plaintext)."\n";
	}
	else
	{
		last;
	}
}

#print $plaintext."\n";

print length($plaintext);