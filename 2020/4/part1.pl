#!/usr/bin/perl

#my $input = './testInput.txt';
my $input = './input.txt';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $runningTotal = 0;
my %passport;
for ( @entries )
{
    my @individualFields= split / /;
    foreach (@individualFields)
    {
        if (/^(.*):(.*)$/)
        {
            $passport{$1}=$2;
        }
        else
        {
            die "Don't understand this entry: $_ \n";
        }
    }
    if ($#individualFields == -1)
    {
        my $numberOfFields = keys(%passport);
        if (defined $passport{"cid"})
        {
            if ($numberOfFields == 8)
            {
                print "Valid passport\n";
                $runningTotal++;
            }
            else
            {
                print "Invalid passport\n";
            }
        }
        else
        {
            if ($numberOfFields == 7)
            {
                print "Valid passport\n";
                $runningTotal++;
            }
            else
            {
                print "Invalid passport\n";
            }
        }
        %passport =();
    }

    #print "This person answered ". (keys %answers) ." questions\n";
    #<>;
}

#Add the last group
## Make sure to add an extra blank line at the end of the input file, so that the last group is processed

print "Total = $runningTotal \n";
    die;