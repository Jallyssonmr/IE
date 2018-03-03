# coding=UTF-8
import csv

class ImportCSVFile(object):
    def Run(self, fileName):
        try:
            with open('Input/' + fileName + '.csv', 'rb') as csvfile: 
                _file = list(csv.reader(csvfile))
                return _file
        except IOError as (errno, strerror):
            print 'I/O error({0}): {1}'.format(errno, strerror)