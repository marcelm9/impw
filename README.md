# impw

### Password manager using images

##### Commands:
- new <name>
- show <name>
- list
- copy <name>

### How passwords are created
- draw image
- for each pixel (scaled by 2):
    - if pixel is black, add 0
    - if pixel is white, add 1
- this results in a 40000 character string of 0s and 1s
- hash this string using sha256
- replace first four characters with "IMPW"
- replace last character with asterisk
