#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';
use Digest::MD5 qw(md5 md5_hex md5_base64);

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2


sub getNextZeros
{
	my $doorId = $_[0];
	my $suffix = $_[1];
	my $hash;
	while (1)
	{
		$hash = md5_hex($doorId.$suffix);
		if (substr($hash,0,5) eq "00000")
		{
#			print "found $hash\n"; 
			return ( $hash, $suffix) ;
		}
		$suffix++;
		#if (($suffix % 100000) == 0) {print "$suffix\n";}
	}
}
sub crack
{
	my $doorId = $_[0];
	my $suffix = "0";
	my $password = "";
	my $hash;
	my $found = "false";
	my @password2 = ("X","X","X","X","X","X","X","X");
	
	if ($task eq "2") 
	{
		while (1)
		{
			($hash,$suffix) = getNextZeros($doorId, $suffix);
			#print "Found a Zero : ".substr($hash, 0,5)." ".substr($hash, 5,1)." ".substr($hash, 6,1)."\n";<STDIN>;
			my $position = substr($hash, 5,1);
			my $character = substr($hash, 6,1);
		if (($position=~/\d/) && ($position < 8))
			{
				print "Position : $position   Character : $character \n";
					if ($password2[$position] eq "X")
					{
						$password2[$position] = $character;
					}
					print "Password: ";
					foreach(@password2){print $_;}
					print "\n";
			}
			### Is Password done yet?
			my $numX=0;
			foreach (@password2)
			{
				if ($_ eq "X") {$numX++;}
			}
			if ($numX == 0) { return join('',@password2);}
			
			$suffix++;
		}
	}

	if (($task eq "1") || ($task eq "test1"))
	{
		while (length($password) < 8)
		{
			($hash, $suffix)  = getNextZeros($doorId, $suffix);
			$password = $password . substr($hash,5,1);
			#if ($suffix % 10000){print $suffix."\n";}
			$suffix++;
		}
		print "New password: $password\n";
	}
	return $password;
		  
}

sub runTests
{
	$task = 1;
	my $code = crack("abc");
	if ($code eq "18f47a30"){print "Test 1 passed!\n";}else{print "Test 1 failed : $code should be 18f47a30 \n";}
	$task = 2;
	$code = crack("abc");
	if ($code eq "05ace8e3"){print "Test 2 passed!\n";}else{print "Test 2 failed : $code should be 05ace8e3 \n";}
	die;
}


if ($star =~ /[\\\/](\d+)-go.pl/)
{
	$star=$1;
}
else
{
	die "I don't even know what day it is... $0 \n";
}
if (defined $ARGV[0])
{
	$task=$ARGV[0];
}	
#my $inputFileName="./".$star."-input.txt";
#open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";


if (substr($task,0,4) eq "test"){runTests();}
print crack("ojvtpuvg");
