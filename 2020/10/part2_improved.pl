#!/usr/bin/perl
use strict;
use warnings;

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
my $input = './input';

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

@entries = sort { $a <=> $b } @entries;
unshift @entries, 0; ## add the zero on the beginning for the power source
push @entries, ($entries[$#entries] + 3); ## add on the device 


#my @chunks; # A chunk is subset of the sorted adapters, bound on each end by a difference of 3. 

my @thisChunk;
my $runningTotal = 1;

for (my $i = 0 ; $i < $#entries; $i++)
{
    push @thisChunk, $entries[$i];
    if (($entries[$i+1] - $entries[$i]) == 3)
    {
        if ($#thisChunk == 2)
        {
            $runningTotal = $runningTotal * 2   ## 2 possible paths through a chunk of 3
        }
        if ($#thisChunk == 3)
        {
            $runningTotal = $runningTotal * 4
        }
        if ($#thisChunk == 4)
        {
            $runningTotal = $runningTotal * 7
        }
        if ($#thisChunk > 4) { die "oops - didn't think we'd get one this big! \n";}

        @thisChunk = ();
    }
}



print "Total : ".$runningTotal."\n";
die;

