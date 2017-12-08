#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";
#my $inputFileName = "./input_test.txt";

my %nodes;



# fwft (72) -> ktlj, cntj, xhth
## @children == (<level>,<Weight>,[<child>..])
open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";
while (<INPUTFILE>)
{
	chomp;
	my @line = split(/[,() \t]+/,$_);
	my @children = (-1,$line[1],@line[3..$#line]); ## Set the level to -1 initially
	$nodes{$line[0]} = \@children;
}
close INPUTFILE;

#print "NODE: ".$nodes{fwft}[0]."\n";
#print "NODE: ".$nodes{fwft}[1]."\n";
#print "NODE: ".$nodes{fwft}[2]."\n";
#print "NODE: ".$nodes{fwft}[3]."\n";
#print "NODE: ".$nodes{fwft}[4]."\n";

## Set levels
	my %parents= %nodes;
	my $level=0;
	my @levels;
	
while ((scalar keys %parents) > 0)
{	
	print "NUMPARENTS:".(scalar keys %parents)."\n";
	print "LEVEL:".$level."\n";
	#<>;
	my @thisLevel;
	foreach ( keys %parents)
	{
		my $node=$_;
		#print "PARENT Node:".$node."\n";
		#foreach($nodes{$node}){print "   ".$_."\n";}
		#print "   ".$parents{$node}[0]."\n";
		#print "   ".$parents{$node}[1]."\n";
		#print "   ".$parents{$node}[2]."\n";
		#print "   ".$parents{$node}[3]."\n";
		#print "   ".$parents{$node}[4]."\n";
		#print "   ".$nodes{$node}[5]."\n";
		if (!$parents{$node}[2])
		{
			#print "DELETING Child ".$node." from parents\n";
			##  No more children
			$nodes{$node}[0]=$level;
			push @thisLevel, $node;
			delete($parents{$node});
		}
	}
	$levels[$level]=\@thisLevel;
	## Remove all references to nodes at this level from their parent
	
	print "Number in level $level ".@thisLevel."\n";
	foreach my $thisChild (@thisLevel)
	{
		#foreach (@thisLevel) {print "  ".$_."\n";}
		#print "This Child: ".$thisChild."\n";
		my $found=0;
		foreach my $thisParent ( keys %parents)
		{
			#print "This parent: ".$thisParent."\n";#" -- ".$parents{$thisParent}."\n";# " -- ".$parents{$thisParent}[0]." -- ".$parents{$thisParent}[1]." -- ".$parents{$thisParent}[2]."\n";
			
			my @children;
			foreach(@{$parents{$thisParent}})
			{
				#print "Pushing ".$_."\n";
				push @children, $_;
			}
			#my @children=@{$parents{$thisParent}};
			
			#print "Number of children of this parent: " .scalar @children."\n";

			for (my $childNum=2;$childNum<=$#children;$childNum++)
			{
				#print "Comparing ".$thisChild ." with ".$children[$childNum]."\n";
				if ($thisChild eq $children[$childNum])
				{
					$found=1;
					#print "Now Parent $thisParent has ".$#children." children.\n";
					splice @children,$childNum,1;
					$parents{$thisParent}=\@children;
					#print "Now Parent $thisParent only has ".$#children." children.".scalar $parents{$thisParent}."\n";
					last;
				}
			}
			if ($found == 1){ last}
			
		}
	}
	$level++;
}

for (my $count=0; $count<=$#levels;$count++)
{
	print "LEVEL ".$count."\n";
	foreach (@{$levels[$count]})
	{
		print "  ".$_."\n";
	}
	
}