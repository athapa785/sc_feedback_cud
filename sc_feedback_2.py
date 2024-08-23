#Author: Adi (aaditya@slac.stanford.edu)

from pydm import Display
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import epics
import sys
from pydm.widgets.channel import PyDMChannel
from pydm.widgets.label import PyDMLabel



#Global Variables

STYLESHEET_OK = "color: black; background-color: rgb(80, 255, 80); border-radius: 6px;"
STYLESHEET_NOT = "color: white; background-color: rgb(100, 100, 100); border-radius: 6px;"
STAT_FONT_1 = QtGui.QFont()
STAT_FONT_1.setBold(True)
STAT_FONT_1.setPointSize(22)
STAT_FONT_2 = QtGui.QFont()
STAT_FONT_2.setBold(True)
STAT_FONT_2.setPointSize(16)


class SC_Feedback(Display):

	def __init__(self, parent = None, args = None):
		super(SC_Feedback, self).__init__(parent = parent, args = args)
		
		#longitudinal feedbacks
		
		self.lh_e_stat =    FixedTextLabel('PHYS:SYS0:1:SCLFB_LH', 'Laser Heater \n Energy', ok_state=1)
		self.bc1b_e_stat =  FixedTextLabel('PHYS:SYS0:1:SCLFB_L1B_E', 'BC1B Energy', ok_state=1)
		self.bc1b_bl_stat = FixedTextLabel('PHYS:SYS0:1:SCLFB_L1B_BL', 'BC1B Bunch \n Length', ok_state=1)
		self.bc2b_e_stat =  FixedTextLabel('PHYS:SYS0:1:SCLFB_L2B_E', 'BC2B Energy', ok_state=1)
		self.bc2b_bl_stat = FixedTextLabel('PHYS:SYS0:1:SCLFB_L2B_BL', 'BC2B Bunch \n Length', ok_state=1)
		self.dl_e_stat =    FixedTextLabel('PHYS:SYS0:1:SCLFB_DL', 'Dogleg Energy', ok_state=1)
		
		vlayouts = [
		    self.LH_E_vlayout,
		    self.BC1B_E_vlayout,
		    self.BC1B_BL_vlayout,
		    self.BC2B_E_vlayout,
		    self.BC2B_BL_vlayout,
		    self.DL_E_vlayout,
		    ]
		labels = [
		    self.lh_e_stat,
		    self.bc1b_e_stat,
		    self.bc1b_bl_stat,
		    self.bc2b_e_stat,
		    self.bc2b_bl_stat,
		    self.dl_e_stat,
		    ]
		
		for layout, stat in zip(vlayouts, labels):
		    layout.addWidget(stat)

		
		
		#transverse feedbacks
		
		self.htr_stat = FixedTextLabel('FBCK:FB06:TR02:STATUS', 'HTR Launch', font= STAT_FONT_2, ok_state=2)
		self.diag0_stat = FixedTextLabel('FBCK:FB06:TR03:STATUS', 'DIAG0 Launch', font= STAT_FONT_2, ok_state=2)
		self.l1b_stat = FixedTextLabel('FBCK:FB06:TR04:STATUS', 'L1B Launch', font=STAT_FONT_2, ok_state=2)
		self.l2b_stat = FixedTextLabel('FBCK:FB06:TR05:STATUS', 'L2B Launch', font=STAT_FONT_2, ok_state=2)
		self.l3b_stat = FixedTextLabel('FBCK:FB06:TR01:STATUS', 'L3B Launch', font=STAT_FONT_2, ok_state=2)
		self.byp_stat = FixedTextLabel('FBCK:FB06:TR06:STATUS', 'BYP Launch', font=STAT_FONT_2, ok_state=2)
		self.ltuh_stat = FixedTextLabel('FBCK:FB03:TR01:STATUS', 'LTUH Launch', font=STAT_FONT_2, ok_state=2)
		self.ltus_stat = FixedTextLabel('FBCK:FB04:TR01:STATUS', 'LTUS Launch', font=STAT_FONT_2, ok_state=2)
		self.undh_stat = FixedTextLabel('FBCK:FB03:TR04:STATUS', 'UNDH Launch', font=STAT_FONT_2, ok_state=2)
		self.unds_stat = FixedTextLabel('FBCK:FB04:TR02:STATUS', 'UNDS Launch', font=STAT_FONT_2, ok_state=2)
		
		self.HTR_D.addWidget(self.htr_stat)
		self.HTR_D.addWidget(self.diag0_stat)
		
		self.L1B_L2B.addWidget(self.l1b_stat)
		self.L1B_L2B.addWidget(self.l2b_stat)
		
		self.L3B_BYP.addWidget(self.l3b_stat)
		self.L3B_BYP.addWidget(self.byp_stat)
		
		self.LTU.addWidget(self.ltuh_stat)
		self.LTU.addWidget(self.ltus_stat)
		
		self.UND.addWidget(self.undh_stat)
		self.UND.addWidget(self.unds_stat)
	
						
	def ui_filename(self):
		return 'sc_feedback_cud_2point0.ui'
		
	
	
#custom PyDMLabel	

class FixedTextLabel(PyDMLabel):
    def __init__(self, channel, fixed_name, ok_state=1, font=STAT_FONT_1, parent=None):
        super(FixedTextLabel, self).__init__(parent=parent)
        self.channel = channel
        self.ok_state = ok_state
        self.fixed_name = fixed_name
        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setFrameShape(QFrame.WinPanel)
        

    def value_changed(self, new_value):
        super(FixedTextLabel, self).value_changed(new_value)
        self.setText(self.fixed_name)
        if new_value == self.ok_state: self.setStyleSheet(STYLESHEET_OK)
        else: self.setStyleSheet(STYLESHEET_NOT)
        return

		

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SC_Feedback()
    window.show()
    sys.exit(app.exec_())
