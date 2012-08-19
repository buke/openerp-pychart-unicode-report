openerp-pychart-unicode-report
==============================

PyChart Unicode Report (Support CJK Font)

Add unicode suppoert to pychart report, such as "Stock Level Forecase" or "Work Center Load" etc.

This module let pychart make report as svg file, then use cairosvg turn svg to pdf file.

Depend on python-cairo & python-cairosvg.

Install it on Debian/Ubuntu: $ su apt-get install python-cairo python-cairosvg

You must set TTFont name in OpenERP config file, as below:

; Simsun is chinese font name, insteaded by your font(the font file must exist in you sys font path)
pychart_ttfont_name = Simsun

Have fun !

----------------------------------------------------------

支持pychart中文报表，如“库存预测”、“工作中心负载” 等报表。

本模块原理是先让pychart 生成svg 文件，然后用cairosvg 模块生成PDF报表。

依赖模块：python-cairo python-cairosvg

Debian/Ubuntu安装方法： $ su apt-get install python-cairo python-cairosvg

可以在OpenERP中配置pychart 报表字体：

; 默认使用宋体，可以修改。注意字体文件必须存在系统字体目录下。
pychart_ttfont_name = Simsun

祝你好运 ~


