#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2
my %initialise;
my %outputs;
my %instructions;
my %bots;
my $comparingBot;
sub runTest
{
	
	
}

sub checkBots
{
	foreach (keys %outputs)
	{
		print "Output $_ : $outputs{$_} \n";
	}
	## test to see if we've found the bot we need
	## the one that compares 61 to 17
	foreach (keys %bots)
	{
		my $botNumber = $_;
		print "Bot ".$botNumber." is holding ";

		if (defined $bots{$botNumber}[0] )
		{
			print $bots{$botNumber}[0];
		}
		else
		{
			print " nothing ";
		}
		if (defined $bots{$botNumber}[1] )
		{
			print " and $bots{$botNumber}[1] \n" ;
		}
		else
		{	
			print " and nothing \n";
		}
		if (	(defined $bots{$botNumber}[1] ) && (defined $bots{$botNumber}[1]) &&
		    (
		     (
		      ($bots{$botNumber}[0] == 61 ) && ($bots{$botNumber}[1]==17)
		     )
		     ||
		     (
		      ($bots{$botNumber}[1] == 61 ) && ($bots{$botNumber}[0]==17)
		     )
		    )
			)
		{
			print "Found it! Bot Number $botNumber \n";
			$comparingBot = $botNumber;
		}
	}
}

sub checkHands
{
	my $stillWorking = "false";
	foreach (keys %bots)
	{
		my $botNumber = $_;
		## Does it hav something in both hands?
		if ( (defined @{$bots{$botNumber}}[0] ) && (defined @{$bots{$botNumber}}[1] ) )
		{
			$stillWorking = "true";
			my ($high, $low) = sort { $b <=> $a } (@{$bots{$botNumber}}[0], @{$bots{$botNumber}}[1]);
			#print "High = $high    Low = $low \n"; die;
			my @handsfulInstruction;
			if ( @{$instructions{$botNumber}}) 
			{
				@handsfulInstruction = @{$instructions{$botNumber}};
			}
			else
			{
				die "can't find an instruction for Bot Number $botNumber \n";
			}
			if ($handsfulInstruction[0] eq "bot")
			{
				push @{$bots{$handsfulInstruction[1]}},$low ;
			}
			elsif ($handsfulInstruction[0] eq "output")
			{
				$outputs{$handsfulInstruction[1]} = $low ;
			}
			if ($handsfulInstruction[2] eq "bot")
			{
				push @{$bots{$handsfulInstruction[3]}},$high ;
			}
			elsif ($handsfulInstruction[2] eq "output")
			{
				$outputs{$handsfulInstruction[3]} = $high ;
			}
			## He's given all his stuff away, is now empty.
		delete $bots{$botNumber};
		}
	}
	return $stillWorking;
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
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";


## Fill the instruction list
my $lineNumber=0;
while (<INPUT>)
{
	$lineNumber++;
	my $line = $_;
	chomp $line;
	if ($line=~/^value (\d+) goes to bot (\d+)$/)
	{
		push @{$bots{$2}} , $1;
	}
	## bot 150 gives low to bot 132 and high to bot 99
	elsif ($line=~/^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)$/)
	{
		@{$instructions{$1}}[0]=$2; ## [0] $2 == bot or output
		@{$instructions{$1}}[1]=$3; ## [1] $3 == low receiveing bot/output number
		@{$instructions{$1}}[2]=$4;
		@{$instructions{$1}}[3]=$5;
	}
	else
	{
		die "Don't understand the instruction : $line\n";
	}
}


## First check 
print "Check 1\n";
checkBots();

my $count = 1;
while (1)
{
	$count++;
	if (checkHands() eq "false")
	{
		 "Can't do anymore \n";
		 last;
	}
	print "Check $count\n";
	checkBots();
}

print "Bot who is comparing 61 and 17: $comparingBot \n";
print "Outputs of 0,1 and 2 are : \n";
print "0: ".$outputs{"0"}."\n";
print "1: ".$outputs{"1"}."\n";
print "2: ".$outputs{"2"}."\n";
print "Multiplied = ". ($outputs{"0"} *  $outputs{"1"} *  $outputs{"2"}) ."\n";