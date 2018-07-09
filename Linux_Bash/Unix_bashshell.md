## Bash Command
### General 

    #!/bin/sh
    #!/usr/bin/php <-- php script
    #!/bin/bash
It's called a shebang, and tells the parent shell which interpreter should be used to execute the script. **Bash** is the most common shell used as a default shell for users of Linux systems. **/bin/sh** is an executable representing the system shell. Actually, it is usually implemented as a symbolic link pointing to the executable for whichever shell is the system shell. A script may specify **#!/bin/bash** on the first line, meaning that the script should always be run with bash, rather than another shell. In Ubuntu /bin/sh used to link to bash, typical behavior on Linux distributions, but now has changed to linking to another shell called **dash**. 