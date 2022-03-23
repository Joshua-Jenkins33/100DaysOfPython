# Snake High Score

Everything makes good sense! Reset the snake, reset the scoreboard, modify the scoreboard to handle the new high score, create, manage, and update the new high score, etc.

Problem is -- how do you keep the high score between sessions?

```py
a = 3
a = input("What do you want 'a' to equal?: ")
print(a)
```

Store it in a document using python to read and write to a file!

# How to Open, Read, and Write to Files using "with" KeyWord

## Files

**Read.** It's as easy as `file = open("fileName")` and `contents = file.read()`!

Then make sure to `file.close()` when you're done so it doesn't continue to consume resources.

The `with open('file_path') as file:` block lets us ignore the `file.close()` method call. As soon as we're done with this block it will close down the file.

**Write.** There's an additional parameter to consider when trying to write to a file in the `open()` method call. That parameter is `mode = ` and it defaults to `r`, or **read**. Change it to `w` for **write**.

`w` will write over the entire file. **Adding** to file just requires the `mode` to be `a`!

If you open a file with `write` mode and that file doesn't actually exist, it will create that file for you from scratch.