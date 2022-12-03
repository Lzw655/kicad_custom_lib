import pcbnew
import os
from pcbnew import wxPoint
from pcbnew import ActionPlugin, GetBoard
from .TextPos_dialog import InitTextPosDialog

class TextPos(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "SetRef 1.0"
        self.category = "Artistic PCBs"
        self.description = "批量设置参考值位置"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'REF.png') # Optional, defaults to ""

    def Run(self):
        # The entry function of the plugin that is executed on user action
        InitTextPosDialog(GetBoard())

TextPos().register() # Instantiate and register to Pcbnew



