#!/bin/bash

ls schedule*html | awk '{print "<a href=\""$1"\">"$1"</a>"}' | sed -e 's/.html//2' | sed -e 's/schedule-//2' > index.html
