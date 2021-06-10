## deephide
Deephide is a steganography tool to hide data in media files such as photos.

### Usage
```
usage: deephide [-h] -b BOX [BOX ...] [-i INPUT [INPUT ...]] [-o OUTPUT] [-c {-1,0,1,2,3,4,5,6,7,8,9}] [-p PASSWORD] [-v | -q] {hide,reveal}
deephide: error: the following arguments are required: action, -b/--box
```

### Example
```
$ ls
 photos  'photos 2'   secret
$ ls photos secret -l
total 16160
8609883 eggs.jpg
7933533 ham.jpg
1494306 secret
$ sha1sum secret 
77cad24b2554c0b366847c14d5f3a3fe074c3961  secret
$ deephide hide -b photos -i secret -p strongpassword
$ ls -l photos
total 18108
9606218 eggs.jpg
8929866 ham.jpg
$ deephide reveal -b photos -o secret_reveal -p strongpassword
$ sha1sum secret_reveal/secret 
77cad24b2554c0b366847c14d5f3a3fe074c3961  secret_reveal/secret
```
