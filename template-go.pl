#!perl

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

print "Day ".$star."\n\n";


## Single line reading
my $input = <INPUT>;
chomp $input;


print "InputFileName = $inputFileName \n";
print "hello";