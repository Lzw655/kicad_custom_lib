import pcbnew
import os
from pcbnew import wxPoint
from pcbnew import ActionPlugin, GetBoard
def ref2pos( pcb,position):
	offset=0
	# if pcb is None:
	board=pcbnew.GetBoard()
	fps=board.GetFootprints()
	# getpos(fps,0)
	for fp in fps:
		ref=fp.Reference()
		
		bb=fp.GetBoundingBox()
		left = bb.GetLeft()
		top = bb.GetTop()
		right = bb.GetRight()
		bottom = bb.GetBottom()
		width = (right-left)
		height = (bottom-top)
		if position == 1:
			ref.SetPosition(wxPoint(left+offset,top+offset))
		elif position == 2:
			ref.SetPosition(wxPoint(left+width/2,top))
		elif position == 3:
			ref.SetPosition(wxPoint(left+width,top))
		elif position == 4:
			ref.SetPosition(wxPoint(left,top+height/2))
		elif position == 5:
			ref.SetPos0(wxPoint(0,0))
		elif position == 6:
			ref.SetPosition(wxPoint(left+width,top+height))
		elif position == 7:
			ref.SetPosition(wxPoint(left,top+height))
		elif position == 8:
			ref.SetPosition(wxPoint(left+width/2,top+height))
		elif position == 9:
			ref.SetPosition(wxPoint(left+width,top+height))
		else:
			print("")



def get_modules_bounding_box(self, modules):
	# get the pivot bounding box
	bounding_box = modules[0].mod.GetFpPadsLocalBbox()
	top = bounding_box.GetTop()
	bottom = bounding_box.GetBottom()
	left = bounding_box.GetLeft()
	right = bounding_box.GetRight()
	for mod in modules:
		mod_box = mod.mod.GetFpPadsLocalBbox()
		top = min(top, mod_box.GetTop())
		bottom = max(bottom, mod_box.GetBottom())
		left = min(left, mod_box.GetLeft())
		right = max(right, mod_box.GetRight())

	position = pcbnew.wxPoint(left, top)
	size = pcbnew.wxSize(right - left, bottom - top)
	bounding_box = pcbnew.EDA_RECT(position, size)
	height = (bottom-top)/1000000.0
	width = (right-left)/1000000.0
	return height, width

def get_modules_bounding_box_center(self, modules):
	# get the pivot bounding box
	bounding_box = modules[0].mod.GetFpPadsLocalBbox()
	top = bounding_box.GetTop()
	bottom = bounding_box.GetBottom()
	left = bounding_box.GetLeft()
	right = bounding_box.GetRight()
	for mod in modules:
		mod_box = mod.mod.GetFpPadsLocalBbox()
		top = min(top, mod_box.GetTop())
		bottom = max(bottom, mod_box.GetBottom())
		left = min(left, mod_box.GetLeft())
		right = max(right, mod_box.GetRight())

	position = pcbnew.wxPoint(left, top)
	size = pcbnew.wxSize(right - left, bottom - top)
	bounding_box = pcbnew.EDA_RECT(position, size)
	pos_y = (bottom+top)/2
	pos_x = (right+left)/2
	return (pos_x, pos_y)


