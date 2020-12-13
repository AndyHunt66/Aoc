#!/usr/bin/perl


#my $input = './testInput.txt';
my $input = './input.txt';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $highestSeatId = 0;
for ( @entries )
{
    my $row;
    my $seat;
    my $seatId;
    #print "Entry: $_ \n";
    my $individualFields = $_ =~  s/F/0/gr
     =~  s/B/1/gr
     =~  s/L/0/gr
     =~  s/R/1/gr;
    
    #print $individualFields."\n";
    if ($individualFields =~ /^(\d{7})(\d{3})$/)
    {
        $row = oct("0b".$1);
        $seat = oct("0b".$2);
        $seatId = ($row * 8) + $seat;
    }
    else
    {
        die "Can't understand boarding pass\n";
    }
    print "Row: ".$row." \n";
    print "Seat: ".$seat ." \n";
    print "Seat ID: ". $seatId."\n";
    
    if ($seatId > $highestSeatId )
    {
        $highestSeatId = $seatId;
    }
    #print "This person answered ". (keys %answers) ." questions\n";
    #<>;
    
}

#Add the last group
## Make sure to add an extra blank line at the end of the input file, so that the last group is processed

print "Highest Seat ID: ".$highestSeatId."\n";
    die;

