#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my @fabric;


my %totals;
while (<INPUTFILE>)
{
    # #1 @ 37,526: 17x23
    my $line = $_;
    my @claim = split(/[ ,:x]/,$line);
   # print "Top left corner = ".$claim[2]." - ".$claim[3]." -- Size : ".$claim[5]." by ".$claim[6]."\n";


    for my $row ($claim[2]..($claim[2]+$claim[5]-1))
    {
        for my $col ($claim[3]..($claim[3]+$claim[6]-1))
        {
            $fabric[$row][$col]++;
            if ($fabric[$row][$col] > 1)
            {
               $totals{$row."-".$col}=1;
            }
        }
    }
    #<>;

}

print "Total: ";
my $total = keys %totals;
print $total."\n";