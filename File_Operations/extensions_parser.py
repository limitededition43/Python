#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import csv
import json
import os

try:

    wb = xlrd.open_workbook(filename='ransomware.xlsx',
                            encoding_override='cp1251')
    sheet1 = wb.sheet_by_index(0)
    sheet2 = wb.sheet_by_index(1)
    sheet3 = wb.sheet_by_index(2)
    sheet4 = wb.sheet_by_index(3)
    Extension = dict()
    Path = os.getcwd()
    Filepath = Path+"/all_ext.txt"
    file = csv.reader(open(Filepath, 'rb'), delimiter='\t')
    Standardextensions = dict(file)
    rows = []


    def extension_check(ext):
        if Standardextensions.has_key(ext):
            return ['Y', Standardextensions[ext]]
        else:
            return ['N', '']


    def getransomware(ext):
        if ext in Extension:
            rans = list(Extension[ext].split()[0:1])
            return str(rans[0])


    def extractor(
        s1,
        s2,
        s3,
        s4,
        ):
        for (item, desc) in zip(s1.col_values(1), s1.col_values(2)):
            item = str(item.encode('utf-8'))[18:]
            desc = str(desc.encode('utf-8'))
            dict1 = dict({item: desc})
            Extension.update(dict1)

        for (item, desc) in zip(s2.col_values(1), s1.col_values(2)):
            item = str(item.encode('utf-8'))
            desc = str(desc.encode('utf-8'))
            Extension.update(dict({item: desc}))

        for i in range(s3.nrows):
            item = repr(s3.cell(i, 1).value)

            # item = (item).replace("u'*","")
            # item = (item).replace("u'","")
            # item = (item).replace("'","")

            item = str(item).rsplit('.', 1)[-1]
            item = str(item)[:-1]

            # item = item.replace("u'","")

            if item in Extension.keys():
                continue
            Extension.update(dict({item: 'Unidentified'}))

        for (item, desc) in zip(s4.col_values(1), s4.col_values(2)):
            item = str(item.encode('utf-8'))
        desc = str(desc.encode('utf-8'))
        Extension.update(dict({item: desc}))


    def csv_exporter(data):
        fields = ['File Extension', 'Ransomware',
                  'Present in other programs', 'Program type']
        rows = data
        with open('output.csv', mode='w') as file:
            o = csv.writer(file, delimiter=',')
            o.writerow(fields)
            o.writerows(data)


    def json_exporter(data):
        jsonString = json.dumps(data)
        with open('output.json', 'w') as jsonFile:
            jsonFile.write(jsonString)
            jsonFile.close()


    def main():
        extractor(sheet1, sheet2, sheet3, sheet4)
        for ext in Extension.keys():
            if len(Extension[ext]):
                rows.append([ext, getransomware(ext),
                            extension_check(ext)[0],
                            extension_check(ext)[1]])
	csv_exporter(rows)
	print("[+] File Successfully written to %soutput.csv" % Path)
        json_exporter(rows)
	print("[+] File Successfully writter to %soutput.json" % Path)

    main()

except IOError as e:
    print '[!]: Missing extension word list <all_ext.txt>',e

except Exception as e:
    print '[!]: Something went wrong .', e



