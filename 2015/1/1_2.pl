#!/bin/perl

use strict;
use warnings;

my @cmds = split(//,$ARGV[0]);

my $floor=0;
my $instrNo = 0;
foreach(@cmds)
{
	$instrNo++;
	if ($_ eq"(")
	{
		$floor++;
	}
	if ($_ eq ")")
	{
		$floor--;
		if ($floor == -1)
		{
			die "Into Basement on Instruction :".$instrNo."\n";
		}
	}
}

print "FLOOR: ".$floor."\n";

