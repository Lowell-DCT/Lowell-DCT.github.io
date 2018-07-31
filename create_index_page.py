#!/usr/bin/env python

# re-written version of hroe's create_index_page.py to construct a
# simple reverse sorted index page to DCT schedules.  Had to re-write
# to handle shift to semesters from quarters.  sel@ell 20180730

# ls schedules/schedule*html |
#  awk '{print "<h1><a href=\""$1"\">"$1"</a></h1>"}' |
#  sed -e 's/.html//2' | sed -e 's/schedules\/schedule-//2' > index.html

# <h1><a href="schedules/schedule-2016Q1.html">2016Q1</a></h1>
# <h1><a href="schedules/schedule-2016Q2.html">2016Q2</a></h1>
# <h1><a href="schedules/schedule-2016Q3.html">2016Q3</a></h1>
# <h1><a href="schedules/schedule-2016Q4.html">2016Q4</a></h1>

import datetime as dt
import glob
import re
from operator import itemgetter

def gen_sched_list ():
    """ Generate simple HTML list of schedules """
    # list schedule files, sort by name
    schedule_files = sorted(glob.glob("schedules/schedule*html"))

    # reverse sort by year and month that starts the scheduling period
    # (which is my kludge for handle quarters, trimesters and
    # semesters in one shot).

    b = []
    for k in schedule_files:
        a = {}
        j = k.replace('schedules/schedule-','').replace('.html', '')
        y = int(j[0:4])
        m = j[4]
        # set idx to month starting scheduling period
        # A, B == semesters, Q[1234] == quarters, a,b,c == trimesters
        if (m == 'A'):
            n = 1
        elif (m == 'B'):
            n = 7
        elif (m == 'a'):
            n = 1
        elif (m == 'b'):
            n = 5
        elif (m == 'c'):
            n = 9
        elif (m == 'Q'):
            n = (int(j[5])-1) * 3 + 1

        a['file']  = k
        a['short'] = j
        a['yr']    = y
        a['mon']   = n
        a['idx']   = y * 100 + n
        b.append(a)

    # c has sorted list of dictionaries
    c = sorted(b, key=itemgetter('idx'), reverse=True)

    #for i in c:
    #    print (i['file'])

    # write out one line pointers to current
    with open('current.html', 'w') as f:
        f.write('<meta http-equiv="refresh" content="0; URL=\'{}\'" />'.\
                format(c[0]['file']))

    with open('current-ToO.html', 'w') as f:
        f.write('<meta http-equiv="refresh" content="0; URL=\'{}.html#Approved_ToO_Programs\'" />'.\
                    format(c[0]['file']))

    # construct and write out index file
    html = '<h1>'
    oyr = c[0]['yr']
    html += '<a href="{0}">Current: {1}</a> '.format(c[0]['file'], c[0]['short'])
    html += '</h1>\n<h1>'

    for i in c:
        if (i['yr'] != oyr):
            html += '</h1>\n<h1>'
        oyr = i['yr']
        html += '<a href="{0}">{1}</a> '.format(i['file'], i['short'])
    html += '</h1>\n'

    with open('index.html', 'w') as f:
        f.write(html)

    return

#----

if __name__ == '__main__':
    gen_sched_list()
