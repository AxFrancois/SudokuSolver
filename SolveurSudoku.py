# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:44:44 2021

@author: Axel François
"""

from math import floor

def getCol(pGrid,pColumn):
    listToSum = []
    for line in pGrid:
        listToSum.append(line[pColumn])
    return listToSum

def getSquare(pGrid,pRow,pColumn):
    SquareRow = int(floor(pRow/3))
    SquareColumn = int(floor(pColumn/3))
    listToSum = []
    for line in pGrid[SquareRow*3:SquareRow*3+3]:
          listToSum = listToSum + line[SquareColumn*3:SquareColumn*3+3]
    return listToSum

def fLineVerif(pLine):
    PossibleNumber = [1,2,3,4,5,6,7,8,9]
    for element in pLine:
        if element in PossibleNumber:
            PossibleNumber.remove(element)
    if len(PossibleNumber) == 1:
        Valren = PossibleNumber[0]
    else:
        Valren = 0
    return Valren

def fColVerif(pGrid,pColumn):
    PossibleNumber = [1,2,3,4,5,6,7,8,9]
    for element in getCol(pGrid,pColumn):
        if element in PossibleNumber:
            PossibleNumber.remove(element)
    if len(PossibleNumber) == 1:
        Valren = PossibleNumber[0]
    else:
        Valren = 0
    return Valren

def fSquareVerif(pGrid,pRow,pColumn):
    PossibleNumber = [1,2,3,4,5,6,7,8,9]
    for element in getSquare(pGrid,pRow,pColumn):
        if element in PossibleNumber:
            PossibleNumber.remove(element)
    if len(PossibleNumber) == 1:
        Valren = PossibleNumber[0]
    else:
        Valren = 0
    return Valren
def fCrossingVerif(pGrid,pRow,pColumn):
    PossibleNumber = [1,2,3,4,5,6,7,8,9]
    SquareRow = int(floor(pRow/3))
    SquareColumn = int(floor(pColumn/3))

    listColumn = getCol(pGrid,pColumn)
    listRow = pGrid[pRow]
    listSquare = getSquare(pGrid,pRow,pColumn)
    listAlreadyIn = listColumn + listRow + listSquare
    listAlreadyIn = [i for i in  listAlreadyIn if i != 0]

    for element in listAlreadyIn:
        if element in PossibleNumber:
            PossibleNumber.remove(element)

    if len(PossibleNumber) == 1:
        Valren = PossibleNumber[0]
    else: 
        RowToCheck = [i for i in range(SquareRow*3,SquareRow*3+3)]
        RowToCheck.remove(pRow)
        ColumnToCheck = [i for i in range(SquareColumn*3,SquareColumn*3+3)]
        ColumnToCheck.remove(pColumn)
        FirstRow = pGrid[RowToCheck[0]]
        SecondRow = pGrid[RowToCheck[1]]
        FirstColumn = getCol(pGrid,ColumnToCheck[0])
        SecondColumn = getCol(pGrid,ColumnToCheck[1])
        Valren = 0
        for value in PossibleNumber:
            #print(value)
            SquareState = []
            for element in listSquare:
                SquareState.append(element)
            if value in FirstRow:
                SquareState[RowToCheck[0]%3*3:RowToCheck[0]%3*3+3] = [value for i in range(3)]
            if value in SecondRow:
                SquareState[RowToCheck[1]%3*3:RowToCheck[1]%3*3+3] = [value for i in range(3)]
            if value in FirstColumn:
                index = ColumnToCheck[0]%3
                SquareState[index] = value
                SquareState[index+3] = value
                SquareState[index+6] = value
            if value in SecondColumn:
                index = ColumnToCheck[1]%3
                SquareState[index] = value
                SquareState[index+3] = value
                SquareState[index+6] = value      

            if 0 in SquareState:
                SquareState.remove(0)
                if 0 not in SquareState:
                    Valren = value
                    break
    return Valren  

Grid = [
[0,0,0,0,2,7,0,0,4],
[6,9,4,8,0,3,0,0,0],
[0,0,0,0,0,0,6,0,0],
[2,0,1,3,0,9,0,4,0],
[0,0,0,0,7,0,0,0,2],
[7,0,0,0,0,0,1,9,0],
[0,0,6,0,5,1,0,7,8],
[0,5,0,7,0,0,0,0,0],
[0,4,0,9,8,0,0,6,0]]

HasZero = True
Security = 0
while HasZero == True and Security < 100:
    HasZero = False
    Security += 1
    for row,line in enumerate(Grid):
        for column,number in enumerate(line):
            if number == 0:
                HasZero = True
                a = fLineVerif(line)
                b = fColVerif(Grid,column)
                c = fSquareVerif(Grid, row, column)
                d = fCrossingVerif(Grid, row, column)
                resultList = [a,b,c,d]
                for element in resultList:
                    if element != 0:
                        Grid[row][column] = element
print(Security)
print(Grid)