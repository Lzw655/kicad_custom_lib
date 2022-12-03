#!/usr/bin/env python

# Teardrop for pcbnew using filled zones
# This is the plugin WX dialog
# (c) Niluje 2019 thewireddoesntexist.org
#
# Based on Teardrops for PCBNEW by svofski, 2014 http://sensi.org/~svo
# Cubic Bezier upgrade by mitxela, 2021 mitxela.com

import wx
import pcbnew
import os
import time
from .TextPos_gui import TextPos_gui
# from .TextPos import __version__
from .func import ref2pos

class TextPosDialog(TextPos_gui):
    """Class that gathers all the Gui control"""

    def __init__(self, board):
        """Init the brand new instance"""
        super(TextPosDialog, self).__init__(None)
        self.board = board
        self.SetTitle("Component Text Position")
        # self.rbx_action.Bind(wx.EVT_RADIOBOX, self.onAction)
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.but_cancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.but_ok.Bind(wx.EVT_BUTTON, self.onProcessAction)
        self.SetMinSize(self.GetSize())

    def onAction(self, e):
        """Enables or disables the parameters/options elements"""


    def onProcessAction(self, event):
        """Executes the requested action"""
        # start = time.time()
        # if self.id is None
           # continue
        if self.id==11:
           print("11")
           ref2pos(self.board,1)
        elif self.id==22:
           print("22")
           ref2pos(self.board,2)
        elif self.id==33:
           print("33")
           ref2pos(self.board,3)
        elif self.id==44:
           print("44")
           ref2pos(self.board,4)
        elif self.id==55:
           print("55")
           ref2pos(self.board,5)
        elif self.id==66:
           print("66")
           ref2pos(self.board,6)
        elif self.id==77:
           print("77")
           ref2pos(self.board,7)
        elif self.id==88:
           print("88")
           ref2pos(self.board,8)
        elif self.id==99:
           print("99")
           ref2pos(self.board,9)
        else :
           print("00")

        # wx.MessageBox("ok")
        pcbnew.Refresh()
        self.EndModal(wx.ID_OK)

    def onCloseWindow(self, event):
        self.EndModal(wx.ID_CANCEL)


def InitTextPosDialog(board):
    """Launch the dialog"""
    tg = TextPosDialog(board)
    tg.ShowModal()
    return tg
