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
unshift @entries, 0; ## add the zero on the beginning for the pwoer source

my $numEntries = $#entries;
print "Num Entries: ".$#entries."\n";

my @totals ;
push @totals, 0,0,0,0; # respectiely, the # of differences of magnitude 0,1,2,3,4

for (my $i = 0 ; $i < $#entries; $i++)
{
    $totals[$entries[$i+1] - $entries[$i]]++;
}

$totals[3]++; ## add one on the end for the device

foreach (@totals)
{
    print $_."\n";
}

print "Answer : ".$totals[3] * $totals[1]."\n";
die;