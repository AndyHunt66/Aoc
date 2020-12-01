#!/usr/bin/perl

my $testInputFile = './part1_testInput.txt';
my $inputFile = './part1_input.txt';

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
        print "Trying $target + $_ = ".($target + $_) . "\n";
        if ( ($target + $_ ) == 2020 )
        {
            print $target * $_ . "\n";
            die;
        }

    }
}
  print "Couldn't find it....\n";
    die;

