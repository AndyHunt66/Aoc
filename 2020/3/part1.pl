#!/usr/bin/perl

#my $inputFile = './part1_testInput.txt';
my $inputFile = './part1_input.txt';



my @entries;
open INPUTFILE, "$inputFile" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $Xs = 0;
my $Os = 0; 
my $jump=0;
my $currentPos = 0 ; ## yeah, but this way, we *move* to the first line
for ( @entries )
{
    if ($jump == 1)
    {
        $jump=0;
        next;
    }
    else
    {
        $jump=1;
    }
    my @line = split(//, $_ );
    $currentPos = ($currentPos + 1) % ($#line + 1);
    if ($line[$currentPos - 1] eq ".")
    {
       $Os++;
    }
    elsif ($line[$currentPos - 1] eq "#")
    {
       $Xs++;
    }
    else
    {
        print "Can't work out where I am.\n";
        print " CurrentPos = $currentPos \n";
        print $line[$currentPos - 1] ."\n";
    }
#<>;

}
print "right 1 down 2\n";
  print "Xs  : $Xs \n";
  print "Os: $Os \n";
    die;

