# Code Word Splitter Assignment
# Author: GHUFRAN AHMED
# Seat No: EB21103039

import re


def tokenize(code, patterns):
    """
    Function to tokenize the code into different types of tokens.
    """
    tokens = []
    for pattern, token_type in patterns:
        matches = re.finditer(pattern, code)
        for match in matches:
            tokens.append((match.group(), token_type))
    return tokens


def remove_comments(code):
    """
    Function to remove comments from the code.
    """
    # Remove single-line comments
    code = re.sub('//.*', '', code)
    # Remove multi-line comments
    code = re.sub('/\*.*?\*/', '', code, flags=re.DOTALL)
    return code


def extract_tokens():
    """
    Function to get user input and extract tokens from the code.
    """
    code = ""
    while True:
        line = input("Enter code line (leave empty to finish): ")
        if not line:
            break
        code += line + "\n"
    code = remove_comments(code)

    # Predefined token patterns for a specific language
    patterns = [
        (r'\b(?:if|else|while|for)\b', 'KEYWORD'),  # Keywords
        (r'\b[a-zA-Z_]\w*\b', 'IDENTIFIER'),  # Identifiers
        (r'\b\d+\b', 'LITERAL'),  # Numeric literals
        (r'[+\-*/=<>]', 'OPERATOR'),  # Operators
        (r'[;(),.]', 'SEPARATOR')  # Separators
    ]

    tokens = tokenize(code, patterns)
    return tokens


# Entry point of the program
def main():
    """
    Main function to orchestrate the program flow.
    """
    extracted_tokens = extract_tokens()
    # Store the tokens in a list or any desired data structure
    token_list = extracted_tokens

    display_tokens = input("Do you want to display the extracted tokens? (y/n): ")

    if display_tokens.lower() == 'y':
        # Print the extracted tokens
        print("Extracted Tokens:")
        for token, token_type in token_list:
            print(f"{token}: {token_type}")

    # Count identifiers, operators, separators, and keywords
    identifier_count = sum(1 for _, token_type in token_list if token_type == 'IDENTIFIER')
    operator_count = sum(1 for _, token_type in token_list if token_type == 'OPERATOR')
    separator_count = sum(1 for _, token_type in token_list if token_type == 'SEPARATOR')
    keyword_count = sum(1 for _, token_type in token_list if token_type == 'KEYWORD')

    # Print the counts
    print("\nToken Counts:")
    print(f"Identifier count: {identifier_count}")
    print(f"Operator count: {operator_count}")
    print(f"Separator count: {separator_count}")
    print(f"Keyword count: {keyword_count}")


if __name__ == "__main__":
    main()
