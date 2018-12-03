#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my @fabric;

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
        }
    }
}
close INPUTFILE;
open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

while (<INPUTFILE>)
{
    my $clear=1;
    # #1 @ 37,526: 17x23
    my $line = $_;
    my @claim = split(/[ ,:x]/,$line);
    # print "Top left corner = ".$claim[2]." - ".$claim[3]." -- Size : ".$claim[5]." by ".$claim[6]."\n";


    for my $row ($claim[2]..($claim[2]+$claim[5]-1))
    {
        for my $col ($claim[3]..($claim[3]+$claim[6]-1))
        {
            if ($fabric[$row][$col]>1)
            {
                $clear=0;
                next;
            }
        }
        if ($clear==0){next;}
    }
    if ($clear==1)
    {
        print "Found ID ".$claim[0]."\n";
        die;
    }
}
