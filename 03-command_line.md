# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

- _pwd -- lists the present directory in which you are working_
- _cd -- allows you to change your directory_
	- _use ".." to go up a directory; "../../.." to go up several_
- _man [command] -- displays the help and syntax for a command_
- _grep [word] [filename] -- searches for a word within a file. Can be paired with wildcards for broader searches_
- _mkdir -- allows you to make a directory (use -p before mkdir to create a multi-step path)_
- _ls -- lists objects in your present working directory_
- _rmdir -- removes a directory_
- _pushd -- saves your present working directory and lets you switch to another directory_
- _popd -- goes to your last "pushed" directory_
- _touch -- creates an empty file_
- _cp -- copies a file. Syntax is "file to copy" "new file name" "[optional directory]"_
- _mv -- moves/renames a file_
- _less [filename] -- displays file text in the terminal window. Press "h" while in this window to see available commands_
- _more [filename] -- displays the text of the file int he terminal window under the command_
- _rm -- removes (deletes) a file_
- _[cmd1] | [cmd2] -- takes the output of cmd1 and directs it to cmd1_
- _[cmd1] < [cmd2] -- takes the output of cmd2 and writes it to cmd1_
- _[cmd1] > [cmd2] -- takes the output of cmd1 and writes it to cmd2_
- _[cmd] >> [cmd2] -- takes the output of cmd1 and appends it to cmd2_
- _find [directory] -name [wildcard] -print -- finds all files that match the wildcard search string and prints them out_
- _env -- lists all elements of your environment_
- _export -- sets a variable in your environment_
- _unset -- removes a variable in your environment_

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`	     -- _lists all files/folders in a directory_  
`ls -a`	  -- _displays all files/folders in a directory, including "." and ".." files_  
`ls -l`	  -- _displays the "long format" listing, which includes file size, modification timestamp, owner, and name_  
`ls -lh`  -- _same as "l" above, but shows sizes in "human readable" format (i.e "24B" rather than just "24")_   
`ls -lah` -- _displays all files/folders like -a, in long format and human-readable_  
`ls -t`	  -- _displays files in chronological order, with the newest timestamp first_  
`ls -Glp` -- _displays files/folders in a directory, color-coded by type, directories have a "/" after them_  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -d`   -- _displays only directories_  
`ls -C`	  -- _displays files/folders in a column format_  
`ls -1`	  -- _displays files/folders each on their own line_  
`ls -R`	  -- _displays files/folders, including subdirectories_  
`ls -m`	  -- _displays files/folders as a comma-delineated list_  	

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

_xargs allows one to execute commands based on arguments from standard input. What does that mean, exactly? xargs allows you to take the output from one command, and execute another command on that output (kind of like a "for each" loop). Say, for instance, you wanted to find all .txt files in a directory, then within those files search for the word "platypus." The first step is finding all text files, as such:_  
`find . -name "*.txt"`  
_This will find all text files. Then, using the `|` command, you can send the output of the_ `find` _to xargs, which will read the found text files as a list and then execute the_ `grep` _command on each element in that list, looking for the word "platypus"--which could look like this:_  
`find . -name "*.txt" | xargs grep "platypus"`


 

