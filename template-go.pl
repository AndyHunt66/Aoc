#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

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
if (defined $ARGV[0])
{
	$task=$ARGV[0];
}	
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

## Single line reading
my $input = <INPUT>;
chomp $input;


## Multi line reading
while (<INPUT>)
{
	my $line = $_;
	chomp $line;
	
	
}
print "InputFileName = $inputFileName \n";
