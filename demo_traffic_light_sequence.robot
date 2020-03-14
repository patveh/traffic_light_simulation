*Settings

Documentation   Execute traffic light actions and transitions between its operational modes.

######  This is Your application  ######

Library         TrafficLight.py

*Tasks

Demo blinking lights
#   | transitions
#                   | list of arguments passed on to functions
    init_mode
    set_light       yellow  1000    ${TRUE}
    activate_mode   2
    init_mode
    set_light       red     1000    ${TRUE}
    activate_mode   2
    init_mode
    set_light       green   1000    ${TRUE}
    activate_mode   2
    set_default_mode

Demo traffic control
#   | transitions
#               | list of arguments passed on to functions
    init_mode
    set_light       yellow  1000    ${FALSE}
    set_light       red     3000    ${FALSE}
    set_light       yellow  1000    ${FALSE}
    set_light       green   3000    ${FALSE}
    activate_mode   2
    set_default_mode
