class PDA_Palindrome:
    def __init__(self):
        self.stack = []

    def is_palindrome(self, s):
        self.stack = []
        s = s.lower().replace(" ", "")   # clean input
        n = len(s)

        print("\n--- PDA Execution Trace ---")
        print("Input:", s)
        print("Phase 1: Pushing first half onto stack...")

        # Push first half
        for i in range(n // 2):
            print(f"Push: {s[i]}")
            self.stack.append(s[i])

        # Determine starting point for pop phase
        start = n // 2
        if n % 2 == 1:
            print("Odd length → skip middle symbol:", s[start])
            start += 1

        print("\nPhase 2: Popping and matching second half...")

        # Pop and match second half
        for i in range(start, n):
            if not self.stack:
                print("Stack empty early → Reject")
                return "Rejected"
            
            top = self.stack.pop()
            print(f"Pop: {top}, Compare with: {s[i]}")

            if top != s[i]:
                print("Mismatch found → Reject")
                return "Rejected"

        # Final acceptance condition
        print("\nPhase 3: Final Check")
        if len(self.stack) == 0:
            print("Stack empty → Accept")
            return "Accepted"
        else:
            print("Stack not empty → Reject")
            return "Rejected"


# ------------------------------
# DRIVER CODE
# ------------------------------

print("PDA for Palindrome Checking")
print("-----------------------------")
print("States: q0 (push), q1 (skip middle), q2 (pop), qf (accept)")
print("Stack Alphabet: input symbols")
print("Input Alphabet: any characters\n")

pda = PDA_Palindrome()

while True:
    s = input("\nEnter a string: ")
    result = pda.is_palindrome(s)
    print("\nResult:", result)

    again = input("\nCheck another string? (y/n): ")
    if again.lower() != 'y':
        print("Exiting PDA Program...")
        break
