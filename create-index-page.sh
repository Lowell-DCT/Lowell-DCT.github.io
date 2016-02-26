#!/bin/bash

ls schedules/schedule*html | awk '{print "<h1><a href=\""$1"\">"$1"</a></h1><br>\n"}' | sed -e 's/.html//2' | sed -e 's/schedules\/schedule-//2' > index.html
