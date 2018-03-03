# coding=UTF-8
from Main import Main

main = Main()

tableExample = [['Nome', 'Idade', 'Nascimento'],['Jallysson', 25, 1992]]

file = main.RunImport('FileCSV')

main.RunExport(tableExample, 'FileCSV')