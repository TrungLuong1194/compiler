# Automata

## Finite Automata

https://www.javatpoint.com/finite-automata

##### Finite Automata
- Finite automata are used to recognize patterns.
- It takes the string of symbol as input and changes its state accordingly. When the desired symbol is found, then the transition occurs.
- At the time of transition, the automata can either move to the next state or stay in the same state.
- Finite automata have two states, Accept state or Reject state. When the input string is processed successfully, and the automata reached its final state, then it will accept.

##### Formal Definition of FA
- A finite automaton is a collection of 5-tuple (Q, ∑, δ, q0, F), where:

    Q: finite set of states  
    ∑: finite set of the input symbol  
    q0: initial state   
    F: final state  
    δ: Transition function  

##### Types of Automata
- There are two types of finite automata:
1. DFA(deterministic finite automata)
2. NFA(non-deterministic finite automata)

## DFA (Deterministic finite automata)

https://www.javatpoint.com/deterministic-finite-automata

##### DFA
- DFA refers to deterministic finite automata. Deterministic refers to the uniqueness of the computation. The finite automata are called deterministic finite automata if the machine is read an input string one symbol at a time.
- In DFA, there is only one path for specific input from the current state to the next state.
- DFA does not accept the null move, i.e., the DFA cannot change state without any input character.
- DFA can contain multiple final states. It is used in Lexical Analysis in Compiler.

##### Formal Definition of DFA
    Q: finite set of states  
    ∑: finite set of the input symbol  
    q0: initial state   
    F: final state  
    δ: Transition function
    
Transition function can be defined as:

    δ: Q x ∑→Q  
    
## NFA (Non-Deterministic finite automata)

https://www.javatpoint.com/non-deterministic-finite-automata

###### NFA
- NFA stands for non-deterministic finite automata. It is easy to construct an NFA than DFA for a given regular language.
- The finite automata are called NFA when there exist many paths for specific input from the current state to the next state.
- Every NFA is not DFA, but each NFA can be translated into DFA.
- NFA is defined in the same way as DFA but with the following two exceptions, it contains multiple next states, and it contains ε transition.

##### Formal definition of NFA
    Q: finite set of states  
    ∑: finite set of the input symbol  
    q0: initial state   
    F: final state  
    δ: Transition function  
    
Transition function can be defined as:

    δ: Q x ∑ →2Q
    
## Eliminating ε Transitions

https://www.javatpoint.com/automata-eliminating-null-transitions

- NFA with ε can be converted to NFA without ε, and this NFA without ε can be converted to DFA. To do this, we will use a method, which can remove all the ε transition from given NFA. The method will be:

1. Find out all the ε transitions from each state from Q. That will be called as ε-closure{q1} where qi ∈ Q.
2. Then δ' transitions can be obtained. The δ' transitions mean a ε-closure on δ moves.
3. Repeat Step-2 for each input symbol and each state of given NFA.
4. Using the resultant states, the transition table for equivalent NFA without ε can be built.

## Conversion from NFA to DFA

https://www.javatpoint.com/automata-conversion-from-nfa-to-dfa

##### Steps for converting NFA to DFA
- Step 1: Initially Q' = ϕ

- Step 2: Add q0 of NFA to Q'. Then find the transitions from this start state.

- Step 3: In Q', find the possible set of states for each input symbol. If this set of states is not in Q', then add it to Q'.

- Step 4: In DFA, the final state will be all the states which contain F(final states of NFA)

## Conversion from NFA with ε to DFA

https://www.javatpoint.com/automata-conversion-from-nfa-with-null-to-dfa

- Non-deterministic finite automata(NFA) is a finite automata where for some cases when a specific input is given to the current state, the machine goes to multiple states or more than 1 states. It can contain ε move. It can be represented as M = { Q, ∑, δ, q0, F}.

Where

    Q: finite set of states  
    ∑: finite set of the input symbol  
    q0: initial state   
    F: final state  
    δ: Transition function  
    
- NFA with ∈ move: If any FA contains ε transaction or move, the finite automata is called NFA with ∈ move.
- ε-closure: ε-closure for a given state A means a set of states which can be reached from the state A with only ε(null) move including the state A itself.

##### Steps for converting NFA with ε to DFA
- Step 1: We will take the ε-closure for the starting state of NFA as a starting state of DFA.

- Step 2: Find the states for each input symbol that can be traversed from the present. That means the union of transition value and their closures for each state of NFA present in the current state of DFA.

- Step 3: If we found a new state, take it as current state and repeat step 2.

- Step 4: Repeat Step 2 and Step 3 until there is no new state present in the transition table of DFA.

- Step 5: Mark the states of DFA as a final state which contains the final state of NFA.

## Minimization of DFA

https://www.javatpoint.com/minimization-of-dfa

Minimization of DFA means reducing the number of states from given FA. Thus, we get the FSM(finite state machine) with redundant states after minimizing the FSM.

##### Steps for minimizing of DFA
- Step 1: Remove all the states that are unreachable from the initial state via any set of the transition of DFA.

- Step 2: Draw the transition table for all pair of states.

- Step 3: Now split the transition table into two tables T1 and T2. T1 contains all final states, and T2 contains non-final states.

- Step 4: Find similar rows from T1 such that:

    1. δ (q, a) = p  
    2. δ (r, a) = p  
    
That means, find the two states which have the same value of a and b and remove one of them.
    
- Step 5: Repeat step 3 until we find no similar rows available in the transition table T1.

- Step 6: Repeat step 3 and step 4 for table T2 also.

- Step 7: Now combine the reduced T1 and T2 tables. The combined transition table is the transition table of minimized DFA.



    
    