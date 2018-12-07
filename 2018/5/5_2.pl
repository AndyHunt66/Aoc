#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";


my $shortest=11946;
for ("a".."z")
{
	my $letter = $_;
	my $full = <INPUTFILE>;
	chomp($full);
	my @full = split //, $full;
	my $combined = 0;
	while (1)
	{
		for (my $count = 0; $count < $#full;)
		{
			if ($full[$count]=~/$letter/i)
			{
				splice(@full, $count,1);
				next;
			}
			#	for(0..5)
			#	{
			#		print $full[$count+$_];
			#	}
			#	print "\n";#<>;
			if (($full[$count] =~ /$full[$count + 1]/i) &&
				($full[$count] !~ /$full[$count + 1]/))
			{
				splice(@full, $count, 2);
				$combined++;
			}
			else
			{
				$count++;
			}
		}
		print "Finished pass - $combined combined - size: ".scalar @full."\n";
		if ($combined == 0)
		{
			print "Final string: ";
			foreach (@full)
			{
				print;
			}
			print "\n";
			print "$letter - Size: " . scalar @full . "\n";
			if ((scalar @full) < $shortest )
			{
				$shortest= (scalar @full);
			}
			close INPUTFILE;
			open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
			last;
		}
		$combined = 0;
	}

}
print "Shortest :".$shortest."\n";