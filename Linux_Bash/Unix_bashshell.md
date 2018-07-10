## Bash Command
### General 

    #!/bin/sh
    #!/usr/bin/php <-- php script
    #!/bin/bash
It's called a shebang, and tells the parent shell which interpreter should be used to execute the script. **Bash** is the most common shell used as a default shell for users of Linux systems. **/bin/sh** is an executable representing the system shell. Actually, it is usually implemented as a symbolic link pointing to the executable for whichever shell is the system shell. A script may specify **#!/bin/bash** on the first line, meaning that the script should always be run with bash, rather than another shell. In Ubuntu /bin/sh used to link to bash, typical behavior on Linux distributions, but now has changed to linking to another shell called **dash**. 
    
    echo #this is to print content to the terminal
    echo ------------------------------
    echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    more ## to view the content via the terminal
    more ~/.bashrc ## the startup file 
    
    # chmod using numeric permission, for 777 is read, write, execute for user, group, others  
    
    clear #to move current commands to the top, don't change setting, 
    
    cd ## change directory
    cd .. ## return to upper level
    cd ## return to home
    cd / ## the root
    cd ~ ## the home 
    
    
    
    
    
    