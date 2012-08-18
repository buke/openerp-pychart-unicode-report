# -*- coding: utf-8 -*-
##############################################################################
#    PyChart Unicode Report (Support CJK Font)
#    Copyright 2012 wangbuke <wangbuke@gmail.com>
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
    "name": "PyChart Unicode Report (Support CJK Font)",
    'version': '1.0',
    "depends" : ["base", ],
    "category" : "Localization",
    'description': """
PyChart Unicode Report (Support CJK Font)

Add unicode suppoert to pychart report, such as "Stock Level Forecase" or "Work Center Load" etc.

This module let pychart make report as svg file, then use cairosvg turn svg to pdf file.

Depend on python-cairosvg.
Install it on Debian/Ubuntu use:  $ su apt-get install python-cairosvg

You must set TTFont name in OpenERP config file, as below:

; Simsun is chinese font name, insteaded by your font(the font file must exist in you sys font path)
pychart_ttfont_name = Simsun

Have fun !

----------------------------------------------------------

支持pychart中文报表，如“库存预测”、“工作中心负载” 等报表。

本模块原理是先让pychart 生成svg 文件，然后用cairosvg 模块生成PDF报表。

依赖模块：python-cairosvg
Debian/Ubuntu安装方法： $ su apt-get install python-cairosvg

可以在OpenERP中配置pychart 报表字体：
; 默认使用宋体，可以修改。注意字体文件必须存在系统字体目录下。
pychart_ttfont_name = Simsun

祝你好运 ~

    """,
    'author': 'wangbuke@gmail.com',
    'website': 'http://my.oschina.net/wangbuke',
    'license': 'AGPL-3',
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
