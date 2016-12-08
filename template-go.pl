#!perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2

if ($star =~ /\\(\d+)-go.pl/)
{
	$star=$1;
}
else
{
	die "I don't even know what day it is... $0 \n";
}
for  ($ARGV[0])
{
	when (1) { $task=1}
	when (2) { $task=2}
	when (3) { $task=3} ## do both 1 and 2
	when (!defined) { $task=3}
	default  { die "No idea which part of the challenge you're trying to do.... $ARGV[0] \n"}
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
