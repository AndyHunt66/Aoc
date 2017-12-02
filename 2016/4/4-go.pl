#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

sub isRoomReal
{
	#print  "Room: $_[0]\n";
	my %letters;
	my @room = split(/[-\[\]]/,$_[0]);
	
	my $roomCode = pop @room; #print "RoomCode: $roomCode \n";
	my $sectorId = pop @room; #print "SectorId : $sectorId \n";
	
	foreach (@room)
	{
		my @word = split("",$_);
		foreach (@word)
		{
			$letters{$_}++;
		}	
	}
	my @sortedLetters = sort 
	{
  	$letters{$b} <=> $letters{$a}
    or
  	"\L$a" cmp "\L$b" 
  } keys %letters;
	
	
	my $roomValue = 0;
	#print "Calculated roomCode= ".$sortedLetters[0].$sortedLetters[1].$sortedLetters[2].$sortedLetters[3].$sortedLetters[4]."\n";
	if ($roomCode eq $sortedLetters[0].$sortedLetters[1].$sortedLetters[2].$sortedLetters[3].$sortedLetters[4])
	{
		return $sectorId;
	}
	return 0;
}

sub spinLetter
{
	my $letterToSpin = $_[0];
	my $spinAmount = $_[1];
	
	for (1..$spinAmount)
	{
		if ($letterToSpin eq "z")
		{
			$letterToSpin = 'a';
		}
		else
		{
			$letterToSpin++;
		}
	}	
	return $letterToSpin;
}
sub spinCode
{
	#print  "Room: $_[0]\n";
	my $realRoomName="";
	my @room = split(/[-\[\]]/,$_[0]);
	
	my $roomCode = pop @room; #print "RoomCode: $roomCode \n";
	my $sectorId = pop @room; #print "SectorId : $sectorId \n";
	foreach (@room)
	{
		if ($realRoomName ne "")
		{
			$realRoomName = $realRoomName." ";
		}
		my @word = split("",$_);
		foreach (@word)
		{
			#print $_."\n";
			$realRoomName=$realRoomName . spinLetter($_, $sectorId);
		}	
		$realRoomName=$realRoomName;
	}
	return $realRoomName;
}

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2

if ($star =~ /[^\d](\d+)-go.pl/)
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
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

#
if ($task eq "test")
{
	my $testResult=isRoomReal("aaaaa-bbb-z-y-x-123[abxyz]");
	if ( $testResult == 123 ) { print "Test 1 passed\n";}else{print "Test 1 failed : 	$testResult should be 123 \n";}
	
	$testResult=isRoomReal("a-b-c-d-e-f-g-h-987[abcde]");
	if ( $testResult == 987 ) { print "Test 2 passed\n";}else{print "Test 2 failed : 	$testResult should be 987 \n";}
	
	$testResult=isRoomReal("not-a-real-room-404[oarel]");
	if ( $testResult == 404 ) { print "Test 3 passed\n";}else{print "Test 3 failed : 	$testResult should be 404 \n";}
	
	$testResult=isRoomReal("totally-real-room-200[decoy]");
	if ( $testResult == 0 ) { print "Test 4 passed\n";}else{print "Test 4 failed : 	$testResult should be 0 \n";}
	
	$testResult=spinCode("qzmt-zixmtkozy-ivhz-343[xxxx]");
	if ( $testResult eq "very encrypted name"){print "Test 5 passed";}else{print "Test 5 failed : $testResult should be \"very encrypted name\"\n";}
}

my $result = 0;
while (<INPUT>)
{
	my $realRoomName = "";
	my $line = $_;
	chomp $line;
	my $thisRoom = isRoomReal($line);
	if ($thisRoom > 0) 
	{
		$result += isRoomReal($line);
		$realRoomName = spinCode($line);
	}
	if ($realRoomName ne "")
	{
		print "Real Room: ".$realRoomName." - ". $thisRoom."\n"; ## meh - just grep the output yourself
	}
	
}
print "Result = $result \n";
