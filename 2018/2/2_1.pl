#!/bin/perl

use strict;
#use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


my $twos =0;
my $threes = 0;
while (<INPUTFILE>)
{
    my $word = $_;
    chomp $word;
    my %letters;
    foreach  my $letter (split (undef, $word))
    {
        if (defined $letters{$letter})
        {
            $letters{$letter}++;
        }
        else
        {
            $letters{$letter}=1;
        }
    }
    print "Word: ".$word." contains ";
    foreach my $letter (keys %letters)
    {
        if ($letters{$letter} == 2)
        {
            $twos++;
            print $letter . " ";
            last;
        }
    }
    print " two times, and ";
    foreach my $letter (keys %letters)
    {
        if ($letters{$letter} == 3)
        {
            $threes++;
            print $letter." ";
            last;
        }
    }
    print " three times \n";

}
my $checksum = $twos * $threes;
print "Final checksum=". $checksum."\n";