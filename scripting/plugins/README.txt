1.解压缩插件包到KICAD5.99插件目录。例如，在Windows上可能是：C:\Users\Administrator\Documents\KiCad\5.99\scripting\plugins
2.重启KiCad或者刷新插件
3.如果遇到错误，请尝试以管理权限运行KiCad。


整理了一些KICAD常用的插件!

HierPlace	布局辅助				https://github.com/xesscorp/HierPlace
InteractiveHtmlBom	智能BOM表		https://github.com/openscopeproject/InteractiveHtmlBom
KiBuzzard		任意字体			https://github.com/gregdavill/KiBuzzard
kicad_freerouting-plugin-master 自动布线 	https://github.com/random-builder/kicad_freerouting-plugin
teardrops	泪滴				https://github.com/NilujePerchut/kicad_scripts
kicad-action-scripts-master			https://github.com/jsreynaud/kicad-action-scripts
KiMesh	反逆向				https://blog.jaseg.de/posts/kicad-mesh-plugin/
RF-tools-KiCAD-master RF工具包		https://github.com/easyw/RF-tools-KiCAD
群内大佬"超级菜鸟"插件（修复泪滴，BGA扇出，线长显示）https://github.com/beanjs-kicad/beantools
插件工具包	https://github.com/easyw/kicad-action-tools
kicad_fab_tool	生成gerber		https://github.com/wemos/kicad_fab_tool/
gerberzipper 生成gerber			https://github.com/g200kg/kicad-gerberzipper
JLCPCB	生产文件插件 			https://github.com/Bouni/kicad-jlcpcb-tools
拼板插件 https://github.com/msvisser/panelize-plugin
布局传递 kicad-plugins-main			https://github.com/ian-ross/kicad-plugins
copper_thief-main（盗铜）			https://github.com/mrussell42/copper_thief
插件集合(阵列插件、布局复制等)			https://github.com/MitjaNemec/Kicad_action_plugins
螺旋线圈  					https://github.com/tristanitschner/kicad_spiral_plugin
搜索布线和过孔 				https://github.com/Polarisru/KiFind
元件互换 					https://github.com/szczygiel-pawel/swap-components-kicad-plugin

WINDOWS下KiBuzzard依赖安装：（新版本已不需要了）
1、安装python3（安装时勾选自动设置环境变量选项）
2、python安装目录复制一份python.exe并改成python3.exe
3、运行KiBuzzard插件目录下我写的批处理KiBuzzard_run.bat


kicad_freerouting-plugin-master 自动布线启动器
需要安装JDK >=11
地址：https://www.oracle.com/java/technologies/javase-jdk16-downloads.html


2022/01/21:>>>>2.0
修复FabricationPositions插件报错 m_AuxOrigin换成GetAuxOrigin()
修复Snap2Grid插件m_AuxOrigin换成GetAuxOrigin()和m_GridOrigin换成GetGridOrigin()
修复place_footprints阵列插件module.Flip(position)参数报错
修复kicad_fab_tool插件生产文件生成
修复盗铜copper_thief插件    dot.SetArcStart(start) dot.SetArcEnd(start)换成dot.SetStart(start) dot.SetEnd(start)
新增螺旋线圈生成插件并修复其UI
新增布线过孔搜索插件
新增元件互换插件
更新所有插件到最新版本


2021/11/17:>>>>1.9
更新部分插件
teardrops KiBuzzard jlcpcb-tools之间的冲突解决了
IBOM更新到最新版本2.4.1
解决FAB插件的API失效问题AttributeError: 'BOARD_DESIGN_SETTINGS' object has no attribute 'm_AuxOrigin'
修复3d模型检测插件

2021/10/10:>>>>1.8
修复泪滴插件失效问题。
修复Create Labels和teardrops插件导致的进程驻留问题
为布局传递插件增加Unicode编码中文支持。
修复Replicate layout布局复制插件BUG(复制完成后不更新显示布线铺铜问题)

2021/10/1:>>>>1.7
新增移植的copper_thief-main（盗铜）插件。
新增布局传递插件SchematicPositionsToLayout。
更新JLCPCB等部分插件

2021/8/7:>>>>1.6
更新部分插件，新增JLCPCB生产文件插件
移植5.1.x的拼版插件panelize
2021/7/28:>>>>1.5
新增并修复gerberzipper,添加两个插件包，内含多个小插件
新增拼板插件，布局插件等未完全修复。
新增Fab插件，导出gerber.BOM与SMT坐标文件
2021/7/12:>>>>1.4
修复老版本BGA_tool扇出工具
泪滴插件全面可用
2021/6/25:>>>>1.3.1
修复泪滴插件的覆铜间隙设置
修复螺旋线封装向导

2021/6/25:>>>>1.3
修复阵列插件，比自带的阵列工具好用
新增个人开发的元件参考值放置工具，未完成!

2021/6/10:>>>>1.2
修复一些插件
2021/6/7:>>>>1.1
修复gerber to order一键导出gerber插件
2021/5/19:>>>>1.0
整理了几个5.99上还活着的插件，很遗憾泪滴还不支持5.99


