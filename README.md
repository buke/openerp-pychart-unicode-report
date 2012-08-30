openerp-pychart-unicode-report
==============================

Update
---------------
2012-08-30  增加读取oecn_base_fonts字体名

简介
---------------
支持pychart中文报表，如“库存预测”、“工作中心负载” 等报表。

本模块原理是先让pychart 生成svg 文件，然后用cairosvg 模块生成PDF报表。

依赖模块
---------------
python-cairo python-cairosvg

Debian/Ubuntu安装方法： $ su apt-get install python-cairo python-cairosvg

字体配置
---------------
如果你安装了oecn_base_fonts模块，会自动读取oecn_base_fonts 的字体设置.

否则将会读取 OpenERP 配置文件中的 pychart_ttfont_name 参数, 示例如下:

; 默认使用宋体，可以修改。注意字体文件必须存在系统字体目录下。
pychart_ttfont_name = Simsun

玩的开心 ~

更多信息请查看本人博客 http://my.oschina.net/wangbuke


