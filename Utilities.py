import xlrd
class Utilities(object):
  
  def __init__(self,codigo,ruta_excel):
	self.images_array=[]
	self.sound_array=[]
	self.token=codigo
	self.path=ruta_excel
	self.xl_workbook = xlrd.open_workbook(self.path)
	# List sheet names, and pull a sheet by name
	sheet_names = self.xl_workbook.sheet_names()
	self.xl_sheet = self.xl_workbook.sheet_by_name(sheet_names[0])
	self.num_cols = self.xl_sheet.ncols   # Number of columns
	
  def get_post_view(self, ind_row):
	cols_post_view=[]
	post_view_per_row=[]
	for row_idx in range(0, 1):
		for col_idx in range(0, self.num_cols):  # Iterate through columns
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			if cell_obj=='post_view': #selecionar las  cols con display_onset
				cols_post_view.append(col_idx)
	for row_idx in range(1, self.xl_sheet.nrows):
		for col_idx in range(0, self.num_cols):  # Iterate through columns}
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			for ind in cols_post_view:
				if col_idx==ind:# si es el sonido la guarda en el array
					post_view_per_row.append(cell_obj)
	return int(post_view_per_row[ind_row])					
  def get_display_onset(self,ind_row):
	cols_display_onset=[]
	display_onset_per_row=[]
	for row_idx in range(0, 1):
		for col_idx in range(0, self.num_cols):  # Iterate through columns
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			if cell_obj=='display_onset': #selecionar las  cols con display_onset
				cols_display_onset.append(col_idx)
	for row_idx in range(1, self.xl_sheet.nrows):
		for col_idx in range(0, self.num_cols):  # Iterate through columns}
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			for ind in cols_display_onset:
				if col_idx==ind:# si es el sonido la guarda en el array
					display_onset_per_row.append(cell_obj)
	return 	int(display_onset_per_row[ind_row])		
	
  def get_sound_dur(self, ind_row): # obtiene un vector de dur_sonido
	cols_sound=[]
	sound_per_row=[]
	for row_idx in range(0, 1):
		for col_idx in range(0, self.num_cols):  # Iterate through columns
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			if cell_obj=='sent_dur': #selecionar las  cols con sound duracion
				cols_sound.append(col_idx)
	for row_idx in range(1, self.xl_sheet.nrows):
		for col_idx in range(0, self.num_cols):  # Iterate through columns}
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			for ind in cols_sound:
				if col_idx==ind:# si es el sonido la guarda en el array
					sound_per_row.append(cell_obj)			
	return int(sound_per_row[ind_row])			
  def get_images_per_row(self,ind_row):
	return self.images_array[ind_row]
  def dist(x1,y1,x2,y2):
    # function to compute the Euclidian distance between two points
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  def get_images(self): #este metodo es para agregar las imagenes el pool de datos del proyecto
	images_per_row=[]	
	cols_images=[]
	images_path=[]	
	for row_idx in range(0, 1):
		for col_idx in range(0, self.num_cols):  # Iterate through columns
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			if cell_obj[0:3]=='img': #selecionar las  cols con img
				cols_images.append(col_idx)
	for row_idx in range(1, self.xl_sheet.nrows):
		for col_idx in range(0, self.num_cols):  # Iterate through columns}
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			for ind in cols_images:
				if col_idx==ind:# si es una imagen la guarda en el array
					images_path.append(cell_obj)
					images_per_row.append(cell_obj)
				
		self.images_array.append(images_per_row)
		images_per_row=[]	
						
	return images_path
  def scale_image(self,largo,ancho):
	print "scale_images",largo
  def get_sound(self):
	cols_sound=[]
	sound_path=[]
	for row_idx in range(0, 1):
		for col_idx in range(0, self.num_cols):  # Iterate through columns
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			if cell_obj=='sound': #selecionar las  cols con sound 
				cols_sound.append(col_idx)	
	for row_idx in range(1, self.xl_sheet.nrows):
		for col_idx in range(0, self.num_cols):  # Iterate through columns}
			cell_obj = self.xl_sheet.cell(row_idx, col_idx).value
			for ind in cols_sound:
				if col_idx==ind:# si es una sonido lo guarda en el array
					sound_path.append(cell_obj)	
	return sound_path	
	