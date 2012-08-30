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
import cairosvg
import pychart
import re
import unicodedata
import openerp.tools.config as config
FONTNAME = None

def wrap_unaligned_get_dimension(func):
    def _func(*args, **kwds):
        arg = args[0].decode('utf8') if type(args[0]) == str else args[0]
        # add 2 char size to east asian char
        for s in arg:
            if unicodedata.east_asian_width(s) != 'Na':
                arg = arg + u'  '
        return func(arg)
    return _func
pychart.font.unaligned_get_dimension = wrap_unaligned_get_dimension(pychart.font.unaligned_get_dimension)

def wrap_font_text_iterator_reset(func):
    def _func(*args, **kwds):
        return func(args[0], args[1].decode('utf8') if type(args[1]) == str else args[1])
    return _func
pychart.font.text_iterator.reset = wrap_font_text_iterator_reset(pychart.font.text_iterator.reset)

def wrap_canvas_init(func):
    def _func(*args, **kwds):
        if kwds.get('format', 'pdf') == 'pdf':
            kwds['format'] = 'svg'
        return func(*args, **kwds)
    return _func
pychart.canvas.init = wrap_canvas_init(pychart.canvas.init)

def wrap_svgcanvas_close(func):
    def _func(*args, **kwds):
        func(*args, **kwds)
        fio = args[0]._T__out_fname
        svg = fio.getvalue()
        svg = re.sub(r'font-family:[\w]+;', 'font-family:%s;' % FONTNAME or config.get('pychart_ttfont_name', 'Simsun'), svg)
        fio.truncate(0)
        cairosvg.surface.PDFSurface.convert(bytestring = svg, write_to = fio)
    return _func
pychart.svgcanvas.T.close = wrap_svgcanvas_close(pychart.svgcanvas.T.close)

# read oe_cn_base_fonts setting
from tools.safe_eval import safe_eval
import openerp.addons.base.res.res_company as res_company
def wrap_res_company_init(func):
    def _func(*args, **kwds):
        func(*args, **kwds)
        global FONTNAME
        try:
            fonts_map = args[1].get('ir.config_parameter').get_param(args[2], 1, 'fonts_map')
            fonts_map = (safe_eval(fonts_map))
            if fonts_map.get('wrap', False):
                FONTNAME = fonts_map['maps'][0][1].encode('utf-8')
        except:
            pass
    return _func
res_company.res_company.__init__ = wrap_res_company_init(res_company.res_company.__init__)






# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
