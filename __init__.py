# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GetBounds
                                 A QGIS plugin
 Copies the view extent to system clipboard
                             -------------------
        begin                : 2019-10-21
        copyright            : (C) 2019 by Jörgen Rosberg
        email                : rosberg.jorgen@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GetBounds class from file GetBounds.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .get_bounds import GetBounds
    return GetBounds(iface)
