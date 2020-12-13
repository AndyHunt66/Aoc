#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw( min max );

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
my $input = './input';

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;
my $departtime = $entries[0];
my @busses = split /[x,]+/ , $entries[1];
print "Depart time : ".$departtime. "\n";
print "Bus 3 = ".$busses[3]."\n";

my @nextBus= ($busses[0] , $busses[0]- ($departtime % $busses[0]));
print "Frist bus: ". $nextBus[0]." leaves in ".$nextBus[1]."\n";
for (my $i =1; $i <= $#busses; $i++)
{
    if ( ($busses[$i]- ($departtime % $busses[$i]) ) < $nextBus[1])
    {
        @nextBus= ($busses[$i] , $busses[$i]- ($departtime % $busses[$i]));
    }
}

print "Bus ".$nextBus[0]." leaves in ".$nextBus[1]." minutes.\n";
print "Answer ".($nextBus[0] * $nextBus[1])."\n";
