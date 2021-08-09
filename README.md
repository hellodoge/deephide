## deephide
Deephide is a steganography tool to hide data in media files such as photos.

### Usage

```
deephide hide -b <files in which we want to hide> -i <what files we want to hide> -p <password> -c <compression level>
```

```
deephide reveal -b <where data is hidden> -o <where to store revealed files> -p <password to decrypt data>
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

### How it works
Deephide will add files we want to hide to a zip archive, then encrypt it and compress. \
The resulting byte sequence will be split into several parts with different length (however, close to the same as much as possible) \
These parts, their length and checksums will be added to the end of media files.

Revealing will know the order of parts according to their length \
Checksums used to verify that the media file contains part of encrypted data, so the algorithm will work as expected even if we add more media files before revealing data

### TODO
- [ ] Implement a backup option that will write each part to several files, so the program will work even if some of the container files were deleted
