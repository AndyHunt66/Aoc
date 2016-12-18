#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2
my $bRows = 6;
my $bCols = 50;

my @board;

sub rect
{
	my $rectX = $_[0];
	my $rectY = $_[1];
	
	for(my $col=0;$col<$rectX;$col++)
	{
		for(my $row=0;$row<$rectY;$row++)
		{
			$board[$col][$row]=1;	
		}			
	}
}

sub printBoard
{
	print "\n";
	for(my $row=0;$row<$bRows;$row++)
	{
		for(my $col=0;$col<$bCols;$col++)
		{
			print $board[$col][$row];	
		}			
		print "\n";
	}
		
	print "\n";
	
	
}
sub rotate
{
	my $dim = $_[0];
	my $target = $_[1];
	my $amount = $_[2];
	
		
	if ($dim eq "row")
	{
		for (1..$amount)
		{
			my $end = $board[$bCols-1][$target];
			for (my $colCount=$bCols-1;$colCount	> 0;$colCount--)
			{
				$board[$colCount][$target]=$board[$colCount-1][$target];
			}	
			$board[0][$target]=$end;
		}
	}
	elsif ($dim eq "column")
	{
		for (1..$amount)
		{
				push @{@board[$target]}, pop @{@board[$target]};
		}	
	}
	
}
## initialise board
for(my $colCount=0;$colCount<$bCols;$colCount++)
{
	my @col;
	for(my $rowCount=0;$rowCount<$bRows;$rowCount++)
	{
		push @col, "0";	
	}
	push @board, \@col;
}

### Tests:
rect(3,2);
printBoard;

rotate("row",1,2);
printBoard;

rotate("column",2,4);
printBoard;



print "Board 3,3: ".$board[3][3]."\n";
print "Board 3,2: ".$board[3][2]."\n";
print "Board 3,1: ".$board[3][1]."\n";
print "Board 2,1: ".$board[2][1]."\n";
print "Board 1,2: ".$board[1][2]."\n";
print "Board 4,0: ".$board[4][0]."\n";

die; 

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
