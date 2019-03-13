# Decision tree implementation

A decision tree is a binary tree where internal nodes have boolean expressions as datum and each external node has as datum a final decision (outcome) value. Each of the pair of branches emerging from a node are labeled as True and False, correspondingly. The boolean expressions at the internal nodes have variables in them.

When program is asked to query the decision tree with a set of variable value settings, algorithm works as follows:
1. Start at the root node.
2. If the node you are at is an internal node then consider the boolean expression of the node. Evaluate it with the given variable settings. If the outcome is True proceed to the True branch of the node, otherwise to the False branch.
3. Else, if the node is an exterior node (a leaf node), you have reached the end. The datum of the node is the outcome, return it.
4. Continue from item (2).

The user needs to give 2 inputs which are decision tree list (representation of the decision tree) and variable value list (list of two-tuples****), respectively.

**** Each two-tuple is representing the value setting of one variable and is of the form:
(variable_i,value_i) variable_i is a string. value_i is either a number or a string.

The list representation of the binary tree is trivial and is defined as:

Internal node: The representation of the node datum is the first element of a ternary list. For the internal node datum is a boolean expression in prefix
form. The representations for the left child and right child are located at the second and third element, respectively, of the ternary list.

External node: The representation of the leaf node datum is a string. It is the outcome value if the query ends at that node.

An example of decision tree is [α,[!,[δ,"x","y"],[ξ,"z","t"]],[γ,"u","v"]], where α,!,γ,δ,ξ are boolean expressions and "x","y","z","t","u","v" are external nodes (outcomes), left branchings stand for the True case and right branchings stand for the False case and note that external nodes are not represented by lists but they are represented with strings.

The prefix form boolean expression which is the datum for the internal node is a list. The first element of this list is a string representing an operator. The operators which can appear in tree are "==", "!=", "<", ">", "in", "and", "or", "not", user should not provide any other operators.


I/O Example:

Please enter the decision tree list:

	[["in", "TNM", [1, 2, 3]], [["and", ["not", ["<", "Salb", 3.65]], [">", "LDH", 200]],[["<", "Age", 71.5], "probably survive", "fiftyfifty"], "fiftyfifty"],[["not", ["<", "Salb", 3.85]],[["<", "Age", 78.5],[["not", ["<", "DiaBP", 103]],"survive",[["or", ["not", ["<", "BMI", 30.5]], [">", "GGT", 150]],"probably survive",[["not", ["<", "SysBP", 119]],"fiftyfifty",[["not", ["<", "BMI", 25.5]], "probably survive", "probably goner"]]]],"mortingen st."],[["<", "Age", 69.5], "fiftyfifty", "probably goner"]]]

Please enter the variable value list:

	[("TNM", 4),("Salb", 3.9),("LDH", 210),("Age", 66),("DiaBP", 96),("BMI", 27.8),("GGT", 157),("SysBP", 105)]


	probably survive