# Importing various modules for use in this script.
# The first import statement uses the "from module import * " syntax, which imports all public objects
# defined in the module directly into the current namespace.
# The second import statement uses the "import module as alias" syntax, which imports the module
# and gives it a shorter name (alias) to make it easier to refer to.

from . import extras, help, play, queue, settings, speed, start

# If you prefer to use the original names for the modules, you can use the second import style.
# This can be helpful if the original module names are more descriptive or if there are naming conflicts
# with other modules in your project.

import .extras as extras
import .help as help
import .play as play
import .queue as queue
import .settings as settings
import .speed as speed
import .start as start
