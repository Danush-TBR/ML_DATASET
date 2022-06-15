1.	It begins with the original set S as the root node.
2.	On each iteration of the algorithm, it iterates through the very unused attribute of the set S and calculates Entropy(H) and Information gain (IG) of this attribute.
3.	It then selects the attribute which has the smallest Entropy or Largest Information gain.
4.	The set S is then split by the selected attribute to produce a subset of the data.
5.	The algorithm continues to recur on each subset, considering only attributes never selected before.
