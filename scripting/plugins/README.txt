1.��ѹ���������KICAD5.99���Ŀ¼�����磬��Windows�Ͽ����ǣ�C:\Users\Administrator\Documents\KiCad\5.99\scripting\plugins
2.����KiCad����ˢ�²��
3.������������볢���Թ���Ȩ������KiCad��


������һЩKICAD���õĲ��!

HierPlace	���ָ���				https://github.com/xesscorp/HierPlace
InteractiveHtmlBom	����BOM��		https://github.com/openscopeproject/InteractiveHtmlBom
KiBuzzard		��������			https://github.com/gregdavill/KiBuzzard
kicad_freerouting-plugin-master �Զ����� 	https://github.com/random-builder/kicad_freerouting-plugin
teardrops	���				https://github.com/NilujePerchut/kicad_scripts
kicad-action-scripts-master			https://github.com/jsreynaud/kicad-action-scripts
KiMesh	������				https://blog.jaseg.de/posts/kicad-mesh-plugin/
RF-tools-KiCAD-master RF���߰�		https://github.com/easyw/RF-tools-KiCAD
Ⱥ�ڴ���"��������"������޸���Σ�BGA�ȳ����߳���ʾ��https://github.com/beanjs-kicad/beantools
������߰�	https://github.com/easyw/kicad-action-tools
kicad_fab_tool	����gerber		https://github.com/wemos/kicad_fab_tool/
gerberzipper ����gerber			https://github.com/g200kg/kicad-gerberzipper
JLCPCB	�����ļ���� 			https://github.com/Bouni/kicad-jlcpcb-tools
ƴ���� https://github.com/msvisser/panelize-plugin
���ִ��� kicad-plugins-main			https://github.com/ian-ross/kicad-plugins
copper_thief-main����ͭ��			https://github.com/mrussell42/copper_thief
�������(���в�������ָ��Ƶ�)			https://github.com/MitjaNemec/Kicad_action_plugins
������Ȧ  					https://github.com/tristanitschner/kicad_spiral_plugin
�������ߺ͹��� 				https://github.com/Polarisru/KiFind
Ԫ������ 					https://github.com/szczygiel-pawel/swap-components-kicad-plugin

WINDOWS��KiBuzzard������װ�����°汾�Ѳ���Ҫ�ˣ�
1����װpython3����װʱ��ѡ�Զ����û�������ѡ�
2��python��װĿ¼����һ��python.exe���ĳ�python3.exe
3������KiBuzzard���Ŀ¼����д��������KiBuzzard_run.bat


kicad_freerouting-plugin-master �Զ�����������
��Ҫ��װJDK >=11
��ַ��https://www.oracle.com/java/technologies/javase-jdk16-downloads.html


2022/01/21:>>>>2.0
�޸�FabricationPositions������� m_AuxOrigin����GetAuxOrigin()
�޸�Snap2Grid���m_AuxOrigin����GetAuxOrigin()��m_GridOrigin����GetGridOrigin()
�޸�place_footprints���в��module.Flip(position)��������
�޸�kicad_fab_tool��������ļ�����
�޸���ͭcopper_thief���    dot.SetArcStart(start) dot.SetArcEnd(start)����dot.SetStart(start) dot.SetEnd(start)
����������Ȧ���ɲ�����޸���UI
�������߹����������
����Ԫ���������
�������в�������°汾


2021/11/17:>>>>1.9
���²��ֲ��
teardrops KiBuzzard jlcpcb-tools֮��ĳ�ͻ�����
IBOM���µ����°汾2.4.1
���FAB�����APIʧЧ����AttributeError: 'BOARD_DESIGN_SETTINGS' object has no attribute 'm_AuxOrigin'
�޸�3dģ�ͼ����

2021/10/10:>>>>1.8
�޸���β��ʧЧ���⡣
�޸�Create Labels��teardrops������µĽ���פ������
Ϊ���ִ��ݲ������Unicode��������֧�֡�
�޸�Replicate layout���ָ��Ʋ��BUG(������ɺ󲻸�����ʾ������ͭ����)

2021/10/1:>>>>1.7
������ֲ��copper_thief-main����ͭ�������
�������ִ��ݲ��SchematicPositionsToLayout��
����JLCPCB�Ȳ��ֲ��

2021/8/7:>>>>1.6
���²��ֲ��������JLCPCB�����ļ����
��ֲ5.1.x��ƴ����panelize
2021/7/28:>>>>1.5
�������޸�gerberzipper,���������������ں����С���
����ƴ���������ֲ����δ��ȫ�޸���
����Fab���������gerber.BOM��SMT�����ļ�
2021/7/12:>>>>1.4
�޸��ϰ汾BGA_tool�ȳ�����
��β��ȫ�����
2021/6/25:>>>>1.3.1
�޸���β���ĸ�ͭ��϶����
�޸������߷�װ��

2021/6/25:>>>>1.3
�޸����в�������Դ������й��ߺ���
�������˿�����Ԫ���ο�ֵ���ù��ߣ�δ���!

2021/6/10:>>>>1.2
�޸�һЩ���
2021/6/7:>>>>1.1
�޸�gerber to orderһ������gerber���
2021/5/19:>>>>1.0
�����˼���5.99�ϻ����ŵĲ�������ź���λ���֧��5.99


