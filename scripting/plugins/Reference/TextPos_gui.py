# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 12 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
###########################################################################
## Class teardrop_gui
###########################################################################

class TextPos_gui ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SetTextPosition", pos = wx.DefaultPosition, size = wx.Size( 380,420 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		import sys
		if sys.version_info[0] == 2:
			self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		else:
			self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		txt1 = wx.StaticText( self, wx.ID_ANY, u"Refrence：", wx.DefaultPosition, wx.DefaultSize, 0 )
		panel = wx.Panel(self)
		panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		
		self.rb1 = wx.RadioButton(panel,11, label = '', style = wx.RB_GROUP) 
		self.rb2 = wx.RadioButton(panel,22, label = '') 
		self.rb3 = wx.RadioButton(panel,33, label = '')
		self.rb4 = wx.RadioButton(panel,44, label = '') 
		self.rb5 = wx.RadioButton(panel,55, label = '') 
		self.rb6 = wx.RadioButton(panel,66, label = '')
		self.rb7 = wx.RadioButton(panel,77, label = '') 
		self.rb8 = wx.RadioButton(panel,88, label = '') 
		self.rb9 = wx.RadioButton(panel,99, label = '')
		
		self.rb1.SetValue(False)
		self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
		
		gs=wx.GridSizer(cols=3, rows=3, vgap=100,hgap=100)
		gs.AddMany([
			(self.rb1, 0, wx.EXPAND),
			(self.rb2, 0, wx.EXPAND),
			(self.rb3, 0, wx.EXPAND),
			(self.rb4, 0, wx.EXPAND),
			(self.rb5, 0, wx.EXPAND),
			(self.rb6, 0, wx.EXPAND),
			(self.rb7, 0, wx.EXPAND),
			(self.rb8, 0, wx.EXPAND),
			(self.rb9, 0, wx.EXPAND)
		])
		panel.SetSizer(gs)
		
		bmain = wx.BoxSizer( wx.VERTICAL )
		bmain.Add( txt1, 0, wx.LEFT, 10 )
		bmain.Add( panel, 0, wx.ALL|wx.ALIGN_CENTER, 10 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bmain.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		box1 = wx.BoxSizer( wx.HORIZONTAL )

		self.but_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		box1.Add( self.but_cancel, 0, wx.ALL, 5 )

		self.but_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		box1.Add( self.but_ok, 0, wx.ALL, 5 )


		bmain.Add( box1, 0, wx.ALIGN_RIGHT, 5 )

		self.SetSizer( bmain )
		self.Layout()

		self.Centre( wx.BOTH )
	def scale_bitmap(bitmap, width, height):
		image = wx.ImageFromBitmap(bitmap)
		image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
		result = wx.BitmapFromImage(image)
		return result
	def OnRadiogroup(self, e):
		rb = e.GetEventObject()
		self.id=rb.GetId()
		print(rb.GetLabel(),' is clicked from Radio Group')
		# wx.MessageBox("{} is selected".format(self.id))
		
	def OnEraseBack(self,event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".", "fpx.png"))
		dc.DrawBitmap(bmp, 32, 25)
	def __del__( self ):
		pass


