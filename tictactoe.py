#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Tic Tac Toe

import random

board =[ "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#3*3の盤面を作るよ。
def print_board(boardvalues):
    print
    print
    print " %s | %s  | %s" %(boardvalues[0], boardvalues[1], boardvalues[2])
    print "   |   |		"
    print('-----------')
    print "   |   |		"
    print " %s | %s  | %s" %(boardvalues[3], boardvalues[4], boardvalues[5])
    print "   |   |		"
    print('-----------')
    print "   |   |		"
    print " %s | %s  | %s" %(boardvalues[6], boardvalues[7], boardvalues[8])
    print "   |   |		"
    print
    print


def getplayerchoose(boardvalues):
	vChoice = False
	while (not vChoice):
		print_board(boardvalues)
		spaceChoice = int(raw_input("choose a space !")) -1 #０から８の範囲内を維持するため入力された数字からー１する。
	
		if (boardvalues[spaceChoice] != "x" and boardvalues[spaceChoice] != "o" ):
			boardvalues[spaceChoice] = "x"
			vChoice = True

	return checkForwin(boardvalues)


def chooseRandom(boardvalues):
	vChoice =False
	while (not vChoice):
		print_board(boardvalues)
		spaceChoice = random.randint(0, 8) #ランダムにスペースを選ぶ。
	
		if (boardvalues[spaceChoice] != "x" and boardvalues[spaceChoice] != "o" ):
			boardvalues[spaceChoice] = "o"
			vChoice = True

	return checkForwin(boardvalues)


def checkHorizonal(boardvalues):
	foundWin = False

	if (boardvalues[0] == boardvalues[1] == boardvalues[2] ): #横方向に３つ並んでいるかをチェック
		foundWin = True
	elif(boardvalues[3] ==boardvalues[4] == boardvalues[5]):
		foundWin = True
	elif(boardvalues[6] == boardvalues[7] == boardvalues[8]):
		foundWin = True
		
	return foundWin


def checkVertical(boardvalues):
	foundWin = False

	if (boardvalues[0] == boardvalues[3] == boardvalues[6] ): #縦方向に３つ並んでいるかをチェック
		foundWin = True
	elif(boardvalues[1] ==boardvalues[4] == boardvalues[7]):
		foundWin = True
	elif(boardvalues[2] == boardvalues[5] == boardvalues[8]):
		foundWin = True
		
	return foundWin


def checkDiaonal(boardvalues):
	foundWin = False

	if (boardvalues[0] == boardvalues[4] == boardvalues[8] ): #ななめ方向に３つ並んでいるかをチェック
		foundWin = True
	elif(boardvalues[2] ==boardvalues[4] == boardvalues[6]):
		foundWin = True
		
	return foundWin


def checkForwin(boardvalues):
	gameWin = False

	if (checkHorizonal(boardvalues) == True): #どちらが勝ったかを判断する
		gameWin = True
	elif (checkVertical(boardvalues) == True):
		gameWin =True
	elif (checkDiaonal(boardvalues) == True):
		gameWin = True

	return gameWin	

	print_board(board)

win = False
turn = 0

while (not win and turn < 9) :

	if turn % 2 == 0 :
		win = getplayerchoose(board)
	else :
		win = chooseRandom(board)
	turn = turn+1

print_board(board)
turn = turn -1

if (not win):
	print "This game in a tie"
elif (turn % 2 == 0):
	print "you win !"
else:
	print "you lose !"