An algorithm is a procedure that takes any of the possible input instances
and transforms it to the desired output.

There are three desirable properties for a good algorithm:
1. correct
2. efficient
3. easy to implement

In industrial settings, any program that seems to give good enough answers 
without slowing the application down is often acceptable, 
regardless of whether a better algorithm exists.

There is a fundamental difference between algorithms, 
procedures that always produce a correct result, 
and heuristics, which may usually do a good job but provide 
no guarantee of correctness.

Mathematical induction is usually the right way 
to verify the correctness of a recursive or incremental insertion algorithm.

### Combinatorial Objects

1. **Permutations** are arrangements, or orderings, of items. 
For example, {1,4,3,2} and {4,3,2,1} are two distinct permutations of the same set 
of four integers. 
Permutations are likely the object in question whenever your problem seeks 
an “arrangement,” “tour,” “ordering,” or “sequence.”
2. **Subsets** represent selections from a set of items. 
For example, {1,3,4} and {2} are two distinct subsets of the first four integers.
Order does not matter in subsets the way it does with permutations, 
so the subsets {1, 3, 4} and {4, 3, 1} would be considered identical. 
Subsets arose as candidate solutions in the movie scheduling problem. 
They are likely the object in question whenever your problem seeks a 
“cluster,” “collection,” “committee,” “group,” “packaging,” or “selection.”
3. **Trees** represent hierarchical relationships between items.
Trees are likely the object in question whenever your problem seeks a 
“hierarchy,” “dominance relationship,” “ancestor/descendant relationship,” 
or “taxonomy.”
4. **Graphs** represent relationships between arbitrary pairs of objects.
Graphs are likely the object in question whenever you seek a “network,” “circuit,” 
“web,” or “relationship.”
5. **Points** define locations in some geometric space. 
For example, the locations of McDonald’s restaurants can be described 
by points on a map/plane. 
Points are likely the object in question whenever your problems work on 
“sites,” “positions,” “data records,” or “locations.”
6. **Polygons** define regions in some geometric spaces. 
For example, the borders of a country can be described by a polygon on a map/plane. 
Polygons and polyhedra are likely the object in question whenever you are working on 
“shapes,” “regions,” “configurations,” or “boundaries.”
**The smallest genuine simple polygon is a triangle**
7. **Strings** represent sequences of characters, or patterns. 
For example, the names of students in a class can be represented by strings. 
Strings are likely the object in question whenever you are dealing with 
“text,” “characters,” “patterns,” or “labels.”

### Proof by Contradiction

The basic scheme of a contradiction argument is as follows:
• Assume that the hypothesis (the statement you want to prove) is false.
• Develop some logical consequences of this assumption.
• Show that one consequence is demonstrably false, 
thereby showing that the assumption is incorrect and the hypothesis is true.

### Estimation

Estimation problems are best solved through some kind of logical reasoning process, 
typically a mix of principled calculations and analogies.
1. **Principled calculations** give the answer as a function of quantities 
that either you already know, can look up on Google, 
or feel confident enough to guess. 
2. **Analogies** reference your past experiences, 
recalling those that seem similar to some aspect of the problem at hand.


# References:

1. The Algorithm Design Manual, Steven S Skiena
