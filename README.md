# impw
Password manager using images.

### installation
```bash
git clone https://github.com/marcelm9/impw.git
cd impw
pip install .
```

### commands
```bash
# create new password
python -m impw new <name>

# list all stored passwords
python -m impw list

# copy password
python -m impw copy <name>

# show drawing for password
python -m impw show <name>

# rename stored password
python -m impw rename <old_name> <new_name>

# delete stored password
python -m impw delete <name>
```

### how passwords are created
- draw image
- for each pixel (scaled by 2):
    - if pixel is black, add 0
    - if pixel is white, add 1
- this results in a 40000 character string of 0s and 1s
- hash this string using sha256
- replace first four characters with "IMPW"
- replace last character with asterisk
