#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw( min max );

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
#my $input = './testinput5.txt';
my $input = './input';

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my @busses = split /,/ , $entries[1];



## Brute force
my $multiple = 1;
my $message = "";
while (1)
{
    my $base = $multiple * $busses[0];
    print "Testing timestamp ".$base.".";
    my $ok = 1;
    for (my $i = 1; $i <= $#busses; $i++)
    {
        if ($busses[$i] eq "x") 
        { 
            print " x .";
            next;
        }
        if (($base + $i) % $busses[$i] != 0)
        {
            print  " Bus $busses[$i] missed.\n";
            $ok = 0;
            last;
        }
        else
        {
            print " ".$busses[$i]. " is ok.";
        }

    }
    if ($ok == 1)
    {
        die  " Found base ".$base."\n";
    }
    else 
    {
        $ok = 0;
        $multiple++;
    }
}
