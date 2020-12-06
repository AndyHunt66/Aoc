#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
my @data;

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
while (<INPUTFILE>)
{
    @data = split(/ /,$_);
}

my $metadataTotal = 0;
while ((scalar @data) > 0)
{
    $metadata &extractNode(@data);

}



