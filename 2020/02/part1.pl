#!/usr/bin/perl

my $testInputFile = './part1_testInput.txt';
my $inputFile = './part1_input.txt';

my $input = $inputFile;

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $valid = 0;
my $invalid = 0;
for ( @entries )
{
    my $line = $_ ;
    if (/^(\d+)-(\d+) (\w): (\w+)$/)
    {
        $lower = $1;
        $upper = $2;
        $letter= $3;
        $pass  = $4;
        print "$lower  - $upper - $letter - $pass ";
        my $count = () = $pass =~ /$letter/g;
        if (($lower <= $count) && ($count <= $upper) )
        {
            print "- valid ";
            $valid++;
        }
        else
        {
            print "- invalid ";
            $invalid++;
        }
        print "- $letter occurs $count times \n";
    }
    else
    {
        die "couldn't parse input $line - $0 \n";
    }
    #<>;
}

  print "Valid  : $valid \n";
  print "InValid: $invalid \n";
    die;

