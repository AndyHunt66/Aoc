#!/usr/bin/perl

my $testInputFile = './part1_testInput.txt';
my $inputFile = './part1_input.txt';

#my $input = $testInputFile;
my $input = $inputFile;

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

while (exists $entries[0] )
{
    my $target = shift @entries;
    for (@entries)
    {
        my $subTarget = $_;

        for (@entries)
        {
            #if ($subTarget == $_) { next;}
            print "Trying $target + $subTarget + $_ = ".($target + $subTarget +  $_) . "\n";
            if ( ($target + $subTarget + $_ ) == 2020 )
            {
                print $target * $subTarget * $_ . "\n";
                die;
            }

        }
    }

}
  print "Couldn't find it....\n";
    die;

