#!perl

use feature "switch";
use strict;
use warnings;

my $star = $0;
if ($star =~ /\\(\d+)-go.pl/)
{
	$star=$1;
}
else
{
	die "Don't know what day it is... $0 \n";
}
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";

## Single line reading
my $line = <INPUT>;
chomp $line;
my @input = split(",",$line);



print "First Instruction: $input[0] \n";

my @directions=('N','E','S','W');
my $direction = 0;
my @location=(0,0); ## x,y

my %locations;
$locations{"0,0"}=1;
my $arrived = "false";
foreach (@input)
{
	#print "Step: ".$_."\n";
	if (/^ *(\w)(\d*)$/)
	{
		#print "\$1 = $1 \n";
		#print "\$2 = $2 \n";
		my $turn = $1;
		my $steps = $2;
		if ($turn eq "R")
		{
			print "Turning right to walk ".$steps." steps ".$directions[($direction + 1)%4];
			$direction = ($direction + 1 ) % 4;
		}
		elsif ($turn eq "L")
		{
			print "Turning left to walk ".$steps." steps ".$directions[($direction - 1)%4];
			$direction = ($direction - 1)%4;
		}
		
		for (my $step =0;$step < $steps;$step++)
		{
			for ($direction)
			{
				when (0)		{ $location[1] += 1;}
				when (1)    { $location[0] += 1;}
				when (2)		{ $location[1] -= 1;}
				when (3)    { $location[0] -= 1;}
			}
			if (defined $locations{$location[0].",".$location[1]})
			{
				print "\nWe're here!\n";
				$arrived = "true";
				last;
			}
			else
			{
				$locations{$location[0].",".$location[1]}=1;
			}
		}
		if ($arrived eq "true")
		{
			last;
		}
	}
	else 
	{
		die "Don't understand the instruction $_ \n";
	}
	print " to ".$location[0].",".$location[1]."\n";

}


print "Final spot: ".$location[0].",".$location[1]."\n";
print "Distance= ".(abs($location[0]) + abs ($location[1]) ). " blocks.\n"