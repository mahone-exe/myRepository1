# -*- coding: UTF-8 -*-
import xlrd
import sys
import json


def readExcelToJosn(fileName):
	importData = {}

	workbook = xlrd.open_workbook(fileName)
	sheets = workbook.sheets()
	for sheet in sheets:

		for row in xrange(2,  sheet.nrows):
			heroName = sheet.cell_value(row, 0)
			importData[heroName] = {}
			#lift
			posx = sheet.cell_value(row, 1)
			posy = sheet.cell_value(row, 2)
			importData[heroName]["1"] = [posx, posy]
			#middle
			posx = sheet.cell_value(row, 3)
			posy = sheet.cell_value(row, 4)
			importData[heroName]["2"] = [posx, posy]
			#right
			posx = sheet.cell_value(row, 5)
			posy = sheet.cell_value(row, 6)
			importData[heroName]["3"] = [posx, posy]
			#gaching
			posx = sheet.cell_value(row, 9)
			posy = sheet.cell_value(row, 10)
			importData[heroName]["4"] = [posx, posy]

			scale3Door = sheet.cell_value(row, 7)
			scaleSelected = sheet.cell_value(row, 11)
			importData[heroName]["5"] = [scaleSelected, scale3Door]

	print importData
	return importData


def writeJsonToFiles(res):
		
	fileHandle = file("vipGachaPos.json",'w')
	jsonData = json.dumps(res)
	fileHandle.write(jsonData)
	fileHandle.close()


if __name__ == "__main__":
	fileName = sys.argv[1]
	print fileName

	cellData = readExcelToJosn(fileName)

	writeJsonToFiles(cellData)
