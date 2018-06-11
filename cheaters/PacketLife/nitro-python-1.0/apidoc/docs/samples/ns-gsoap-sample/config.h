// $Id: //depot/main/rs_105_56_8/usr.src/netscaler/config/api/gsoap/config.h#1 $
/*
 * Note: wherever we compile with -DHAVE_CONFIG_H (currenltly everywhere)
 * we must copy necessary definitions for that platform from stdsoap2.h
 * into this file.
 */
#ifdef FreeBSD

// 2003apr23/reilbert
#define HAVE_SYS_TIMEB_H
#undef HAVE_FTIME

#endif // FreeBSD

#ifdef WIN32

/* 2003jul03/reilbert
 * This file is included before winsock.h in stdsoap2.h, so if LONG64
 * *is* defined in a windoze header file the definitions below will
 * cause problems.  (The windoze build machine appears to be using
 * a different version of vc than I am, not sure how long that has
 * been the case ....)
 */
#include <winsock.h>

// 2003jun30/reilbert
#ifndef LONG64
#define LONG64 long
#define ULONG64 unsigned long
#endif

// (Copied from stdsoap.h)
#define HAVE_SYS_TIMEB_H
#define HAVE_FTIME

#endif // WIN32
