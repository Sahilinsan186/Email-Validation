import sys
Email = input("Enter E-mail: ")

if '@' not in Email:
    print("'@' is not present.")
    sys.exit()
else :
    if Email.count('@') == 1:
        Username,Domain_Name =  Email.split('@')
    else:
        print("Email must contain only 1 '@' symbol.")
        sys.exit()

if Domain_Name.count('.') == 1 or Domain_Name.count('.') == 2:
    pass
else:
    print(f"{Domain_Name} (after '@' symbol) should contain atleast one '.' and atmost 2 '.' (no dots consecutively).")
    sys.exit()

if len(Email)<6:
    print("It's not valid\nEmail should be atleast 6 characters long\nFor ex: a@a.in (the smallest email address.)")
elif not Email.islower():
    print("Please write in lowercase only.")
elif not Email[0].isalpha():
    print("First letter should be alphabet only.")
elif not Username[-1].isalpha():
        print("Last letter should be alphabet only.")

elif not Username.replace('_','').replace('.','').isalnum():
    print(f"{Username}(before '@' symbol) should be alpha-numeric only.")
    sys.exit()
elif not all(parts.isalnum() for parts in Domain_Name.split('.')):
    print(f"{Domain_Name}(after '@' symbol) should contain only alpha-numerical and dot(s).")
elif not all(len(x)>=2 for x in Domain_Name.split('.')):
    for x in Domain_Name.split('.'):
        if len(x)<2:
           print(f'{x} is only {len(x)} characters long.\nMinimum 2 is required.')
else:
    print(f'"{Email}" is valid.')