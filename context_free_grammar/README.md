# Context-free Grammar

## Context-free Grammar

https://www.javatpoint.com/automata-context-free-grammar

CFG stands for context-free grammar. It is is a formal grammar which is used to generate all possible patterns of strings in a given formal language. Context-free grammar G can be defined by four tuples as:

    G = (V, T, P, S)  
    
- G is the grammar, which consists of a set of the production rule. It is used to generate the string of a language.
- T is the final set of a terminal symbol. It is denoted by lower case letters.
- V is the final set of a non-terminal symbol. It is denoted by capital letters.
- P is a set of production rules, which is used for replacing non-terminals symbols(on the left side of the production) in a string with other terminal or non-terminal symbols(on the right side of the production).
- S is the start symbol which is used to derive the string. We can derive the string by repeatedly replacing a non-terminal by the right-hand side of the production until all non-terminal have been replaced by terminal symbols.

## Simplification of Context-free Grammar

https://www.javatpoint.com/automata-simplification-of-cfg

Simplification of grammar means reduction of grammar by removing useless symbols. The properties of reduced grammar are given below:

- Each variable (i.e. non-terminal) and each terminal of G appears in the derivation of some word in L.
- There should not be any production as X → Y where X and Y are non-terminal.
- If ε is not in the language L then there need not to be the production X → ε.

##### Removal of Useless Symbols
A symbol can be useless if it does not appear on the right-hand side of the production rule and does not take part in the derivation of any string. That symbol is known as a useless symbol. Similarly, a variable can be useless if it does not take part in the derivation of any string. That variable is known as a useless variable.

##### Elimination of ε Production
The productions of type S → ε are called ε productions. These type of productions can only be removed from those grammars that do not generate ε.

- Step 1: First find out all nullable non-terminal variable which derives ε.

- Step 2: For each production A → a, construct all production A → x, where x is obtained from a by removing one or more non-terminal from step 1.

- Step 3: Now combine the result of step 2 with the original production and remove ε productions.

##### Removing Unit Productions
The unit productions are the productions in which one non-terminal gives another non-terminal. Use the following steps to remove unit production:

- Step 1: To remove X → Y, add production X → a to the grammar rule whenever Y → a occurs in the grammar.

- Step 2: Now delete X → Y from the grammar.

- Step 3: Repeat step 1 and step 2 until all unit productions are removed.

## Chomsky's Normal Form (CNF)

https://www.javatpoint.com/automata-chomskys-normal-form

CNF stands for Chomsky normal form. A CFG (context free grammar) is in CNF (Chomsky normal form) if all production rules satisfy one of the following conditions:

- Start symbol generating ε. For example, A → ε.
- A non-terminal generating two non-terminals. For example, S → AB.
- A non-terminal generating a terminal. For example, S → a.

##### Steps for converting CFG into CNF
- Step 1: Eliminate start symbol from the RHS. If the start symbol T is at the right-hand side of any production, create a new production as:
    
        S1 → S  
    
Where S1 is the new start symbol.

- Step 2: In the grammar, remove the null, unit and useless productions. You can refer to the Simplification of CFG.

- Step 3: Eliminate terminals from the RHS of the production if they exist with other non-terminals or terminals. For example, production S → aA can be decomposed as:

        S → RA  
        R → a  
        
- Step 4: Eliminate RHS with more than two non-terminals. For example, S → ASB can be decomposed as:

        S → RS  
        R → AS  
    