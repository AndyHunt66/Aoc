#!/usr/bin/perl

use strict;
use warnings;
no warnings 'experimental';

my $star = $0;   ## Which day of the challenge it is
my $task = 1;    ## Which part of that day's challenge - 1 or 2

sub includesAbba
{
	my $chunk = $_[0];
	if ($chunk=~/(.)(.)\2\1/)
	{
		if ($1 eq $2)
		{
			return "false";
		}
		else
		{
			return "true";
		}
	}
	return "false";	
}
sub includesAba
{
	my $chunk = $_[0];
	my @foundAbas;
	for (my $count=0;$count<length($chunk)-2;$count++)
	{
		my $char=substr($chunk, $count,1);
		my $charPlusOne= substr($chunk, $count+1,1);
		my $charPlusTwo= substr($chunk, $count+2,1);
		
		if ( 
		    ($char eq $charPlusTwo) && 
				($char ne $charPlusOne)  
			 )
		{
			push @foundAbas, $char.$charPlusOne.$charPlusTwo;
		}
		
		
	}
	return @foundAbas;
}
sub supportsSSL
{
	my $address = $_[0];
	my @chunks=split ('[\[\]]',$address);	
	my @supernetAbas;
	my @hypernetBabs;
	for (my $count=0; $count<scalar(@chunks);$count=$count+2)
	{
		 push @supernetAbas, includesAba($chunks[$count]);
	}
	for (my $count=1; $count<scalar(@chunks);$count=$count+2)
	{
		 	push @hypernetBabs, includesAba($chunks[$count]);
	}
	foreach (@supernetAbas)
	{
		my $super = $_;
		foreach(@hypernetBabs)
		{
			my $hyper = $_;
			if ($hyper eq substr($super,1,1).substr($super,0,1).substr($super,1,1))
			{
				print "YES : ".$hyper." - ".$super."\n";
				return "true";
			}
			else
			{
				print "NO  :".$hyper." - ".$super."\n";
			}
			
		}
	}
	return "false"	;
}
sub supportsTLS
{
	my $address = $_[0];
	my $supports = 'false';
	
	my @chunks=split ('[\[\]]',$address);
	## Test the ones from brackets first
	## Every odd numbered item
	for(my $count=1;$count<scalar(@chunks);$count=$count+2)
	{
		if (includesAbba($chunks[$count]) eq "true")
		{
			 return "false";
		}
	}
	## Now test the ones outside the brackets
	## Every even  numbered item
	for(my $count=0;$count<scalar(@chunks);$count= $count+2)
	{
		if (includesAbba($chunks[$count]) eq "true") 
		{
			return "true";
		}
	}
	return "false";
}

sub runTests
{
	my $answer;
	$answer = supportsTLS("abcd[bddb]xyyx");
	if ($answer eq "false") { print "Test 2 passed\n\n"} else {die "Test 2 failed : $answer should be false\n"}
	$answer = supportsTLS("abba[mnop]asdsadsa[fdggf]qrst");
	if ($answer eq "true") { print "Test 1 passed\n\n"} else {die "Test 1 failed : $answer should be true\n"}
	$answer = supportsTLS("aaaa[qwer]tyui");
	if ($answer eq "false") { print "Test 3 passed\n"} else {die "Test 3 failed : $answer should be false\n"}
	$answer = supportsTLS("ioxxoj[asdfgh]zxcvbn");
	if ($answer eq "true") { print "Test 4 passed\n"} else {die "Test 4 failed : $answer should be true\n"}
	
	$answer = supportsSSL("abcdefffgfh[asssgfglll]jkjlj");
	#if ($answer eq "true") { print "Test 5 passed\n"} else {die "Test 5 failed : $answer should be true\n"}

	$answer = supportsSSL("zazbz[bzb]cdb");
	if ($answer eq "true") { print "Test 6 passed\n"} else {die "Test 6 failed : $answer should be true\n"}
	
	
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

if ($task eq "test"){runTests;}
my $inputFileName="./".$star."-input.txt";
open INPUT, "$inputFileName" or die "Can't open Input file ($inputFileName) for reading - $! \n";

print "Day ".$star."\n";
print "Task ".$task."\n\n";
my $supportsTls = 0;
my $noTls = 0;
my $supportsSsl = 0;
my $noSsl = 0;
my $total = 0;
while (<INPUT>)
{
	$total++;
	my $line = $_;
	chomp $line;
	if (supportsTLS($line) eq "true")
	{
		$supportsTls++;
	}
	else
	{
		$noTls++;
	}
	if (supportsSSL($line) eq "true")
	{
		$supportsSsl++;
	}
	else
	{
		$noSsl++;
	}
	
}
print "Supports TLS         : $supportsTls \n";
print "Does not support TLS : $noTls\n";
print "Supports SSL         : $supportsSsl \n";
print "Does not support SSL : $noSsl\n";
print "Total   : $total \n";
