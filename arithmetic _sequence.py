"""
Generates an arithmetic sequence starting at 5 with common difference 3
"""

def generate_sequence(start=5, difference=3, terms=8):
    """
    Generates arithmetic sequence
    Args:
        start: First term in sequence
        difference: Common difference between terms
        terms: Number of terms to generate
    Returns:
        List containing the arithmetic sequence
    """
    sequence = [start + i * difference for i in range(terms)]
    return sequence

def print_sequence(sequence):
    """Prints the sequence with term numbers"""
    print("Arithmetic Sequence:")
    for i, term in enumerate(sequence, 1):
        print(f"Term {i}: {term}")

if __name__ == "__main__":
    seq = generate_sequence()
    print_sequence(seq)
