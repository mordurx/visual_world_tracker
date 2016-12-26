#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.
OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""
from openexp._canvas import canvas
from openexp._coordinates.legacy import legacy as legacy_coordinates
from expyriment import stimuli
from Utilities import Utilities
from openexp.canvas import canvas
from libopensesame.py3compat import *
from PyQt4 import QtCore, QtGui
from libopensesame import debug
from libqtopensesame.extensions import base_extension
from PyQt4 import QtGui
from PyQt4.QtGui import *
from libopensesame import debug
from libopensesame import metadata
from libqtopensesame.misc import _
from libqtopensesame.extensions import base_extension
from libqtopensesame.misc.base_subcomponent import base_subcomponent
from libqtopensesame.misc.config import cfg
from libopensesame.py3compat import *
import xlrd
import xlwt
from libopensesame.experiment import experiment
from expyriment import design, control, stimuli, io, misc
from openexp.backend import backend, configurable
import os
from libopensesame.experiment import experiment
from libopensesame import item
from libopensesame.inline_script import inline_script
from libopensesame.exceptions import osexception

class action_page(QtGui.QAction, base_subcomponent):

	"""
	desc:
		A menu entry for a single help page.
	"""

	def __init__(self, main_window):

		"""
		desc:
			Constructor.
		arguments:
			main_window:	The main-window object.
			title:			The menu title.
			link:			The URL to open.
			menu:			The menu for the action.
		"""

		QtGui.QAction.__init__(self, main_window.theme.qicon(
			u'applications-internet'))
		self.setup(main_window)
		
	






