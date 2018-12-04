#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my %records;
my %guards;
while (<INPUTFILE>)
{

    # #1 @ 37,526: 17x23
    my $line = $_;
    $line =~ /^\[(.*)\] (.*)$/;
    $records{$1} = $2;
    
}
close INPUTFILE;

my $guardId=0;
my $minuteAsleep=0;
my $date="";
foreach my $record (sort keys %records)
{
	$record=~/(\d\d\d\d-\d\d-\d\d)/;
	if ($1 ne $date)
	{
		print "Day: $1\n";
		$date = $1;
	}
	my $minute;
	$records{$record} =~/^([wfG])[^ ]* (#(\d*) )?/;
	my $action = $1;
	if ($action eq "G")
	{
	 	$guardId = $3;
	 	print "Guard $guardId on duty\n";
	}
	else
	{
		$record =~ /\d\d:(\d\d)/;
		$minute = $1;
	}
	if ($action eq "f")
	{
		$minuteAsleep=$minute;
	 	print "Guard $guardId fell asleep at $minute ";
	}
	if ($action eq "w")
	{
		for (my $count=$minuteAsleep;$count<$minute;$count++)
		{
			$guards{$guardId}[$count]++;
		}
	 	print "and woke up at $minute \n";
	 	<>;
	}
	

	
};
