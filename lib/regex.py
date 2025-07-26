import re

# Name regex - matches capitalized names with spaces, hyphens, or apostrophes
name_regex = re.compile(r'^[A-Z][A-Za-z\'-]+( [A-Z][A-Za-z\'-]+)*$')
print(name_regex.fullmatch("Anya Taylor-Joy"))  # Should match
print(name_regex.fullmatch("John O'Connor"))    # Should match
print(name_regex.fullmatch("123 John"))         # Should NOT match

# Phone regex - matches various phone number formats
phone_regex = re.compile(r'^(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
print(phone_regex.fullmatch("(555) 555-5555"))  # Should match
print(phone_regex.fullmatch("555-555-5555"))    # Should match
print(phone_regex.fullmatch("+1 555 555 5555")) # Should match

# Email regex - standard email validation
email_regex = re.compile(r'^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
print(email_regex.fullmatch("user@gmail.com"))    # Should match
print(email_regex.fullmatch("invalid@email"))    # Should NOT match