# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sheet Width Relative
#
#    Copyright (C) 2015 ICTSTUDIO (<http://www.ictstudio.eu>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Sheet Width Relative',
    'version': '8.0.1.0.1',
    'author' : 'ICTSTUDIO, André Schenkels',
    'category': 'Web',
    'description': 'Sheet width relative to screen size',
    'license': 'AGPL-3',
    'category': 'Tools',
    'depends': [
        'web',
        ],
    'data': [
        'views/qweb.xml',
        ],
    'installable': True,
}