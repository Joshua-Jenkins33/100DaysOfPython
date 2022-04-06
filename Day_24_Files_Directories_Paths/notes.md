# Snake High Score

Everything makes good sense! Reset the snake, reset the scoreboard, modify the scoreboard to handle the new high score, create, manage, and update the new high score, etc.

Problem is -- how do you keep the high score between sessions?

```py
a = 3
a = input("What do you want 'a' to equal?: ")
print(a)
```

Store it in a document using python to read and write to a file!

## How to Open, Read, and Write to Files using "with" KeyWord

### Files

**Read.** It's as easy as `file = open("fileName")` and `contents = file.read()`!

Then make sure to `file.close()` when you're done so it doesn't continue to consume resources.

The `with open('file_path') as file:` block lets us ignore the `file.close()` method call. As soon as we're done with this block it will close down the file.

**Write.** There's an additional parameter to consider when trying to write to a file in the `open()` method call. That parameter is `mode = ` and it defaults to `r`, or **read**. Change it to `w` for **write**.

`w` will write over the entire file. **Adding** to file just requires the `mode` to be `a`!

If you open a file with `write` mode and that file doesn't actually exist, it will create that file for you from scratch.

## Understand Relative and Absolute File Paths

Files can live within folders, some files can be several folders deep or nested in.

**Working Directory.** The current directory we're working in!

**Relative File Path.** Look in the current folder for this file! 
- `./talk.ppt` — gets a file inside your current working directory
- `./Projects/talk.ppt` — gets a file inside a folder in your current working directory
- `../report.doc` — to go up one layer and read a file 

File Path Peculiarity for different Operating Systems. Python doesn't care; woot!

### Get something from the desktop when working in your project

```py
with open("/Users/angela/Desktop/my_file.txt") as file:
  contents = file.read()
  print(contents)
```

### Relative to our main.py

PyCharm knows what your directory looks like.

```py
with open("../../Desktop/my_file.txt") as file:
  contents = file.read()
  print(contents)
```

**Absolute File Path.** Relative to your ROOT or C drive.

**Relative File Path.** Relative to your current workind directory.