#!/bin/bash

ls schedules/schedule*html | awk '{print "<a href=\""$1"\">"$1"</a><br>\n"}' | sed -e 's/.html//2' | sed -e 's/schedules\/schedule-//2' > index.html
