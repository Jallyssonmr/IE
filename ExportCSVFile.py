# coding=UTF-8
import os
import csv

class ExportCSVFile(object):
	def Run(self, table, fileName):
		try:
			if not os.path.exists('Output/'):
				os.makedirs('Output/')
			file = csv.writer(open('Output/' + fileName + '.csv',"wb"))
			for line in table:
				file.writerow(line)
		except IOError as (errno, strerror):
			print 'I/O error({0}): {1}'.format(errno, strerror)