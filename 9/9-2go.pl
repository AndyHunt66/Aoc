#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2
my $nestedLevel=0;
my $runningNestedLevel = 0;

sub decompressCount
{
	$nestedLevel++;# if ($nestedLevel % 1000000 == 0) {print "Nested: $nestedLevel\n";}
	$runningNestedLevel++;
	my $line = $_[0];
	#print "Setting count to zero \n";

	my $plaintextCount=0;
	my $plaintext = "";
	chomp $line;
	#print "INCOMING LINE: ".$line."\n";
	#print "LENGTH: ".length($line)."\n";
	$_ = $line;
	if (!/\(/)
	{
		#print "Returning line length :".length($line)."\n";
		$runningNestedLevel--;
		return length($line);
	}
	

	for (my $count=0;$count<length($line);$count++)
	{
		if ($nestedLevel % 1000000 == 0) {print "Running Level: $runningNestedLevel  Nested: $nestedLevel   Count: $count\n";}
		if ($runningNestedLevel<2)  {print "Running Level: $runningNestedLevel  Nested: $nestedLevel   Count: $count\n";};
		if (substr($line,$count,1) ne "(")
		{
			#print "Adding one to count\n";
			
			$plaintextCount++;
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
					
					#<STDIN>;
					#print "Plaintext: ".$plaintext."\n";
					#$plaintextCount = $plaintextCount + decompressCount($plaintext);
					#print "Plaintext Count: $plaintextCount \n";
					$plaintextCount +=   decompressCount($plaintext);
					$plaintext="";
					last;
				}
			}
			
		}
	}
	#print "Plaintext: $plaintext\n";
	#return length($plaintext);
	#return $plaintextCount +decompressCount($plaintext);
			$runningNestedLevel--;
	return $plaintextCount ;
}

sub runTest
{
my $compText = "(3x3)XYZ";
	my $len = decompressCount($compText);
	if ($len == 9) {print "Test 1 passed!\n\n"}else{print "Test 1 failed - ".$len." should be 9\n\n";}
	
	$len = decompressCount("X(8x2)(3x3)ABCY");
	if ($len == length("XABCABCABCABCABCABCY")) {print "Test 2 passed!\n\n"}else{print "Test 2 failed - ".$len." should be ". length("XABCABCABCABCABCABCY")."\n\n";}

	$len = decompressCount("(27x12)(20x12)(13x14)(7x10)(1x12)A");
	if ($len == 241920) {print "Test 3 passed!\n"}else{print "Test 3 failed - ".$len." should be 241920\n";}
	$len = decompressCount("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN");
	if ($len == 445) {print "Test 4 passed!\n"}else{print "Test 4 failed - ".$len." should be 445\n";}
	
	
	
	
	die;
}

$star=9;
$task=2;

if ((defined $ARGV[0]) && ($ARGV[0] eq "test") ){ runTest();}

my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

## Single line reading
my $input = <INPUT>;
chomp $input;
my $count = decompressCount($input);
print "Plaintext Length: $count\n";
