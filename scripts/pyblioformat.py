# -*- python -*-
# -*- coding: utf-8 -*-
# This file is part of pybliographer
# 
# Copyright (C) 2018 Germán Poo-Caamaño <gpoo@gnome.org>
# Copyright (C) 1998-2004 Frederic GOBRY <gobry@pybliographer.org>
# 	   
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2 
# of the License, or (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details. 
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# 
# 

import string
import sys
import os
import getopt

from gettext import gettext as _

from Pyblio import Autoload, Fields
from Pyblio.Style import Utils
from Pyblio.Open import bibopen

import locale
charset = locale.getlocale () [1] or 'ascii'


def usage ():
    print _(u"""usage: pyblioformat [options] <database…>

    options:
      -o file, --output=file		specify an output filename
      -s style, --style=style		specify a bibliography style
      -f format, --format=format	specify an output format
      -H header, --header=header	defines a header file
      -F footer, --footer=footer	defines a footer file
      -l 'output', --list='output'	lists the available output formats
      -h, --help			show this help message
    """).encode (charset)
    return

def error (text, exit = 1):
    sys.stderr.write ((_("pyblioformat: error: %s\n") % text).encode (charset))
    if exit:
        sys.exit (1)
    return

def warning (text, exit = 0):
    sys.stderr.write ((_("pyblioformat: warning: %s\n") % text).encode (charset))
    if exit:
        sys.exit (1)
    return

try:
    optlist, args = getopt.getopt (sys.argv [2:],
			       'H:F:o:l:hs:f:',
			       ['header=',
				'footer=',
                                'output=',
                                'list=',
                                'style=',
                                'format=',
				'help'])
except getopt.GetoptError, err:
    usage ()
    error (str(err).decode (charset))


header  = None
footer  = None
outfile = sys.stdout
format  = 'text'
style   = 'Alpha'

for opt, value in optlist:
    if opt == '-H' or opt == '--header':
        header = value
        continue
    
    if opt == '-F' or opt == '--footer':
        footer = value
        continue

    if opt == '-o' or opt == '--output':
        try:
            outfile = open (value, 'w')
        except IOError, err:
            error (_(u"can’t open “%s”: %s") % (value, str (err).decode (charset)))
        continue

    if opt == '-l' or opt == '--list':
        try:
            list = Autoload.available (value)
        except KeyError:
            error (_(u"unknown list “%s”") % value)
            
        if list:
            print (_(u"pyblioformat: available values for “%s”:") % value).encode (charset)
            print "  " + string.join (list, ", ")
            sys.exit (0)
        else:
            warning (_(u"empty value list “%s”") % value)
            sys.exit (0)
            
    if opt == '-h' or opt == '--help':
        usage ()
        sys.exit (0)
        continue

    if opt == '-s' or opt == '--style':
        style = value
        continue

    
    if opt == '-f' or opt == '--format':
        format = value
        continue
    

# test input arguments
if len (args) < 1:
    # user gave wrong arguments...
    usage ()
    error (_("too few arguments"))

files  = args

# get the specified style and the output
output = Autoload.get_by_name ('output', format)
if output is None:
    error (_(u"unknown output format “%s”") % format)

url = None
style = os.path.splitext (style) [0]
if os.path.exists (style + '.xml'):
    url = Fields.URL (style + '.xml')
else:
    from Pyblio import version
    full = os.path.join (version.pybdir, 'Styles', style)
    full = full + '.xml'
    if os.path.exists (full): url = Fields.URL (full)

if not url:
    error (_(u"can’t find style “%s”") % style)


sys.stderr.write ((_(u"pyblioformat: using style “%s”, format “%s”\n") % (style, output.name)).encode (charset))

formatter = output.data

# first, write the header
if header:
    try:
        h = open (header, 'r')
        line = '\n'
        while line:
            line = h.readline ()
            if line:
                outfile.write (line)
        h.close ()
    except IOError, err:
        error (_(u"can’t open header “%s”: %s") % (header, str (err).decode (charset)))

# write the data
for file in files:

    try:
        db = bibopen (file)
    except IOError, err:
        error (_(u"can’t open database: %s") % file)

    Utils.generate (url, formatter, db, db.keys (), outfile)
    
# last, write the footer
if footer:
    try:
        h = open (footer, 'r')
        line = '\n'
        while line:
            line = h.readline ()
            if line:
                outfile.write (line)
        h.close ()
    except IOError, err:
        error (_(u"can’t open footer “%s”: %s") % (footer, str (err).decode (charset)))

        
outfile.close ()
