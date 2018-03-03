# coding=UTF-8
from ImportCSVFile import ImportCSVFile
from ExportCSVFile import ExportCSVFile

class Main(object):
	def RunImport(self, fileName):
		try:
			_importCSVFile = ImportCSVFile()
			_file = _importCSVFile.Run(fileName)
			return _file
		except Exception as ex:
			print 'An unexpected error occurred: ' + repr(ex)

	def RunExport(self, table, fileName):
		try:
			_exportCSVFile = ExportCSVFile()
			_exportCSVFile.Run(table, fileName)
		except Exception as ex:
			print 'An unexpected error occurred: ' + repr(ex)