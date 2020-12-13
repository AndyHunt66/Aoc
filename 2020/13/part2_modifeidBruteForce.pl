#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw( min max );

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
#my $input = './testinput5.txt';
my $input = './input';

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $startingTime = localtime();
my @busses = split /,/ , $entries[1];

## Get a list of bus positions, in order of their magnitude, descending
my %bussesMagnitude;
my $biggestPosition = 0;
for(my $i=0; $i<=$#busses;$i++)
{
    if ($busses[$i] eq "x")
    {
        next;
    }
    $bussesMagnitude{$i}=$busses[$i];
    if ($busses[$i] > $busses[$biggestPosition])
    {
        $biggestPosition = $i;
    }
}
my @bussesSorted = (sort { $bussesMagnitude{$b} <=> $bussesMagnitude{$a} } keys %bussesMagnitude) ;


foreach (@bussesSorted)
{
    print "Position ". $_." bus number ".$busses[$_]."\n";
}


## Brute force
my $multiple = 12270;
my $message = "";
while (1)
{
    my $base = ($multiple * $busses[$bussesSorted[0]] ) - $biggestPosition;
    # if ($base < 100000000000000) 
    # {
    #     $base = 100000000000000;
    #     $multiple++;
    #     while ( ( $base - $biggestPosition ) % $busses[$bussesSorted[0]] != 0)
    #     {
    #         $base++;
    #     }
    #     $multiple = ( $base - $biggestPosition ) / $busses[$bussesSorted[0]] ;
    #     print $multiple; die;
    # }
    $message =  "Testing timestamp ".$base.".";
    my $ok = 1;
    foreach (@bussesSorted)
    {
        my $busPosition = $_;
        if (($base + $busPosition) % $busses[$busPosition] != 0)
        {
            $message = $message . " Bus ".$busses[$busPosition] ." missed.\n";
            $ok = 0;
            if (($multiple % 1000000) == 0)
            {
                print $message;
            }
            $message = "";
            last;
        }
        else
        {
            $message = $message .  " ".$busses[$busPosition]. " is ok.";
        }

    }
    if ($ok == 1)
    {
        print $message ."\n";
        my $endTime = localtime();
        print "started ".$startingTime."\nFinished ".$endTime."\n";
        die  " Found base ".$base."\n";
    }
    else 
    {
        $multiple = $multiple + 21443;
    }
}


