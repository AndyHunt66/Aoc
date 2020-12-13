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
push @entries, ($entries[$#entries] + 3); ## add on the device (actually, this isn't needed )


my @chunks; # A chunk is subset of the sorted adapters, bound on each end by a difference of 3. 
my @chunkvalues ; # The vlaue for a chunk is the number of different paths through it

my @thisChunk;

for (my $i = 0 ; $i < $#entries; $i++)
{
    push @thisChunk, $entries[$i];
    if (($entries[$i+1] - $entries[$i]) == 3)
    {
        push @chunks, [@thisChunk];
        @thisChunk = ();
    }
}

for (my $i = 0 ; $i <= $#chunks; $i++)
{
    my @chunk = @{$chunks[$i]};
    if ($#chunk <= 1)
    {
        $chunkvalues[$i] = 1;
    }
    if ($#chunk == 2)
    {
        $chunkvalues[$i] = 2;
    }
    if ($#chunk == 3)
    {
        $chunkvalues[$i] = 4;
    }
    if ($#chunk == 4)
    {
        $chunkvalues[$i] = 7;
    }
    

}

my $runningTotal = 1;
print "Chunks 1 : ".$chunks[1][0]."\n";
for (my $i = 0 ; $i <= $#chunks; $i++)
{
    $runningTotal = $runningTotal * $chunkvalues[$i];
    my @chunk = @{$chunks[$i]};
    print "Value:  ".$chunkvalues[$i].",  ";
    foreach (@chunk)
    {
        print "      ".$_ ." ";
    }
    print "\n";

}

print "Total : ".$runningTotal."\n";
die;

