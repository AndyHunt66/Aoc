#!/usr/bin/perl

#my $input = './testInput.txt';
my $input = './input.txt';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $runningTotal = 0;
my %answers;
for ( @entries )
{
    my @individualAnswers= split //;
    foreach (@individualAnswers)
    {
        print "    This answer is $_ \n";
        $answers{$_}=1;
    }
    if ($#individualAnswers == -1)
    {
        print "   This group answered ". (keys %answers) ." questions\n";
        for (keys %answers)
        {
            print "          ".$_ ."\n";
        }
        $runningTotal += keys %answers;
        %answers = ();
    }
    #print "This person answered ". (keys %answers) ." questions\n";
    #<>;
}

#Add the last group
print "   This group answered ". (keys %answers) ." questions\n";
$runningTotal += keys %answers;

print "Total = $runningTotal \n";
    die;