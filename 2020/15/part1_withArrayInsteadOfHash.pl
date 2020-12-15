#!/usr/bin/perl
use strict;
use warnings;

#my $input = './testinput.txt'; 
#my $input = './testinput2.txt';
my $input = './input';

my $MAXTURN = 30000000;

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

@entries = split /,/ , $entries[0];

my $startingTime = localtime();

my @track;
my $turn = 0;
my $nextNumber = 0;
my $thisNumber = 0;
# Read the numbers on the paper
foreach (@entries)
{
    $turn++;
    $track[$_]=$turn;
}

## Start the game
while (1)
{
    $turn++;
    $thisNumber = $nextNumber;                                 
    #print $turn." " . $thisNumber."\n";                    
    if ($turn == $MAXTURN)
    {
        print "Final number: ".$thisNumber."\n";
        my $endTime = localtime();
        print "Started : ".$startingTime."\n";
        print "Ended   : ".$endTime."\n";
        die;
    }
   if ( defined $track[$thisNumber])                          
    { 
        $nextNumber = ($turn  ) - $track[$thisNumber];    
    }
    else 
    {
        $nextNumber = 0;
    }
    $track[$thisNumber]=$turn;
}
    