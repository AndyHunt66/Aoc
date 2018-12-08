#!/usr/bin/perl

use strict;
use warnings;

my $inputFileName = "./input.txt";


open INPUTFILE, "$inputFileName" or die "Couldn't open InputFile $inputFileName for reading - $!\n";

my %graph;
while (<INPUTFILE>)
{
    /^Step (.) must be finished before step (.) can begin./;
    my $parent = $1;
    my $child = $2;
    print "1: $1  2: $2\n";
    if ( defined @{$graph{$parent}{"kids"}}[0])
    {
        push (@{$graph{$parent}{"kids"}},$child);
    }
    else
    {
        $graph{$parent}->{"kids"}[0] = $child;
    }
    if (defined @{$graph{$child}{"parents"}}[0])
    {
        push (@{$graph{$child}->{"parents"}},$parent);
    }
    else
    {
        $graph{$2}->{"parents"}[0] = $1;
    }

}

my @taskOrder;
while (scalar (keys %graph) > 0)
{
    my @noParents;
    print "Keys left: ".(scalar (keys %graph))."\n";
    ## Find any tasks who no longer have any parents
    foreach my $taskId (keys %graph)
    {
        if ((!defined $graph{$taskId}{"parents"})|| (scalar( @{$graph{$taskId}{"parents"}}) == 0))
        {
            print "Found $taskId without parents \n";
            ## Add to list of those without parents
            push (@noParents, $taskId);
        }
    }
    @noParents = sort @noParents;

    ## Do the first task
    my $nextTask = shift @noParents;
    push (@taskOrder, $nextTask);

    ## Remove that task from the parent lists of any of this task's kids
    foreach my $child (@{$graph{$nextTask}{"kids"}})
    {
        for (my $count = 0;$count<= scalar (@{$graph{$child}{"parents"}});$count++)
        {
            print "NEXT TASK : ".$nextTask."\n";
            print "CHILD : ".$child."\n";
            print "GRAPH: ".%graph."\n";
            print "GRAPH->CHILD : ".$graph{$child}."\n";
            print "GRAPH->CHILD->Parents : ".$graph{$child}{"parents"}."\n";
            print "GRAPH->CHILD->Parents->COUNT : ".$graph{$child}{"parents"}[$count]."\n";
            if ($graph{$child}{"parents"}[$count] eq $nextTask)
            {
                print "About to reduce this array, by removing $nextTask \n";
                foreach (@{$graph{$child}{"parents"}})
                {
                    print $_." - ";
                }
                print "\n";
                splice (@{$graph{$child}{"parents"}}, $count,1);
                print "Reduce Array : \n";
                foreach (@{$graph{$child}{"parents"}})
                {
                    print $_." - ";
                }
                print "\n";
                #<>;
                last;
            }
        }
    }
    delete ($graph{$nextTask});
    print "TaskOrder: ";
    foreach (@taskOrder)
    {
        print $_;
    }
    print "\n";
}

foreach (@taskOrder)
{
    print $_;
}
print "\n";
