## Bash Command
### General 

    #!/bin/sh
    #!/usr/bin/php <-- php script
    #!/bin/bash
    # command option arguments  structure
    
    
It's called a shebang, and tells the parent shell which interpreter should be used to execute the script. **Bash** is the most common shell used as a default shell for users of Linux systems. **/bin/sh** is an executable representing the system shell. Actually, it is usually implemented as a symbolic link pointing to the executable for whichever shell is the system shell. A script may specify **#!/bin/bash** on the first line, meaning that the script should always be run with bash, rather than another shell. In Ubuntu /bin/sh used to link to bash, typical behavior on Linux distributions, but now has changed to linking to another shell called **dash**. 
    
    echo #this is to print content to the terminal
    echo ------------------------------
    echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    ## Warning ##
    # "" and '' are different in shell, prefer "" if not
    ############
    
    more ## to view the content via the terminal
    more ~/.bashrc ## the startup file 
    
    # chmod using numeric permission, for 777 is read, write, execute for user, group, others  
    
    clear #to move current commands to the top, don't change setting, 
    
    cd ## change directory
    cd .. ## return to upper level
    cd ## return to home
    cd / ## the root
    cd ~ ## the home 

The commands to view/inspect (the information of) file:

    #!/bin/sh
    ls -l                          # the lone option to view detailed information
    wc README.md                   # the word count shows line, words and chars, use first to show size 
    cat README.md                  # can concatenate files, also print content to the terminal, for small size file
    less README.md                 # take over the terminal screen, ` ` to next, `b` previous, `q` to quit, exit
    head -n 10 README.md           # the default is 10 lines to show
    tail -n 10 README.md           # the same as head
    
The commands to edit file. The 1st type of method is called output redirection:

    #!/bin/sh
    touch README.md                                     # to create empty file
    echo "# Project Summary" > README.md                # this is to create a new file with the content, first line # Project Summary.
    echo "## Introduction"  >> README.md                # append the 2nd line to the README.md, append 
    # be careful with > and >> there is no undo, > will rewrite the file

The 2nd methods to edit file is the editor `nano`, `vim` and `emacs`

    nano README.md                            # writeout means save in the nano
    # create new file with nano
    
    
    
    
    
    
