# PDA-based-palindrome-checker
A computational model simulator implemented in Python that utilizes a Pushdown Automaton (PDA) to evaluate whether a given input string is a palindrome. This project demonstrates the concept of context-free language recognition and the practical utility of stack memory in automata theory.


🚀 Features
Algorithmic String Evaluation: Cleans inputs (converts to lowercase and removes spaces) and processes them using theoretical state machine logic.


Dynamic Stack Operations: Simulates strict push and pop operations to match string halves dynamically.

Odd & Even Length Support: Automatically detects string length and correctly skips the middle symbol for odd-length strings before entering the pop-and-compare phase.


Execution Tracing: Prints a detailed, step-by-step execution trace of the PDA's internal state changes and stack manipulations.


🧠 Theoretical Background & PDA Design
The language of palindromes is context-free and can be recognized by a PDA, but not by a simple finite automaton. The application evaluates inputs using the following state progression:


q0 (Push Phase): Pushes the first half of the input onto the stack.


q1 (Skip Phase): Skips the middle character for odd-length strings.


q2 (Pop-and-Compare Phase): Pops the stack and compares symbols with the remaining input.


qf (Final State): Accepts the string if the stack empties and all characters match; otherwise, it rejects.


🛠️ Technical Stack
Language: Python 

Data Structures: Python Lists utilized as an internal stack for memory operations.
