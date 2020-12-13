#!/usr/bin/perl

#my $input = './testInput.txt';
my $input = './input.txt';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $runningTotal = 0;
my %answers;
my $peopleInGroup = 0;
for ( @entries )
{
    my @individualAnswers= split //;
    $peopleInGroup++;
    foreach (@individualAnswers)
    {
        print "    Person ".$peopleInGroup." answered $_ \n";
        if ($answers{$_})
        {
            $answers{$_}++;
        }
        else
        {
            $answers{$_}=1;
        }
    }
    if ($#individualAnswers == -1)
    {
        $peopleInGroup--;
        print "   This group answered ". (keys %answers) ." questions\n";
        for (keys %answers)
        {
            print "Answer $_ had ".$answers{$_} ." responses. People in group:  ".$peopleInGroup."\n";
            if ($answers{$_} == $peopleInGroup)
            {
                $runningTotal ++;
            }
        }
        %answers = ();
        $peopleInGroup =0;
    }
    #print "This person answered ". (keys %answers) ." questions\n";
    #<>;
}

#Add the last group
## Make sure to add an extra blank line at the end of the input file, so that the last group is processed

print "Total = $runningTotal \n";
    die;