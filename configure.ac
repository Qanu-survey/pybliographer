dnl -*- m4 -*-
dnl This file is part of pybliographer
dnl
dnl Copyright (C) 1998-2003 Frederic GOBRY
dnl Email : gobry@idiap.ch
dnl          
dnl This program is free software; you can redistribute it and/or
dnl modify it under the terms of the GNU General Public License
dnl as published by the Free Software Foundation; either version 2 
dnl of the License, or (at your option) any later version.
dnl   
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details. 
dnl
dnl You should have received a copy of the GNU General Public License
dnl along with this program; if not, write to the Free Software
dnl Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
dnl
dnl $Id$
dnl
dnl Process this file with autoconf to produce a configure script.

AC_PREREQ(2.57)

AC_INIT(pybliographer, 1.1.90)
AM_INIT_AUTOMAKE

AC_CONFIG_SRCDIR(pybliographer.py)
AC_CONFIG_HEADERS(config.h)

AM_ACLOCAL_INCLUDE(macros)

AC_PROG_CC
AC_ISC_POSIX


dnl Checking for python

AM_CHECK_PYTHON(2.2)

AC_MSG_CHECKING([python devel])

Py_Makefile="${Python_Prefix}/lib/python${Python_Major_Version}.${Python_Minor_Version}/config/Makefile"

if test -f ${Py_Makefile} ; then
  AC_MSG_RESULT([found])
else
  AC_MSG_RESULT([${Py_Makefile} missing])

[
cat<<EOF

To compile pybliographer, you need the development package for python.
This is usually an additional package, called python-devel (for
RPM-based distributions), or python-dev (for Debian users).

Once this package is installed, run the configure script again.

EOF
]

  AC_MSG_ERROR([aborting])
fi

dnl Checks for libraries.
AM_PATH_GLIB(1.2.0, , AC_MSG_ERROR([require glib]))

AC_PROG_LIBTOOL

dnl Checks for programs.
AM_PROG_LEX
AC_PROG_YACC

dnl NLS
ALL_LINGUAS="az da de fi fr hu it ja no pt_BR ru sk sv tr uk"

dnl Manually unset LINGUAS so that all the packages get installed
unset LINGUAS

AM_GNU_GETTEXT

AC_ARG_WITH(recode_prefix,
[  --with-recode-prefix=dir   Prefix where GNU Recode is installed],,
            with_recode_prefix=no)

AC_ARG_WITH(recode_exec_prefix,
[  --with-recode-exec-prefix=dir   Exec prefix where GNU Recode is installed],,
            with_recode_exec_prefix=no)

dnl Check in the standard paths
if test "x${with_recode_prefix}" = "xno" ; then
  AC_MSG_CHECKING([for GNU Recode])
  RECODELIB="-lrecode"
  RECODEINC=''
  RECODEPATH="${PATH}"
else
  dnl Check in the specified path
  if test "x${with_recode_exec_prefix}" = "xno" ; then
    AC_MSG_CHECKING([for GNU Recode in ${with_recode_prefix}])
    RECODELIB="-L${with_recode_prefix}/lib -lrecode"
  else
    AC_MSG_CHECKING([for GNU Recode in ${with_recode_exec_prefix}])
    RECODELIB="-L${with_recode_exec_prefix}/lib -lrecode"
  fi

  RECODEINC="-I${with_recode_prefix}/include"
  RECODEPATH="${with_recode_prefix}/bin"
fi

dnl Checks for library functions.

old_CPPFLAGS=${CPPFLAGS}
old_LIBS=${LIBS}

CPPFLAGS="${CPPFLAGS} ${RECODEINC}"
LIBS=${RECODELIB}


if test "x${USE_INCLUDED_LIBINTL}" = "xyes" ; then
  AC_MSG_RESULT(not tested because of i18n dependency)
