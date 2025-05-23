/*
 * Copyright 2022 Alexandros Frantzis for Collabora Ltd
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#ifndef __WINE_WAYLANDDRV_UNIXLIB_H
#define __WINE_WAYLANDDRV_UNIXLIB_H

#include <stdarg.h>
#include "winternl.h"
#include "wine/unixlib.h"

enum waylanddrv_unix_func
{
    waylanddrv_unix_func_init,
    waylanddrv_unix_func_read_events,
    waylanddrv_unix_func_init_clipboard,
    waylanddrv_unix_func_count,
};

#endif /* __WINE_WAYLANDDRV_UNIXLIB_H */
