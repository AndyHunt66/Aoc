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
	}
};

my %guardsAsleep;
my $highestGuardId;
my $highestGuardMinutes=0;
foreach $guardId (keys %guards)
{
	
	for (my $count=0;$count<=59;$count++)
	{
#		print "Minute $count\n";
		if (defined $guards{$guardId}[$count])
		{
#			print "minute $count - $guards{$guardId}[$count]\n";

			if (defined $guardsAsleep{$guardId})
			{
#				print $guardsAsleep{$guardId} ." -- ". $guards{$guardId}[$count]."\n";
				$guardsAsleep{$guardId}=$guardsAsleep{$guardId} + $guards{$guardId}[$count];
			}
			else
			{
				$guardsAsleep{$guardId}=$guards{$guardId}[$count];
#				print "Sleepy time; ".$guardsAsleep{$guardId}."\n";
			}
		}
		else
		{
#			print "minute $count - Nothing\n";
		}
	}
	if ($guardsAsleep{$guardId} > $highestGuardMinutes)
	{
		print "Highest So far: $highestGuardMinutes\n";
		$highestGuardMinutes = $guardsAsleep{$guardId};
		$highestGuardId=$guardId;
	}
	
}


print "Guard $highestGuardId slept for $highestGuardMinutes \n";
my $guardHighestMinuteValue=0;
my $guardHighestMinute;
my $guardIdHighestMinute=0;
foreach my $guard (keys %guards)
{
	for (my $count=0;$count<=59;$count++)
	{
		if (!defined $guards{$guard}[$count]) { next;}
		if ($guards{$guard}[$count] > $guardHighestMinuteValue)
		{
			$guardHighestMinuteValue = $guards{$guard}[$count];
			$guardHighestMinute = $count;
			$guardIdHighestMinute=$guard;	
		}
	}
}
print "Guard $guardIdHighestMinute was asleep $guardHighestMinuteValue times in minute $guardHighestMinute \n";
print "Answer is : ".$guardIdHighestMinute * $guardHighestMinute."\n";