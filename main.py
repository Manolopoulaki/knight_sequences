# Define the keypad layout
keypad = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    [None, '1', '2', '3', None]
]

# Define the vowels
vowels = {'A', 'E', 'I', 'O'}

# Create a list of the possible knight moves
knight_moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Initialise a dictionary to save already discovered valid moves
memo = {}

# helper functions
def is_valid(r, c):
    """Checks if a position is valid on the keypad."""
    return 0 <= r < 4 and 0 <= c < 5 and keypad[r][c] is not None

def count_sequences(r, c, length, vowel_count):
    """Searches to find all valid sequences."""

    # If sequence length is already 10, then search can end
    if length == 10:
        return 1
    
    # Check if move is already discoverd by looking at memo
    if (r, c, length, vowel_count) in memo:
        return memo[(r, c, length, vowel_count)]
    
    # Check if new move is valid and count it if it is
    total_sequences = 0
    
    for dr, dc in knight_moves:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc):
            new_vowel_count = vowel_count + (1 if keypad[nr][nc] in vowels else 0)
            if new_vowel_count <= 2:
                total_sequences += count_sequences(nr, nc, length + 1, new_vowel_count)
    
    # Store this valid move in memo
    memo[(r, c, length, vowel_count)] = total_sequences
    return total_sequences

def total_valid_sequences():
    """Loops over all initial positions and calculates the possible total sequences for each one"""
    total_valid_sequences = 0
    for r in range(4):
        for c in range(5):
            if keypad[r][c] is not None:
                total_valid_sequences += count_sequences(r, c, 1, 1 if keypad[r][c] in vowels else 0)
    return total_valid_sequences

# Print the result
print(total_valid_sequences())
