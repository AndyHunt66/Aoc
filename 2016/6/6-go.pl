#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2
my @letterDists = ({},{},{},{},{},{});#,{},{});

sub addLine
{
	print "Line coming in : ".$_[0]."\n";
	my @letters = split('',$_[0]);
	my $count=0;
	for ($count = 0; $count < scalar(@letters); $count++)
	{
		if (defined $letterDists[$count]{$letters[$count]})
		{
			$letterDists[$count]{$letters[$count]} = $letterDists[$count]{$letters[$count]} +1;
		}
		else
		{
			$letterDists[$count]{$letters[$count]} = 1;
		}
	}
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
my $inputFileName = $star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";



## Add them in 
while (<INPUT>)
{
	my $line = $_;
	chomp $line;
	addLine($line);
}
##Read them out
my @sortedLetters ;
for(my $count=0;$count<scalar(@letterDists);$count++)
{
	my %thisPosition = %letterDists[$count];
	my @sortedPosition;
	foreach (keys %thisPosition)
	{
		print "1 - ".$_ . " - ".$thisPosition{$_}."\n";
		my $tempCount = $_;
		foreach (keys $thisPosition{$tempCount})
		{
			print "2 - ".$_. " - ".$thisPosition{$tempCount}{$_}."\n";
		}
  	@sortedPosition = sort 
		{
			## Swap a and b on the next line to switch between task 1 and task 2
  		$thisPosition{$tempCount}{$a} <=> $thisPosition{$tempCount}{$b}
  	} keys %thisPosition{$tempCount};
  	$sortedLetters[$count]=$sortedPosition[0];
	}
}
print "Sorted Letters: ";
foreach (@sortedLetters) { print $_;}
print "\n";
