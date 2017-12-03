#!/bin/perl

use strict;
use warnings;

my @cmds = split(//,$ARGV[0]);

my $floor=0;
foreach(@cmds)
{
	if ($_ eq"(")
	{
		$floor++;
	}
	if ($_ eq ")")
	{
		$floor--;
	}
}

print "FLOOR: ".$floor."\n";

