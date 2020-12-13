#!/usr/bin/perl

#my $input = './testinput.txt';
#my $input = './testinput2.txt';
my $input = './input';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my @bags; ## single list of "parent" bags
my %children ; ## e.g. $children{"light blue"} = ["dark olive", "light taupe", "light taupe"] ## Light Blue must carry one Dark Olive and 2 Light taupe bags

for ( @entries )
{
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
    my $parent = "";
    foreach (split /,/)
    {
        #print $_ . "\n";
        if (/^(.*) bags contain (\d+) (.*) bag(|s)(|\.)$/)
        {
            ## Parent bag
            #print "Adding parent bag $1 \n";
            $parent=$1;

            ## Child bag
            #print "Adding child bag $3 \n";
            for (1..$2)
            {
                push @{ $children{$parent} }, $3;
            }

        }
        elsif (/^ (\d+) (.*) bag(|s)/)
        {
            ## Child bag
            #print "Adding child bag $2 \n";
            for (1..$1)
            {
                push @{ $children{$parent} }, $2;
            }   
        }
        elsif (/^(.*) bags contain no other bags\./)
        {
            ## Child bag
            #print "Adding child bag $1 \n";
        }
        else
        {
            die "I don't understand this: $_ \n";
        }
    }
    
}



my $myBag = "shiny gold";
print "\n\n\n";


my %allChildren;
getRecursiveChildren($myBag);
my $numberOfBags=0;
foreach ( keys %allChildren)
{
    $numberOfBags = $numberOfBags + $allChildren{$_};
}
print "My $myBag bag must carry $numberOfBags \n";




    die;

sub getRecursiveChildren
{
    my $thisBag = shift;
    print "This bag: $thisBag\n";
    foreach (@{ $children{$thisBag}})
    {
        $allChildren{$_}++;
        getRecursiveChildren($_);
    }
}