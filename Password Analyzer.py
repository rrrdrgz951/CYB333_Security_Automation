import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Add digits.")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Add special symbols.")

    # Determine strength
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, suggestions

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    strength, suggestions = check_password_strength(password)
    print(f"Password strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for s in suggestions:
            print(f"- {s}")
