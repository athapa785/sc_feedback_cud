from pydm import Display
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import epics
import sys

class SCFeedback(Display):

	def __init__(self, parent = None, args = None):
		super(SCFeedback, self).__init__(parent = parent, args = args)
		#self.colorCharge()
		#self.colorLaser()
		#self.colorL0B()
		#self.colorL1B()
		#self.colorL1Bchirp()
		#self.colorBC2C()
		#self.colorBC2C_chrip()
		#self.colorL3B()
	
		
	def ui_filename(self):
		return 'sc_feedback_cud_v1.ui'
		
	def colorCharge(self):
		chrgstpt = epics.PV('TPG:SYS0:1:BUNCH_CHARGE_RBV')
		
		chrgrdbck = epics.PV('BPMS:GUNB:314:FW:CHRG_SLOW')
		
		upper = 40
		lower = 39.5
		
		"""
		#test
		if chrgrdbck.value > lower and chrgrdbck.value < upper:
			self.ui.g_csp.setStyleSheet('color:rgb(255, 255, 0);')
		elif chrgrdbck.value > upper:
			self.ui.g_csp.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.g_csp.setStyleSheet('color:rgb(0, 255, 0);')			
		
		"""
		
		if abs(chrgrdbck.value - chrgstpt.value) / chrgstpt.value > 0.1 and abs(chrgrdbck.value - chrgstpt.value) / chrgstpt.value < 0.15:
			self.ui.g_csp.setStyleSheet('color:rgb(255, 255, 0);')
		elif abs(chrgrdbck.value - chrgstpt.value) / chrgstpt.value > 0.15 and abs(chrgrdbck.value - chrgstpt.value) / chrgstpt.value < 0.2:
			self.ui.g_csp.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.g_csp.setStyleSheet('color:rgb(0, 255, 0);')
		
		
		#QApplication.processEvents()
			
	def colorLaser(self):
		laser_pwr = epics.PV('LASR:LGUN:220:LASER_PWR_READBACK')
		
		upper = 10
		lower = 3
		
		if laser_pwr.value > lower and laser_pwr.value < upper:
			self.ui.c_CSP1_2.setStyleSheet('color:rgb(255, 255, 0);')
		elif laser_pwr.value > upper:
			self.ui.c_CSP1_2.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_2.setStyleSheet('color:rgb(0, 255, 0);')
		
		#QApplication.processEvents()
		
			
	def colorL0B(self):
		lob = epics.PV('ACCL:L0B:0100:AL:EHEADRM')
		
		if lob.value < 5 and lob.value > 1:
			self.ui.c_CSP1_3.setStyleSheet('color:rgb(255, 255, 0);')
		elif lob.value < 1:
			self.ui.c_CSP1_3.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_3.setStyleSheet('color:rgb(0, 255, 0);')		
		
		#QApplication.processEvents()
			
	def colorL1B(self):
		l1b = epics.PV('ACCL:L1B:0200:AL:EHEADRM')
		
		if l1b.value < 20 and l1b.value > 5:
			self.ui.c_CSP1_4.setStyleSheet('color:rgb(255, 255, 0);')
		elif l1b.value < 5:
			self.ui.c_CSP1_4.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_4.setStyleSheet('color:rgb(0, 255, 0);')		
	
		#QApplication.processEvents()

	def colorL1Bchirp(self):
		l1b_c = epics.PV('ACCL:L1B:0200:AL:CHEADRM')
		
		if abs(l1b_c.value) < 10 and abs(l1b_c.value) > 5:
			self.ui.c_CSP1_5.setStyleSheet('color:rgb(255, 255, 0);')
		elif abs(l1b_c.value) < 5:
			self.ui.c_CSP1_5.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_5.setStyleSheet('color:rgb(0, 255, 0);')		

		#QApplication.processEvents()
		
			
	def colorBC2C(self):
		bc2b = epics.PV('ACCL:L2B:0400:AL:EHEADRM')
		
		if bc2b.value < 50 and bc2b.value > 10:
			self.ui.c_CSP1_6.setStyleSheet('color:rgb(255, 255, 0);')
		elif bc2b.value < 10:
			self.ui.c_CSP1_6.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_6.setStyleSheet('color:rgb(0, 255, 0);')		

		#QApplication.processEvents()
	
	def colorBC2C_chrip(self):
		bc2b_c = epics.PV('ACCL:L2B:0400:AL:CHEADRM')
		
		if abs(bc2b_c.value) < 25 and abs(bc2b_c.value) > 10:
			self.ui.c_CSP1_7.setStyleSheet('color:rgb(255, 255, 0);')
		elif abs(bc2b_c.value) < 10:
			self.ui.c_CSP1_7.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_7.setStyleSheet('color:rgb(0, 255, 0);')		

		#QApplication.processEvents()	
	
	def colorL3B(self):
		l3b = epics.PV('ACCL:L3B:1600:AL:EHEADRM')
		
		if l3b.value < 200 and l3b.value > 10:
			self.ui.c_CSP1_8.setStyleSheet('color:rgb(255, 255, 0);')
		elif l3b.value < 10:
			self.ui.c_CSP1_8.setStyleSheet('color:rgb(255, 0, 0);')
		else:
			self.ui.c_CSP1_8.setStyleSheet('color:rgb(0, 255, 0);')			
	
		#QApplication.processEvents()
			
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SCFeedback()
    window.show()
    sys.exit(app.exec_())
		