class visual_world(base_extension):

	"""
	desc:
		An example extension that lists all available events.
	"""
	
	def activate(self):

		"""
		desc:
			Is called when the extension is activated through the menu/ toolbar
			action.
		"""
		self.cargar_excel()
		debug.msg(u'Example extension activated')

	# Below is a list of event handlers, which you can implement to have your
	# extension react to specific events.

	def event_startup(self):
		#QMessageBox.information(self.main_window, "Message", "event_startup")
		debug.msg(u'Event fired: startup')
		
		

	def event_prepare_regenerate(self):
		debug.msg(u'Event fired: prepare_regenerate')

	def event_regenerate(self):
		debug.msg(u'Event fired: regenerate')

	def event_run_experiment(self, fullscreen):
		debug.msg(u'Event fired: run_experiment(fullscreen=%s)' % fullscreen)

	def event_end_experiment(self, ret_val):
		debug.msg(u'Event fired: end_experiment')

	def event_save_experiment(self, path):
		debug.msg(u'Event fired: save_experiment(path=%s)' % path)

	def event_open_experiment(self, path):
		debug.msg(u'Event fired: open_experiment(path=%s)' % path)
		#QMessageBox.information(self.main_window, "Message", path)

	def event_close(self):
		debug.msg(u'Event fired: close')

	def event_prepare_rename_item(self, from_name, to_name):
		debug.msg(
			u'Event fired: prepare_rename_item(from_name=%s, to_name=%s)' \
			% (from_name, to_name))

	def event_rename_item(self, from_name, to_name):
		debug.msg(u'Event fired: rename_item(from_name=%s, to_name=%s)' \
			% (from_name, to_name))

	def event_new_item(self, name, _type):
		debug.msg(u'Event fired: new_item(name=%s, _type=%s)' % (name, _type))

	def event_change_item(self, name):
		debug.msg(u'Event fired: change_item(name=%s)' % name)

	def event_prepare_change_experiment(self):
		debug.msg(u'Event fired: prepare_change_experiment')

	def event_change_experiment(self):
		debug.msg(u'Event fired: change_experiment')

	def event_prepare_delete_item(self, name):
		debug.msg(u'Event fired: prepare_delete_item(name=%s)' % name)

	def event_delete_item(self, name):
		debug.msg(u'Event fired: delete_item(name=%s)' % name)

	def event_prepare_purge_unused_items(self):
		debug.msg(u'Event fired: prepare_purge_unused_items')

	def event_purge_unused_items(self):
		debug.msg(u'Event fired: purge_unused_items')
	def cargar_excel(self):
		print "xd"
		"""Locates the experiment file."""
		file_type_filter = "Excel (*.xlsx *.xls )"
		path = QtGui.QFileDialog.getOpenFileName(self.main_window, "Open experiment file", filter = file_type_filter)
		
		w = QWidget()
		if path=='':
			return
		
		xl_workbook = xlrd.open_workbook(path)
		
		# List sheet names, and pull a sheet by name
		sheet_names = xl_workbook.sheet_names()
		print('Sheet Names', sheet_names)
		xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
		row = xl_sheet.row(1)
		num_cols = xl_sheet.ncols   # Number of columns
		self.num_rows = xl_sheet.nrows-1   # Number of rows
		for row_idx in range(1, xl_sheet.nrows):
			 for col_idx in range(0, num_cols):  # Iterate through columns
				cell_obj = xl_sheet.cell(row_idx, col_idx)
				#QMessageBox.information(w, "Message", str(cell_obj))
		filename = QtGui.QFileDialog.getSaveFileName(self.main_window, "Guardar proyecto", "", "*.osexp")
		#carpeta_proyecto=os.path.dirname(os.path.abspath(filename))
		carpeta_proyecto=os.path.dirname(filename)
		if not os.path.exists(carpeta_proyecto+'/results'):
			os.makedirs(carpeta_proyecto+'/results')
		#QMessageBox.information(w, "Message", str(xd))
		file = open(filename, "w")
		
		#------------------------------------------------------------------------------------
		#file.write("API: 2\n")
		#file.write("OpenSesame: 3.0.5\n")
		#file.write("Platform: nt\n")
		file.write("set width 1024 \n")
		file.write("set uniform_coordinates 'no' \n")
		file.write("set synth_backend 'legacy' \n")
		
		file.write("set title 'visual_world' \n")
		file.write("set subject_parity 'even' \n")
		file.write("set subject_nr 0 \n")
		file.write("set start 'experimentoseq' \n")  #esta variable esta relacionada con "define sequence" debe ser el mismo nombre 
		file.write("set height 768 \n")
		file.write("set foreground 'black' \n")
		file.write("set description 'Default description' \n")
		file.write("set coordinates 'uniform' \n")
		file.write("set compensation 0 \n")
		file.write("set canvas_backend 'legacy' \n")
		file.write("set background 'white' \n")
		# crear sequencia por defecto , esta esta ligada al proyecto no se puede borrar
		file.write("\n")
		file.write("define sequence experimentoseq \n")
		file.write("\tset flush_keyboard 'yes' \n")
		file.write("\tset description 'Runs a number of items in sequence' \n")
		file.write("\trun form_text_display always\n")
		file.write("\trun pygaze_init always\n")
		file.write("\t run load_pool\n")
		file.write("\trun block_loop always\n")
		file.write("\trun save_data_cvs\n")
		
		### partir calibrando
		file.write("\n")
		file.write("define form_text_display form_text_display \n")
		file.write("\tset timeout 'infinite' \n")
		file.write("\tset spacing 10 \n")
		file.write("\tset rows '1;4;1' \n")
		file.write("\tset only_render 'no'\n")
		file.write("\tset ok_text 'Ok'\n")
		file.write("\tset margins '50;50;50;50'\n")
		file.write("\tset form_title '<span size=24>Calibracion</span>'\n")
		file.write("\t__form_text__\n")
		file.write("\t<span size=20> Usted verá cuatro objetos en la pantalla y escuchara una palabra.\n\tPor favor ponga atención a lo que ve y escucha.\n\tPuede mirar donde quiera, pero mantenga sus ojos sobre el monitor durante el experimento.\n\n\tPara comenzar porfavor, mire fijamente cada punto que aparezca en la pantalla.</span>\n")
		#file.write("\tset form_text '<span size=14>Usted verá cuatro objetos en la pantalla y escuchara una palabra.</span>'\n")
		file.write("\t__end__\n")
		
		file.write("\tset description 'A simple text display form'\n")
		file.write("\tset cols '1;1;1' \n")
		file.write("\tset _theme 'gray' \n")
		file.write("\twidget 0 0 3 1 label text='[form_title]'\n")	
		file.write("\twidget 0 1 3 1 label center=no text='[form_text]'\n")
		file.write("\twidget 1 2 1 1 button text='[ok_text]' \n")
		###  iniciar pygaze init
		file.write("\n")
		file.write("define pygaze_init pygaze_init \n")
		file.write("\tset tracker_type 'EyeTribe' \n")
		file.write("\tset smi_send_port 4444 \n")
		file.write("\tset smi_recv_port 5555 \n")
		file.write("\tset smi_ip '127.0.0.1' \n")
		file.write("\tset sacc_vel_thr 33 \n")
		file.write("\tset sacc_acc_thr 9500\n")
		file.write("\tset eyelink_pupil_size_mode 'area'\n")
		file.write("\tset eyelink_force_drift_correct 'yes'\n")
		file.write("\tset description 'Initialize and calibrate eye tracker'\n")
		file.write("\tset calibrate 'yes'\n")
		file.write("\tset calbeep 'no'\n")
		file.write("\tset _logfile 'automatic'\n")
	
	    
	
	
	
		
		
		#crear loop
		file.write("define loop block_loop \n")
		
		
		#obtener variable nombre de colunmas del excel
		ordenColumna=""
		vectorColsName=[]		
		for row_idx in range(0, 1):
			for col_idx in range(0, num_cols):
				cell_obj = xl_sheet.cell(row_idx, col_idx).value
				vectorColsName.append(cell_obj)
				ordenColumna=ordenColumna+cell_obj+";"
				
		
		# set column_order "image_1;image_2;image_3;image_4;oracion;timeless;fade"
		file.write("\t set column_order "+ordenColumna+" \n")
		file.write("\t  set cycles '"+str(self.num_rows)+"' \n")# set cycles "4"
		#file.write("\t set item '_trial_sequence' \n")# set item "_trial_sequence"
		file.write("\t set order 'random' \n")# set order "sequential"
		file.write("\t set repeat '1' \n")# set repeat "1"
		#file.write("\t set skip '0' \n")# set skip "0"
		file.write("\t set offset 'yes'\n")#set offset "no"
		contadorVueltas=0
		contadorCols=0
		# se cargar todas las variables de experimento , es este caso desde el excel
		for row_idx in range(1, xl_sheet.nrows):
			 for col_idx in range(0, num_cols):  # Iterate through columns
				cell_obj = xl_sheet.cell(row_idx, col_idx).value
					
				file.write("\t setcycle "+str(contadorVueltas)+" "+vectorColsName[contadorCols]+" "+str(cell_obj)+ "\n")# ciclos
				#QMessageBox.information(w, "Message", str(cell_obj))
				contadorCols=contadorCols+1
			 contadorCols=0	
			 contadorVueltas=contadorVueltas+1	
		file.write("\t run trial_sequence\n")
        
		##################### script to cargar datos al pool
		file.write("define inline_script load_pool \n")# codigo en python inline_script TO add many sequences
		file.write("\t set description 'add dato to pool' \n")# crear trial
		file.write("\t set _run '' \n")# set run part}
		file.write("\t___prepare__\n")
		
		utilidad=Utilities('img',path)
		cols_image=utilidad.get_images()  
		print cols_image
		
		utilidad2=Utilities('sound',path)
		cols_sound=utilidad2.get_sound()#obtitene todos los sonidos  
		
		
		#file.write("\pool.add(u'C://Users//eP_Lab2//Desktop//baltiloka.jpg') \n")
		for imagePath in cols_image:
			file.write("\tpool.add(u'"+carpeta_proyecto+"/library/"+imagePath+"'"+") \n")
		
		# get the sound to add pool data
		for soundPath in cols_sound:
			file.write("\tpool.add(u'"+carpeta_proyecto+"/library/"+soundPath+"'"+") \n")

		
		file.write("\t __end__ \n")
		
		file.write("\t___run__\n")
		file.write("\t#inicializar variables\n")
		file.write("\tfrom openexp.keyboard import keyboard\n")
		file.write("\tfrom openexp.canvas import canvas\n")
		file.write("\timport time\n")
		file.write("\timport math\n")
		file.write("\tglobal my_keyboard,my_canvas\n")
		file.write("\tmy_keyboard = keyboard(exp,timeout = 0)\n")
		file.write("\tsubject_nr = exp.get('subject_nr')\n")
		file.write("\tmy_canvas=canvas(exp)\n")# set run part
		file.write("\tcanvas_blank=canvas(exp)\n")
		file.write("\tcalibration = 0\n")
		file.write("\trepeticion =[]\n")
		file.write("\texp.data  =[]\n")
		#file.write("\texp.data = [['session','item','cond','img_1','img_2','img_3','img_4','crit','sonido','sent_dur','sent_onset','display_onset','display_offset','post_view','repeticion','orden fijacion','comienzo fijacion','termino fijacion','tiempo fijacion','area de interes']]\n")
		file.write("\tmx = my_canvas.xcenter()\n")
		file.write("\tmy = my_canvas.ycenter()\n")
		
		file.write("\tfilename=self.get('logfile') \n")
		file.write("\tarrayPath=filename.split('.')\n")
		file.write("\tdirFinal=arrayPath[0]+'.tsv' \n")
		file.write("\toutputFinal=arrayPath[0]+'.txt'\n")
		
		file.write("\tfd = open(outputFinal,'w')\n")
				
		file.write("\t __end__ \n")
	    
		file.write("\n")
		
		
		# crear funcion que comprueba estado de calibracion en cada trial
		file.write("define inline_script test_calibracion \n")
		file.write("\tset flush_keyboard 'yes' \n")
		file.write("\tset description 'test de calibracion' \n")
		file.write("\t___run__\n")
		file.write("\timport time\n")
		file.write("\timport math\n")
		file.write("\tdot_canvas=canvas(exp)\n")
		file.write("\ttimeout_start = time.time()\n")
		file.write("\ttimeout =time.time() + 1*5   # 5 segundos from now\n")
		file.write("\tglobal response_calibration\n")
		file.write("\tresponse_calibration=False\n")
		file.write("\twhile time.time() < timeout_start + timeout:\n")
		
		file.write("\t\ttime.sleep(1)\n")
		file.write("\t\tdot_canvas.fixdot(mx,my,color='green')\n")
		file.write("\t\tx, y = exp.pygaze_eyetracker.sample()\n")
		#file.write("\t\tdot_canvas.fixdot(x, y)\n")
		file.write("\t\tdistancia=int(math.sqrt((x-mx)**2 + (y-my)**2))\n")
		#file.write("\t\tdot_canvas.text('distancia<b>'+str(distancia)+'</b> ', x=mx,y=my-100,color='black')\n")
		file.write("\t\tdot_canvas.show()\n")
		file.write("\n")
		
		file.write("\t\tif distancia <=50:\n")
		#file.write("\t\t\ttimestamp, startpos = self.experiment.pygaze_eyetracker.wait_for_fixation_start()\n")
		#file.write("\t\t\tdot_canvas.fixdot(startpos[0],startpos[1],color='blue')\n")
		file.write("\t\t\tdot_canvas.show()\n")
		file.write("\t\t\tcalibration=True\n")
		file.write("\t\t\tbreak\n")
		
		file.write("\t\tif time.time() > timeout:\n")
		file.write("\t\t\tif calibration==False:\n")
		file.write("\t\t\t\twhile(response_calibration==False):\n")
		file.write("\t\t\t\t\tresponse_calibration=exp.pygaze_eyetracker.calibrate()\n")
		file.write("\t\t\t\tif response_calibration==True:\n")
		file.write("\t\t\t\t\tcalibration=True\n")
					
		file.write("\t\t\tbreak\n")
		
		file.write("\t\tdot_canvas.clear()\n")	
		
		file.write("\tcalibration=False\n")
		file.write("\tself.sleep(1000)\n")
		
		file.write("\t __end__ \n")
		file.write("\t___prepare__\n")
		file.write("\t#Obtenemos el tamaño de la pantalla\n")
		
		file.write("\t#definimos listas para almacenar los datos\n")
		file.write("\txList, yList, tList , imgList, repList = [], [], [], [], []\n")
		file.write("\t __end__ \n")
		
		
		##### create sequence del trial
		
		file.write("define sequence trial_sequence \n")
		file.write("\tset flush_keyboard 'yes' \n")
		file.write("\tset description 'trial of sequence' \n")
		
		file.write("\t run test_calibracion\n")
		file.write("\t run load_trial\n")
		
		
		file.write("define inline_script load_trial \n")# codigo en python inline_script TO add many sequences
		file.write("\t set description 'crear many trial' \n")# crear trial
		
		
		file.write("\t___prepare__\n")
		file.write("\timport threading\n")# librerias hilos
		file.write("\tfrom PIL import Image\n")#libreria para manipular imagenes
		file.write("\tsound_trial=self.get('sound')\n") #cargar sonido del pool
		file.write("\tsonido = exp.pool[sound_trial]\n")#cargar el sonido al trial
		file.write("\taudio=sampler(sonido, volume=0.5)\n")
		
		file.write("\n")
		#file.write("\timg_1=self.get('img_1')\n")
		#file.write("\timagen_1 = pool[img_1]\n")
		#file.write("\tim = Image.open(imagen_1)\n")
		#file.write("\twidth1, height1 = im.size\n")
		#file.write("\tscale_factor_1=200/float(width1)\n")
		#file.write("\tim.close()\n")
		
		file.write("\tcount=self.get('count_trial_sequence')\n")#contador de vueltas de el loop
		file.write("\tvector_img1=[]\n")
		file.write("\tvector_img2=[]\n")
		file.write("\tvector_img3=[]\n")
		file.write("\tvector_img4=[]\n")
		
		
		file.write("\tglobal image_size\n")
		file.write("\timage_size=200\n")#size de la imagen
		
		#imagen 2 escalado y add a trial
		count_image=4
		#QMessageBox.information(w, "Message", str(count_image))
		i=1
		while i<=count_image:
			#file.write("\t#scale to image before add in trial\n")
			file.write("\timg_"+str(i)+"=self.get('img_"+str(i)+"')\n")
			file.write("\timagen_"+str(i)+"= pool[img_"+str(i)+"]\n")
		
			#file.write("\t#cargar imagen \n")
			file.write("\tim = Image.open(imagen_"+str(i)+")\n")
			file.write("\twidth"+str(i)+", height"+str(i)+" = im.size\n")
			file.write("\timg_"+str(i)+"X=self.get('X_img_"+str(i)+"')\n")	#get x de cada imagen desde excel\n")
			file.write("\timg_"+str(i)+"Y=self.get('Y_img_"+str(i)+"')\n")	#get Y de cada imagen desde excel\n")
			file.write("\tscale_img_"+str(i)+"=self.get('scale_img_"+str(i)+"')\n")	#get Y de cada imagen desde excel\n")
			
			file.write("\tim.close()\n")
			#file.write("\n")
			i=i+1
		#file.write("\tmy_canvas.clear()\n")
		file.write("\tmy_canvas.image(imagen_1,False,img_1X,img_1Y,scale_img_1)\n")
		file.write("\tvector_img1.append([img_1X,img_1Y,img_1])\n")
		file.write("\tmy_canvas.image(imagen_2,False,img_2X,img_2Y,scale_img_2)\n")			
		file.write("\tvector_img2.append([img_2X,img_2Y,img_2])\n")	
		file.write("\tmy_canvas.image(imagen_3,False,img_3X,img_3Y,scale_img_3)\n")
		file.write("\tvector_img3.append([img_3X,img_3Y,img_3])\n")
		file.write("\tmy_canvas.image(imagen_4,False,img_4X,img_4Y,scale_img_4)\n")
		file.write("\tvector_img4.append([img_4X,img_4Y,img_4])\n")
		######
		


		file.write("\titem=self.get('item')\n")
		file.write("\tcond=self.get('cond')\n")
		file.write("\tcrit_obj=self.get('crit')\n")
		
		
		file.write("\tsent_dur=self.get('sent_dur')\n")
		file.write("\tsent_onset=self.get('sent_onset')\n")
		file.write("\tdisplay_onset=self.get('display_onset')\n")
		file.write("\tdisplay_offset=self.get('display_offset')\n")
		file.write("\tpost_view=self.get('post_view')\n")
		file.write("\tdef sonido(sent_dur,sent_onset,audio):\n")#check
		file.write("\t\tself.sleep(sent_onset)\n")
		file.write("\t\tprint 'comienza audio'\n")
		
		file.write("\t\tvector_salida.append(self.time())#start audio\n")
		
		file.write("\t\taudio.play()\n")
		file.write("\t\tself.sleep(sent_dur)\n")
		file.write("\t\tvector_salida.append(self.time())#end audio\n")
		file.write("\n")
		file.write("\tcanvas_blank.clear(color='white')\n")
		file.write("\tcanvas_blank.show()\n")
		file.write("\t __end__ \n")
	

		file.write("\t___run__\n")
		
		
	
		
		
		file.write("\tsonido = threading.Thread(target=sonido, name='sonido',args=(sent_dur,sent_onset,audio))\n")
		
		file.write("\tcount2=0\n")
		file.write("\tduration = display_offset\n")
		file.write("\tvector_salida=[]\n")
		######################################
		file.write("\tvector_salida.append(subject_nr)\n")
		file.write("\tvector_salida.append(item)\n")
		file.write("\tvector_salida.append(cond)\n")
		file.write("\tvector_salida.append(img_1)\n")
		file.write("\tvector_salida.append(img_2)\n")
		file.write("\tvector_salida.append(img_3)\n")
		file.write("\tvector_salida.append(img_4)\n")
		file.write("\tvector_salida.append(crit_obj)\n")		
		file.write("\tvector_salida.append(sound_trial)\n")			
		file.write("\tvector_salida.append(sent_dur)\n")				
		file.write("\tvector_salida.append(sent_onset)\n")		
		file.write("\tvector_salida.append(display_onset)\n")	
		file.write("\tvector_salida.append(display_offset)\n")			
		file.write("\tvector_salida.append(post_view)\n")		
		file.write("\tvector_salida.append(count+1)\n")		
		file.write("\tsonido.start()\n")
		file.write("\tt0=my_canvas.show()\n")
		file.write("\tstartsample=t0\n")
		file.write("\n")
		
		file.write("\t#black screen")
		
		
		#file.write("\tself.sleep(display_onset)\n")
		#file.write("\n")
		
		#file.write("\tstart =int(round(time.time() * 1000))\n")
		#file.write("\tw,z=0,0 #variables auxiliares de sampleo tracker\n")
		#file.write("\tenable_fijacion=False #flag de fijacion\n")
		
		#file.write("\tcontador_fijacion=0\n")
		#file.write("\tfijacion_time=0\n")
		file.write("\tarea_de_interes=-1\n")
		
		file.write("\twhile(self.time() - t0 < duration+post_view):	\n")
		
		#file.write("\t\tself.sleep(17) #frames por milisegundo que puede getear el tracker \n")
		file.write("\t\tx, y = eyetracker.sample()\n")
		#file.write("\t\tnow = int(round(time.time() * 1000))\n")
		#file.write("\t\tcurrent_time=now-start\n")
		#file.write("\t\tx=math.ceil(x*100)/100\n")
		#file.write("\t\ty=math.ceil(y*100)/100\n")
		#file.write("\t\tx=int(round(x))\n")
		#file.write("\t\ty=int(round(y))\n")
		
		#file.write("\t#distancia entre dos puntos\n")
		#file.write("\t\tdistancia=int(math.sqrt((x-w)**2 + (y-z)**2))\n")
		#file.write("\t\tif distancia <=15:\n")
		#file.write("\t\t\tif enable_fijacion==False:\n")
		#file.write("\t\t\t\tif enable_fijacion==False:\n")
		
		#file.write("\t\t\t\tfijacion_time=0\n")
		
				
		
		
		
		
		
		
		
		
		#file.write("\t\t\t\tcontador_fijacion=contador_fijacion+1\n")
		#file.write("\t\t\t\tvector_salida.append(contador_fijacion)\n")
		#file.write("\t\t\t\tstart_timer=int(current_time)\n")
		
		
		#file.write("\t\t\t\tvector_salida.append(int(current_time))\n")
		#file.write("\n")
		
		#file.write("\t\t\t\t\tstart_fijacion =int(round(time.time() * 1000))\n")
		#file.write("\t\t\t\t\tmy_canvas.fixdot(x, y,'large-open',color='green')\n")
		#file.write("\t\t\t\tenable_fijacion=True\n")
		
		file.write("\t#validacion area de interes\n")
		
		file.write("\t\tif vector_img1[0][0]<x<vector_img1[0][0]+(width1*scale_img_1) and vector_img1[0][1]<y<vector_img1[0][1]+ (height1*scale_img_1):\n")
		file.write("\t\t\tarea_de_interes=1\n")
		
		file.write("\t\telif vector_img2[0][0]<x<vector_img2[0][0]+(width2*scale_img_2) and vector_img2[0][1]<y<vector_img2[0][1]+(height2*scale_img_2):\n")
		file.write("\t\t\tarea_de_interes=2\n")
		
		file.write("\t\telif vector_img3[0][0]<x<vector_img3[0][0]+(width3*scale_img_3) and vector_img3[0][1]<y<vector_img3[0][1]+(height3*scale_img_3):\n")
		file.write("\t\t\tarea_de_interes=3\n")
		
		file.write("\t\telif 	vector_img4[0][0]<x<vector_img4[0][0]+(width4*scale_img_4) and vector_img4[0][1]<y<vector_img4[0][1]+(height4*scale_img_4):\n")
		file.write("\t\t\tarea_de_interes=4\n")
		
		file.write("\t\telse:\n")
		file.write("\t\t\tarea_de_interes='.'\n")
		
		#file.write("\t\telse:\n")
		file.write("\t\tcount2=count2+1\n")
		
		file.write("\t\ttime_sample=self.time()\n")
		#file.write("\t\tsample=time_sample-startsample\n")
		
		
		file.write("\t\tfd.write('\\t'+str(count2)+'\\t'+str(x)+'\\t'+str(y)+'\\t'+str(int(time_sample))+'\\t'+str(area_de_interes)+'\\n')\n")
		
		#file.write("\t\tstartsample=time_sample\n")
		file.write("\t\ttime.sleep(0.017)\n")
		
		##########
		
		file.write("\tmy_canvas.clear()\n")
		file.write("\tt1=self.time()\n")
		file.write("\tvector_salida.append(t0)\n")
		file.write("\tvector_salida.append(t1)\n")
		
		#pic onset
		file.write("\tvector_salida.append(t0)#pic onset\n")
		#pics offset
		file.write("\tvector_salida.append(t1)#pics offset\n")
		
		file.write("\tprint 'trial_time '+str(t1-t0)\n")
		file.write("\tprint 'total_count '+str(count2)\n")
		file.write("\texp.data.append(vector_salida)	\n")
		
		#file.write("\t\t\t\ttermino_fij_time=int(current_time)\n")
		#file.write("\t\t\t\tfijacion_time=int(current_time)-start_timer\n")
		#file.write("\t\t\t\tvector_salida.append(int(current_time))\n")
		#file.write("\t\t\t\ttermino_fijacion = int(round(time.time() * 1000))\n")
		#file.write("\t\t\t\tfijacion_time=termino_fijacion-start_fijacion\n")
		#file.write("\t\t\t\tvector_salida.append(int(fijacion_time))\n")
		
		#file.write("\t\t\t\tenable_fijacion=False\n")
		#file.write("\t\t\t\tvector_salida.append(area_de_interes)\n")
		
		#file.write("\t\t\t\texp.data.append(vector_salida)\n")
		#file.write("\t\t\t\tvector_salida=[]\n")	
		
		#file.write("\t\t\tmy_canvas.fixdot(x, y)\n")
		#file.write("\t\tw=x\n")
		#file.write("\t\tz=y\n")
		
		#file.write("\t\tmy_canvas.show()\n")
		
		#file.write("\t\tif current_time>=display_offset:\n")
		#file.write("\t\t\tif enable_fijacion==True:\n")
		
		#file.write("\t\t\t\tfijacion_time=int(current_time)-start_timer\n")
		#file.write("\t\t\t\tvector_salida.append(int(current_time))\n")
		#file.write("\t\t\t\ttermino_fijacion = int(round(time.time() * 1000))\n")
		#file.write("\t\t\t\tfijacion_time=termino_fijacion-start_fijacion\n")
		#file.write("\t\t\t\tvector_salida.append(int(fijacion_time))\n")
		
		#file.write("\t\t\t\tenable_fijacion=False\n")
		#file.write("\t\t\t\tvector_salida.append(area_de_interes)\n")
		
		#file.write("\t\t\t\texp.data.append(vector_salida)\n")
		#file.write("\t\t\t\tvector_salida=[]\n")	
		#file.write("\t\t\tbreak\n")
		#file.write("\tprint exp.data\n")	
		#file.write("\tself.sleep(post_view)\n")
		file.write("\t __end__ \n")

		# funcion que crea el archivo csv de salida finally
		file.write("define inline_script save_data_cvs \n")
		file.write("\tset description 'guardar los datos en un file csv'\n")
		
		file.write("\t___run__ \n")
		file.write("\tfrom GetTrackerReportFromLog import DataFile \n")
		file.write("\tfd.close()\n")
		file.write("\tDataFile(200,200,outputFinal,exp.data).Generate()\n")
		#file.write("\twith open(filename, 'wb') as myfile: \n")
		#file.write("\t\twr = csv.writer(myfile, delimiter=',') \n")
		#file.write("\t\twr.writerows(exp.data) \n")
		
		file.write("\t __end__\n")
		QMessageBox.information(w, "Message", "datos cargados")
		
		
		
	
		
		file.close()	
				# Create and show a canvas with a central fixation dot
		