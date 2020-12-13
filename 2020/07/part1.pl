#!/usr/bin/perl

#my $input = './testinput.txt';
my $input = './input';
my @entries;

open INPUTFILE, "$input" or die "Can't open input file $input for reading - $! \n";
chomp(@entries = <INPUTFILE>);
close INPUTFILE;

my @bags; ## single list of "parent" bags
my %parents; ## e.g. $parents{"light blue"} = ["dark olive", "light taupe"] ## Light Blue can be carried in a Dark Olive or a Light taupe bag

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
            push @bags, $1;

            ## Child bag
            #print "Adding child bag $3 \n";
            push @{ $parents{$3} }, $parent;

        }
        elsif (/^ (\d+) (.*) bag(|s)/)
        {
            ## Child bag
            #print "Adding child bag $2 \n";
            push @{ $parents{$2} }, $parent;
        }
        elsif (/^(.*) bags contain no other bags\./)
        {
            ## Child bag
            #print "Adding child bag $1 \n";
            push @bags, $1 ;
        }
        else
        {
            die "I don't understand this: $_ \n";
        }
    }
    
}
print "All the bags:\n";
foreach (@bags)
{
    print "  ".$_."\n";
}

print "\n\n";
foreach (keys %parents)
{
    print $_." can be carried in \n";
    foreach (@{ $parents{$_} })
    {
        print "   ".$_. "\n";
    }
}

my $myBag = "shiny gold";
print "\n\n\n";


my %allParents;
getRecursiveParents($myBag);

print "My $myBag bag can be carried in \n";
foreach (keys %allParents)
{
    print "  $_ \n";
}
print "That's ".(%allParents) ."!\n";
    die;

sub getRecursiveParents
{
    my $thisBag = shift;
    #print "This bag: $thisBag\n";
    foreach (@{ $parents{$thisBag}})
    {
        $allParents{$_}=1;
        getRecursiveParents($_);
    }
}