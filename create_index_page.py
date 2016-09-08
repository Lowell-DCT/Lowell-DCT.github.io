#!/usr/bin/env python

# ls schedules/schedule*html | awk '{print "<h1><a href=\""$1"\">"$1"</a></h1>"}' | sed -e 's/.html//2' | sed -e 's/schedules\/schedule-//2' > index.html

# <h1><a href="schedules/schedule-2016Q1.html">2016Q1</a></h1>
# <h1><a href="schedules/schedule-2016Q2.html">2016Q2</a></h1>
# <h1><a href="schedules/schedule-2016Q3.html">2016Q3</a></h1>
# <h1><a href="schedules/schedule-2016Q4.html">2016Q4</a></h1>

import datetime as dt
import glob
import re

schedule_files = sorted(glob.glob("schedules/schedule*html"))
unique_years = sorted({re.findall('(\d\d\d\d)', a)[0]:None for a in schedule_files}.keys())[-1::-1]

cur_year = dt.datetime.utcnow().year
cur_quarter = int((dt.datetime.utcnow().month - 1)/3) + 1

with open('current.html', 'w') as f:
    f.write('<meta http-equiv="refresh" content="0; URL=\'schedules/schedule-{0}Q{1}.html\'" />'.format(cur_year, cur_quarter))

with open('current-ToO.html', 'w') as f:
    f.write('<meta http-equiv="refresh" content="0; URL=\'schedules/schedule-{0}Q{1}.html#Approved_ToO_Programs\'" />'.format(cur_year, cur_quarter))

html = '<h1><a href="schedules/schedule-{0}Q{1}.html">Current: {0}Q{1}</a></h1>\n'.format(cur_year, cur_quarter)
for cur_year in unique_years:
    html += '<h1>'
    for curfile in schedule_files:
        if cur_year in curfile:
            html += '<a href="{0}">{1}</a>  '.format(curfile, re.findall('(\d\d\d\dQ\d)', curfile)[0])
    html += '</h1>\n'

with open('index.html', 'w') as f:
    f.write(html)

