#!/usr/bin/perl

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
my $input = './input';

my @entries;
open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my $MAGIC_NUMBER = 624;
my @program ;

for ( @entries )
{
    my @line;
    (my $op, my $value )= (split / /, $_);
    $line[0]=$op;
    $line[1]=$value;
    push @program, \@line;
}
## Just makes it easier to look at the input if the program is a 1-based array
my  @line;
    $line[0]="nop";
    $line[1]="0";
    unshift @program, \@line;


for (my $i=0; $i<$#program ; $i++)
{
    if ($program[$i][0] eq "nop")
    {
        my $total = $i + $program[$i][1];
        print $i." - ". $total ." \n";
    }
}
#die;
print "Line 1 op = ".$program[1]->[0]."\n";
print "Line 1 value = ".$program[1]->[1]."\n";
print "program length : ".$#program."\n";
## Run The program
    for ($m = 0 ; $m <=$#program; $m++)
    {
        my $thisOp = $program[$m][0];
        if ($program[$m][0] eq "jmp")
        {
            print "Changing statement $m to nop\n";
            $program[$m][0] = "nop";
        }
        elsif ($program[$m][0] eq "nop")
        {
            print "Changing statement $m to jmp\n";
            $program[$m][0] = "jmp";
        }

my $pointer = 0;
my $acc = 0;
my %visited;
my $highestVisited = 0;

my $found = 0;


while (1)
{
    if ($pointer > $highestVisited) { $highestVisited = $pointer}
    $visited{$pointer} = 1;
    if ($program[$pointer][0] eq "end")
    {

        die "Found it - Acc; $acc  -- pointer : $pointer \n";
    }

    if ($program[$pointer][0] eq "nop")  
    {
        # if (($pointer + $program[$pointer][1]) >= $MAGIC_NUMBER)
        # {
        #     print "Changing instruction $pointer to JMP \n";
        #     print "    ".$pointer . " -- jmp ".$program[$pointer][1]." \n" ;
        #     $pointer = $pointer + $program[$pointer][1];
        #     next;

        # }

#        print $pointer . " -- No-op ".$program[$pointer][1]."\n" ;
        $pointer++;
        next 
    }
    if ($program[$pointer][0] eq "acc")  
    {
 #       print $pointer . " -- Acc ".$program[$pointer][1]." \n" ;
        $acc = $acc + $program[$pointer][1] ;
        $pointer++;
    }
    if ($program[$pointer][0] eq "jmp")  
    { 
  #      print $pointer . " -- jmp ".$program[$pointer][1]." \n" ;
        $pointer = $pointer + $program[$pointer][1];
    }

    if (defined $visited{$pointer})
    {
        print "Terminated abnormally - Program run $m - Highest visited = ".$highestVisited;
        print "     - ACC = ".$acc . "  pointer $pointer \n";
        $found =1;
        last ;
    }
    # if ($pointer > $#program)
    # {
    #     print "Terminated normally - Acc = ".$acc."  pointer : $pointer \n";
    #     die;
    # }
}

            $program[$m][0] = $thisOp;
           
}


die;