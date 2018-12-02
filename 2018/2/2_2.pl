#!/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";

open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


my %words;
while (<INPUTFILE>)
{
    my $word = $_;
    chomp $word;
    $words{$word} = 1;
}
close INPUTFILE;

foreach my $word (keys %words)
{
   # print "WORD: ".$word."\n";

    my @outerWord = (split(//, $word));
    foreach my $innerWord (keys %words)
    {
        my @innerInnerWord = (split(//,$innerWord));
        my $differences=0;
        my $difference=0;
        for (my$count=0;$count<=$#innerInnerWord;$count++)
        {
    #        print "Comparing ".$outerWord[$count] ." with ". $innerInnerWord[$count]." - ";

            if ($outerWord[$count] ne $innerInnerWord[$count])
            {
     #           print "Different \n";
                $differences++;
                $difference=$count;
                if ($differences > 1) { last;}
            }
            else
            {
      #          print "not different\n";
            }

        }
        if ($differences == 1)
        {
            print "Found ".$word." and ".$innerWord."\n";
            print "Difference in position $difference\n";
            splice @outerWord,$difference,1;
            print "Answer: ";
            foreach (@outerWord)
            {
                print;
            }
            print "\n";
            die;
        }
        #print "OuterWord = ".$word." InnerWord = ".$innerWord. " Differences = ".$differences."\n";

    }
}
