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
           # print "  Field $1 = $2\n"
        }
        else
        {
            die "Don't understand this entry: $_ \n";
        }
    }
    if ($#individualFields == -1)
    {
        print "This passport : pid = ".$passport{"pid"}."\n";
        if ( validate(\%passport) == 1)
        {
            print "Valid \n";
            $runningTotal++;
        }
        else
        {
            print "Invalid\n";
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


sub validate
{
    my $passportRef = shift;
    foreach(keys %{$passportRef})
    {
        print "  ".$_. " ".$passportRef->{$_}."\n";
    }
    ## byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if ((! defined $passportRef->{"byr"}) || ($passportRef->{"byr"} !~ m/^\d{4}$/ ) || ($passportRef->{"byr"} < 1920 ) || ($passportRef->{"byr"} > 2002 ))
    {
        return 0;
    }

    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if ((! defined $passportRef->{"iyr"}) || ($passportRef->{"iyr"} !~ m/^\d{4}$/ ) || ($passportRef->{"iyr"} < 2010 ) || ($passportRef->{"iyr"} > 2020 ))
    {
        return 0;
    }

    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if ((! defined $passportRef->{"eyr"}) || ($passportRef->{"eyr"} !~ m/^\d{4}$/ ) || ($passportRef->{"eyr"} < 2020 ) || ($passportRef->{"eyr"} > 2030 ))
    {
        return 0;
    }

    #hgt (Height) - a number followed by either cm or in:
    if ((! defined $passportRef->{"hgt"}) || ($passportRef->{"hgt"} !~ m/^(\d+)(cm|in)$/ ) )
    {
        return 0;
    }
    elsif (($2 eq "cm") && (($1 < 150) || ($1 > 193)) )
    #    If cm, the number must be at least 150 and at most 193.
    {
        return 0;
    }
    #    If in, the number must be at least 59 and at most 76.
    elsif (($2 eq "in") && ( ($1 < 59) || ($1 > 76)))
    {
        return 0;
    }

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if ((! defined $passportRef->{"hcl"}) || ($passportRef->{"hcl"} !~ m/^#([0-9a-f]{6})$/ ) )
    {
        return 0;
    }

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if ((! defined $passportRef->{"ecl"}) || ($passportRef->{"ecl"} !~ m/^(amb|blu|brn|gry|grn|hzl|oth)$/ ) )
    {
        return 0;
    }

    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    if ((! defined $passportRef->{"pid"}) || ($passportRef->{"pid"} !~ m/^(\d{9})$/ ) )
    {
        return 0;
    }

    #cid (Country ID) - ignored, missing or not.

    return 1;
}
