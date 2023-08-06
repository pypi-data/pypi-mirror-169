# -*- coding: utf-8 -*-

#      Copyright (C)  2022. CQ Inversiones SAS.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         6/09/22 1:45 PM
# Project:      djangoPlugin
# Module Name:  error_messages
# ****************************************************************
from django.utils.translation import gettext as _


class ErrorMessages:
    """
    Error messages compilation
    """
    FIELD_REQUIRED = _("Error! The field is required.")
    CREATE_ERROR = _("Error! Record has not been created.")
    UPDATE_ERROR = _("Error! Record has not been updated.")
    NOT_FOUND = _("Error! There is not record matching.")
    DELETE_ERROR = _("Error! Record can not be deleted.")
    DATA_REQUIRED = _("Error! The data required not found.")
    DATABASE_ERROR = _("Error at database.")

