# IE

:file_folder: Import and Export csv files

### First

Open the Run.py file.

### Second

#### Import file

Enter the file name ('FileCSV'):

```python
file = main.RunImport('FileCSV')
```

*Note*: no directory and extension.

#### Export file

Pass the table and name to save to file (tableExample, 'FileCSV'):

```python
tableExample = [['Nome', 'Idade', 'Nascimento'],['Jallysson', 25, 1992]]

main.RunExport(tableExample, 'FileCSV')
```

*Note*: no directory and extension

### Last

Run Run.py file :relieved::coffee:
