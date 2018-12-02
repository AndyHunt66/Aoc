#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
my $outputFileName = "./output.txt";

my $cmdLineInput = $ARGV[0];

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
#open OUTPUTFILE, ">$outputFileName" or die "Couldn't open outputFile $outputFileName for writing - $!\n";

my $freq = 0;
my %freqs ;
my $found = 0;
while ($found == 0)
{
    while (<INPUTFILE>)
    {
        /^(\+|-)(\d*)$/;
        if ($1 eq "+")
        {
            $freq += $2;
        }
        else
        {
            $freq -= $2;
        }
        if (defined $freqs{$freq})
        {
            $found = 1;
            last;
        }
        else
        {
            $freqs{$freq}=1;
        }
    }
    close INPUTFILE;
    open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
}
print "Final Frequency= " . $freq;