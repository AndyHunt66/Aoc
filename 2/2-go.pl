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


sub moveTask2
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
sub moveTask1
{
	my @moves=split("",$_[0]);
	my $position = 5 ; ## Starting position
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
		 when ("U") 
		 {if ($position-3 > 0) { $position -= 3;} }
		 when ("D")
		 {if ($position+3 < 10 ) { $position += 3;} }
		 when ("L")
		 {if (ceil(($position-1)/3) == ceil($position/3) ){ $position -= 1;} }
		 when ("R")
		 {if (ceil(($position+1)/3) == ceil($position/3)) { $position += 1;} }
		}	
		#print "Moving $move to $position \n";
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

if ($task eq 2)
{
	%plot = task2Plot;
}

## run tests
my $test = moveTask1("ULL\n");
if ($test == 1) { print "Test 1 passed\n\n";} else { die "Test 1 failed: $test should be 1" }

$test = moveTask1("ULL\nRRDDD");
if ($test == 9) { print "Test 2 passed\n\n";} else { die "Test 2 failed: $test should be 9" }

$test = moveTask1("ULLRRDDDLURDLUUUUD");
if ($test == 5) { print "Test 3 passed\n\n";} else { die "Test 3 failed: $test should be 5" }

$test = moveTask1("ULUULLUULUUUUDURUUULLDLDDRDRDULULRULLRLULRUDRRLDDLRULLLDRDRRDDLLLLDURUURDUDUUURDRLRLLURUDRDULURRUDLRDRRLLRDULLDURURLLLULLRLUDDLRRURRLDULRDDULDLRLURDUDRLLRUDDRLRDLLDDUURLRUDDURRLRURLDDDURRDLLDUUDLLLDUDURLUDURLRDLURURRLRLDDRURRLRRDURLURURRRULRRDLDDDDLLRDLDDDRDDRLUUDDLDUURUULDLUULUURRDRLDDDULRRRRULULLRLLDDUDRLRRLLLLLDRULURLLDULULLUULDDRURUDULDRDRRURLDRDDLULRDDRDLRLUDLLLDUDULUUUUDRDRURDDULLRDRLRRURLRDLRRRRUDDLRDDUDLDLUUDLDDRRRDRLLRLUURUDRUUULUDDDLDUULULLRUDULULLLDRLDDLLUUDRDDDDRUDURDRRUUDDLRRRRURLURLD");
if ($test == 5) { print "Test 4 passed\n\n";} else { die "Test 4 failed: $test should be 5" }

$test = moveTask2("RRR\n");
if ($test == 8) { print "Test 5 passed\n\n";} else { die "Test 5 failed: $test should be 8" }

$test = moveTask2("ULL\n",5);
if ($test == 5) { print "Test 6 passed\n\n";} else { die "Test 6 failed: $test should be 5" }

$test = moveTask2("RRDDD\n",5);
if ($test eq "D") { print "Test 7 passed\n\n";} else { die "Test 7 failed: $test should be D" }

$test = moveTask2("LURDL\n","D");
if ($test eq "B") { print "Test 8 passed\n\n";} else { die "Test 8 failed: $test should be B" }

$test = moveTask2("UUUUD\n","B");
if ($test eq "3") { print "Test 9 passed\n\n";} else { die "Test 9 failed: $test should be 3" }



my $start = 5;
my $result ;

	my $data;
	while (<INPUT>)
	{
		chomp;
		if ($task eq 1)
		{
			 $start=moveTask1($_,$start); 
		}
		if ($task eq 2)
		{
			 $start=moveTask2($_,$start); 
		}
		$result= $result.$start;
		print "Next number: $start\n";
	}
	close INPUT;

print "Result = $result \n";
