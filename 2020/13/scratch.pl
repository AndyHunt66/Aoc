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

my $startingTime = localtime();
my @busses = split /,/ , $entries[1];



## Get a list of bus positions, in order of their magnitude, descending
my %bussesMagnitude;
my $biggestPosition = 0;
for(my $i=0; $i<=$#busses;$i++)
{
    if ($busses[$i] eq "x")
    {
        next;
    }
    $bussesMagnitude{$i}=$busses[$i];
    if ($busses[$i] > $busses[$biggestPosition])
    {
        $biggestPosition = $i;
    }
}
my @bussesSorted = (sort { $bussesMagnitude{$b} <=> $bussesMagnitude{$a} } keys %bussesMagnitude) ;


foreach (@bussesSorted)
{
    print "Position ". $_." bus number ".$busses[$_]."\n";
}

my $base = $busses[$bussesSorted[0]] ; 
  print "Starting Base; ".$base."\n";

my $multiple = 1;
while (1)
{
    my $target = ( $base * $multiple ) - $bussesSorted[0];
    if ( ( $target + $bussesSorted[1])  % $busses[$bussesSorted[1]] == 0 )
    {
        if ( ( $target + $bussesSorted[2] ) % $busses[$bussesSorted[2]]  == 0)
        {
       print "Found at Multiple ".$multiple."\n";
       print "Second multiple ". ( ($target + $bussesSorted[1]) / $busses[$bussesSorted[1]] )."\n";
       print "Third multiple ". ( ($target + $bussesSorted[2]) / $busses[$bussesSorted[2]] )."\n";
       print "Target ".$target."\n";
       print $bussesSorted[1] . "\n";
       print  $busses[$bussesSorted[1]] ."\n";
     
           print "Third matches\n"; 

            if ( ( $target + $bussesSorted[3]) % $busses[$bussesSorted[3]] == 0)
            {
                # print "fourth matches \n";
                die;
                if ( ( $target + $bussesSorted[4]) % $busses[$bussesSorted[4]] == 0)
                {
                    print "fifth matches  $target\n";
                    # print "Target ".$target."\n";       die;
                    if ( ( $target + $bussesSorted[5]) % $busses[$bussesSorted[5]] == 0)
                    {
                        print "sixth matches \n";
                        print "Target ".$target."\n";  
                        if ( ( $target + $bussesSorted[6]) % $busses[$bussesSorted[6]] == 0)
                        {
                            print "seventh matches \n";
                            print "Target ".$target."\n";       last;
#                         {
#                             print "Seventh matches\n";
#                             if ( ( $target -67 ) % $eigth == 0)
#                             {
#                                 print "eigth matches\n";
#                                 if ( ( $target -37 ) % $ninth == 0)
#                                 {
#                                     print "ninth matches\n";
#                                     die;
#                                 }
                    
#                             }

                        }
                    }
                }
            }
        }
    }
    else
    {
     #   print "Target ".$target."  multiple ".$multiple." skipped \n";
    }
    $multiple++;
}

my $endTime = localtime();
print "Started: ".$startingTime."\n";
print "Ended: ".$endTime."\n";
