#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';


sub isTriangle
{
	my @sides = sort(@_);
	my $wellIsIt = "true";
	for (1..3)
	{
		my $testSide = shift @sides;
#		print "is testSide ... $testSide > ".int($sides[0])." + ".int($sides[1]) ." \n";
		my $bothSides = int($sides[0])+int($sides[1]);
#		print "Both Sides = $bothSides and testSide = $testSide \n";
		if ($testSide >= $bothSides) { $wellIsIt= "false";}
		push @sides, $testSide;
		#print "BothSides = $bothSides  testSide = $testSide  Result = $wellIsIt \n";
	}
	print "Returning $wellIsIt \n";
	return $wellIsIt;
}

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2

if ($star =~ /[\\\/](\d+)-go.pl/) 
{
	$star=$1;
}
else
{
	die "I don't even know what day it is... $0 \n";
}
if  (defined $ARGV[0])
{
	 $task=$ARGV[0];
}	
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

## Test
my $testResult = isTriangle(5,10,25);
if ($testResult eq "false") { print "Test 1 passed.\n";}
$testResult = isTriangle(5,3,4);
if ($testResult eq "true") { print "Test 2 passed.\n";} else {print "Test 2 failed : $testResult should be true\n"}
$testResult = isTriangle(827,126,272);
if ($testResult eq "false") { print "Test 3 passed.\n";} else {print "Test 3 failed : $testResult should be false\n"}


my $falses = 0;
my $trues = 0;
my $total = 0;


if ($task == 1)
{

	while (<INPUT>)
	{
		$total++;
		chomp;
		my @line = split(" ",$_);
		print "$line[0] , $line[1] , $line[2] ";
		if ( (isTriangle($line[0],$line[1],$line[2]) eq "true")){$trues++}else{$falses++};
	}
	close INPUT;
}
else
{
	while (<INPUT>)
	{
		$total++;
		chomp;
		my @line1 = split(" ",$_);
		$_ = <INPUT>;
		$total++;
		chomp;
		my @line2 = split(" ",$_);
		$_ = <INPUT>;
		$total++;
		chomp;
		my @line3 = split(" ",$_);
		print "$line1[0] , $line2[0] , $line3[0] ";
		if ( (isTriangle($line1[0],$line2[0],$line3[0]) eq "true")){$trues++}else{$falses++};
		print "$line1[1] , $line2[1] , $line3[1] ";
		if ( (isTriangle($line1[1],$line2[1],$line3[1]) eq "true")){$trues++}else{$falses++};
		print "$line1[2] , $line2[2] , $line3[2] ";
		if ( (isTriangle($line1[2],$line2[2],$line3[2]) eq "true")){$trues++}else{$falses++};
		
		
	}	
	
	
}
print "Trues : $trues \n";
print "Falses: $falses \n";
print "Total : $total \n";
