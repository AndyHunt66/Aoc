#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my %places;

my $santaX=0;
my $santaY=0;
my $roboX=0;
my $roboY=0;
$places{"0,0"}=2;
while (<INPUTFILE>)
{
  my @directions = split(//,$_);
  for (my $count=0; $count<=$#directions;$count++)
  {
  	if ($count %2 == 1)
  	{
 	    if ($directions[$count] eq "<"){$santaX--}
	    if ($directions[$count] eq ">"){$santaX++}
	    if ($directions[$count] eq "^"){$santaY++}
 	    if ($directions[$count] eq "v"){$santaY--}
	    if ( $places{$santaX.",".$santaY}){$places{$santaX.",".$santaY}++}
  	  else {$places{$santaX.",".$santaY}=1}
  	}
  	else
  	{
 	    if ($directions[$count] eq "<"){$roboX--}
	    if ($directions[$count] eq ">"){$roboX++}
	    if ($directions[$count] eq "^"){$roboY++}
 	    if ($directions[$count] eq "v"){$roboY--}
	    if ( $places{$roboX.",".$roboY}){$places{$roboX.",".$roboY}++}
  	  else {$places{$roboX.",".$roboY}=1}
  	}

  }
}

print "HOUSES: ".(keys %places)."\n";
