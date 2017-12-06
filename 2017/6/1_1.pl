#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my %splits;

my @banks;

while (<INPUTFILE>)
{
  @banks = split(//,$_);
}
close INPUTFILE;

while(1)
{
  $biggest=7;
  foreach (@banks)
{


}


}
die;


