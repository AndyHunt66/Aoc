#!/bin/perl

use strict;
use warnings;
use Digest::MD5 qw(md5 md5_hex md5_base64);
my $keyStart  = $ARGV[0];






for (my $count=0; 1;$count++)
{
	my $md5 = md5_hex($keyStart.$count);	
	print $md5."\n";
	if ( $md5 =~ /^000000/) 
	{
		print "Answer is :". $count."\n"; die;
	}
			
}