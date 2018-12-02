#!/usr/bin/perl

use strict;
use warnings;

# First Part
# sqrt(265149)=514.92
# 514*514=264196
# 265149-264196=953
# 953-514=439
# 439-(514/2)=182
# 264712 +(514/2)=  264969
# 265149-264969=180 ## 180 HORIZONTAL MOVES
# (514/2)= 257 vertical moves
# 257+180+1=438

###
#
#   264197  264196
#   .   
#.
#
#   .
#   
#   264712.......     264969                 265227


###Second Part
my @grid;
for my $count (1..512)
{
	for my $innerCount (1..512)
	{
		$grid[$count][$innerCount]=0;
	}
}


print "3-2:".$grid[3][2]."\n";
$grid[257][180]=1;
$grid[258][180]=1;
$grid[258][181]=2;
$grid[257][181]=4;
#$grid[256][181]=&makeNextNumber(256,181);
my $position=4;
my $hori=257;
my $vert=181;
my $lineLength = 2;
my $side=0;
			print "POSTIION ".$position."  : NUMBER:"." Coord: ".($hori-257)." - ". ($vert-180)."\n";
	$hori--;

while (1)
{
	for (my $sideCount=1;$sideCount<=4;$sideCount++)
	{
		for (my $count=1;$count<=$lineLength;$count++)
		{
			$position++;
			my $value = &makeNextNumber($hori,$vert);
			if ($value > 265149) {print "VALUE:".$value."\n"; die;}
			$grid[$hori][$vert]=$value;
			print "POSTIION ".$position."  : NUMBER:".$value." Coord: ".($hori-257)." - ". ($vert-180)."\n";
			
			if ($sideCount==1){$vert--}
			if ($sideCount==2){$hori++}
			if ($sideCount==3){$vert++}
			if ($sideCount==4){$hori--}
			
			
		}
		if ($sideCount==1){$lineLength++}
		if ($sideCount==3){$lineLength++}
	}
	
}



sub makeNextNumber
{
	my $hori = $_[0];
	my $vert = $_[1];
	
	my $total = 0; 
	$total += $grid[$hori-1][$vert]; 
	$total += $grid[$hori -1][$vert -1];
	$total += $grid[$hori][$vert -1];
	$total += $grid[$hori +1][$vert -1];
	$total += $grid[$hori +1][$vert];
	$total += $grid[$hori +1][$vert+1];
	$total += $grid[$hori][$vert +1];
	$total += $grid[$hori-1][$vert +1];
return $total;
	
}
