"""
Source code for SyGuS solver based on constraint solving.  

The key component is representing a SyGuS grammar using variables from SMT theories, primarily booleans. The 
representation maps the choices in rule applications for various nonterminals in the grammar into valuations over 
said variables. An accompanying 'evaluation' formula that represents the semantics of the function chosen by given 
rule applications (or correspondingly, valuations over variables) can be computed.  An SMT solver then checks for 
assignments to these representation variables such that the constraints in the original SyGuS problem are satisfied, 
effectively acting as a synthesis engine.  

NOTE: The implementation currently does not use logically consistent objects with defined interfaces to represent 
various mathematically well-defined aspects of the data including types, rather choosing to represent these using 
strings (in SMT-Lib format). This essentially makes the implementation a 'wrapper' around any standard SMT solver to 
create a SyGuS solver based on constraint solving techniques that is agnostic to the particular syntax of the 
underlying SMT solver for theories such as sets with no defined standard while still providing synthesis support for 
such theories. This is expected to change almost entirely with the choice of a single primary SMT solver, making 
this package a SyGuS solver by itself.  
"""
