#!perl
use feature "switch";
use strict;
use warnings;
no warnings 'experimental';
use POSIX;

my %plot;

sub task2Plot
{
	my %plot;
	
	$plot{"1"}=["X","X","3","X"];
	$plot{"2"}=["X","3","6","X"];
	$plot{"3"}=["1","4","7","2"];
	$plot{"4"}=["X","X","8","3"];
	$plot{"5"}=["X","6","X","X"];
	$plot{"6"}=["2","7","A","7"];
	$plot{"7"}=["3","8","B","6"];
	$plot{"8"}=["4","9","C","7"];
	$plot{"9"}=["X","X","X","8"];
	$plot{"A"}=["6","B","X","X"];
	$plot{"B"}=["7","C","D","A"];
	$plot{"C"}=["8","X","X","B"];
	$plot{"D"}=["B","X","X","X"];
	return %plot;
}

sub task1Plot
{
	my %plot;
	$plot{"1"}=["X","2","4","X"];
	$plot{"2"}=["X","3","5","1"];
	$plot{"3"}=["X","X","6","2"];
	$plot{"4"}=["1","5","7","X"];
	$plot{"5"}=["2","6","8","4"];
	$plot{"6"}=["3","X","9","5"];
	$plot{"7"}=["4","8","X","X"];
	$plot{"8"}=["5","9","X","7"];
	$plot{"9"}=["6","X","X","8"];
	return %plot;	
}
sub moveTask
{
	my @moves=split("",$_[0]);
	my $position = 5 ; ## start position
	if (defined $_[1])
	{
		$position = $_[1];
	}
	foreach (@moves)
	{
		my $move = $_;
			if (/\n/)
		{
			## line feed - ignoring
			next;	
		}
		for ($move)
		{
			## No idea why if (!$plot{$position}[0] eq "X") doesn't work... but it doesn't, so had to turn it around
			when ("U") {if ($plot{$position}[0] eq "X"){}else{$position=  $plot{$position}[0];}}
			when ("R") {if ($plot{$position}[1] eq "X"){}else{$position=  $plot{$position}[1];}}
			when ("D") {if ($plot{$position}[2] eq "X"){}else{$position=  $plot{$position}[2];}}
			when ("L") {if ($plot{$position}[3] eq "X"){}else{$position=  $plot{$position}[3];}}
			
		}
		print "Move $move to $position \n";
		#print "Plot{Position}[0] = ".$plot{$position}[0]."<----\n";
		#print "Plot{Position}[1] = ".$plot{$position}[1]."<----\n";
	}	
	return $position;
}


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
if (!defined $ARGV[0])
{
	$task=1;
}
else
{
	$task=$ARGV[0];
}

my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";

if ($task eq 1)
{
	%plot = task1Plot;
}
elsif ($task eq 2)
{
	%plot = task2Plot;
}


my $start = 5;
my $result ;
my $data;

	print "Starting at $start\n";
	while (<INPUT>)
	{
		#chomp;
		$start=moveTask($_,$start); 
		$result= $result.$start;
		print "Next number: $start\n";
	}
	close INPUT;

print "Result = $result \n";
