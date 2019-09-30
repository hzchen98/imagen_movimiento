# -*- coding: utf-8 -*-
import os

def recent_file(directorio):
	files = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio,f))]
	creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
	return files[creates_dates.index(max(creates_dates))]
print(recent_file("D:/python_proyects"))