else
  
  echo "configure: checking if librecode can be found at compile time" >&5
  AC_TRY_LINK(
  [
  
  char recode_new_outer();
  char * program_name;
  
  ],
  
  [
    recode_new_outer (0); 
  ],,
  
  [
    AC_MSG_RESULT([no (cannot compile)])
    AC_MSG_ERROR([please install GNU Recode (version 3.5)]) 
  ])
  

  echo "configure: checking if librecode can be found at runtime" >&5
  AC_TRY_RUN(
  [

   char recode_new_outer();
   char * program_name;
   
   int main () {
     recode_new_outer (0); 
     return 0;
   }

  ],,
    AC_MSG_RESULT([no (cannot run)])

[
cat<<EOF

A test program has been compiled but could not be run. This usually
means that the librecode.so library is not in a standard place. If you
installed recode from the sources, for instance in /usr/local, please
add /usr/local/lib to either

    - /etc/ld.so.conf and run ldconfig (esp. for linux)

    - the LD_LIBRARY_PATH environment variable.

...and run configure again.

You can find additional information in config.log

EOF
]

    AC_MSG_ERROR([librecode could not be found at runtime]), 

  [/bin/false]
 )
  
  echo "configure: checking if librecode actually works" >&5
  AC_TRY_RUN(
  [

#include <stdio.h>
#include <stdbool.h>
#include <recode.h>
char *program_name;

int main (int argc, char *argv[]) {
  RECODE_OUTER   outer;
  RECODE_REQUEST request;
  char * res;

  program_name=argv[0];
  outer = recode_new_outer (true);
  request = recode_new_request (outer);
  recode_scan_request (request, "latin1..latex");

  res = recode_string (request, "simple test\n");
  exit (strlen (res) ? 0 : 1);
}
  
  ],,
    AC_MSG_RESULT([no (broken recode version)])
[
cat<<EOF

A test program has been compiled but did not run as expected. This can
be caused by a broken version of GNU Recode. Recode 3.6 is known to be
broken, unless your vendor provided a patch for it. In doubt, please
install recode 3.5 and run configure again.

EOF
]

    AC_MSG_ERROR([your version of recode does not work.]), 

  [/bin/false]
 )

  AC_MSG_RESULT([found])
fi

CPPFLAGS=${old_CPPFLAGS}
LIBS=${old_LIBS}

AH_TEMPLATE([USE_RECODE], [Compile the python extensions with recode])
AC_DEFINE(USE_RECODE)

AC_SUBST(RECODELIB)
AC_SUBST(RECODEINC)

dnl Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADERS(stdbool.h)

dnl Check if Gtk/GNOME is available
AC_MSG_CHECKING([for Gnome-Python])

if ${Python} -c 'import gnome' >&5 2>&1 ; then
  AC_MSG_RESULT([found])
  dnl Check if Gtk/GNOME is new enough
  AC_MSG_CHECKING([for Gnome-Python threads])

  if test "x${DISPLAY}" = "x" ; then
    AC_MSG_RESULT([skipped (no display)])
  else
    if ${Python} -c 'import gtk ; print gtk.threads_leave' >&5 2>&1 ; then
      AC_MSG_RESULT([found])
    else
      AC_MSG_RESULT([not found])
      AC_MSG_ERROR([this version is too old. Please install gnome-python, version >= 1.0.52])
    fi
  fi

else
  AC_MSG_RESULT([not found])
  AC_MSG_WARN([install gnome-python if you want the graphical interface])
fi

AC_CONFIG_FILES(	
	Makefile 
	macros/Makefile
	etc/installer
	scripts/Makefile
	tests/Makefile
	glade/Makefile
	compiled/Setup.tmp:compiled/Setup.in
	bibtex/Makefile 
	Pyblio/Makefile
	Pyblio/GnomeUI/Makefile
	Pyblio/Format/Makefile
	Pyblio/Output/Makefile
	Pyblio/ConfDir/Makefile
	Pyblio/Style/Makefile
        intl/Makefile
        po/Makefile.in
	doc/Makefile
	doc/C/Makefile
	doc/it/Makefile
	Styles/Makefile
)

AC_CONFIG_COMMANDS([bootstrap],
[

/bin/sh ./etc/installer < compiled/Setup.tmp > compiled/Setup

if echo ${srcdir} | grep '^/' > /dev/null ; then
	source=${srcdir}
else
	source="`pwd`/${srcdir}"
fi

(
echo
echo "---------- python bootstrap ----------"
echo
cd compiled && \
	make -f ${source}/compiled/Makefile.pre.in boot \
	VPATH=${source}/compiled srcdir=${source}/compiled
) >> config.log 2>&1

])

AC_OUTPUT

echo "pybliographer is now configured. Type make to build it"