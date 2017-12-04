#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my %places;

my $x=0;
my $y=0;
$places{$x.",".$y}=1;
while (<INPUTFILE>)
{
  my @directions = split(//,$_);
  foreach (@directions)
  {
    if ($_ eq "<"){$x--}
    if ($_ eq ">"){$x++}
    if ($_ eq "^"){$y++}
    if ($_ eq "v"){$y--}

    if ( $places{$x.",".$y}){$places{$x.",".$y}++}
    else {$places{$x.",".$y}=1}
  }
}

my $multiples=0;
foreach  (keys %places)
{
  if ($places{$_} > 1)
  {
     $multiples++;
  }
}
print "MULTIPLES: ".$multiples."\n";
## 1762 is too low
