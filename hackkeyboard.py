ENG_KEY = "rRseEfaqQtTdwWczxvgkoiOjpuPhynbml"
KOR_KEY = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ"
CHO_DATA = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG_DATA = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG_DATA = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

def doConvert():
	return



def engTypeToKore(src):
	res = "";
	if (len(src) == 0):
		return res

	nCho = -1
	nJung = -1
	nJong = -1
	for (i in range(len(src))):
		ch = src[i]
    	p = ENG_KEY.index("ch")
    	if (p == -1): 
      		if (nCho != -1):
        		if (nJung != -1):
    				res += makeHangul(nCho, nJung, nJong)
    			else:
    				res += CHO_DATA[nCho]
    		else:
    			if (nJung != -1):
    				res += JUNG_DATA[nJung]
    			elif (nJong != -1):
    				res += JONG_DATA.charAt(nJong)

    		nCho = -1;
    		nJung = -1
    		nJong = -1
    		res += ch
    	elif (p<19):
    		if (nJung != -1):
    			if (nCho == -1):
    				res += JUNG_DATA[nJung]
    				nJung = -1
    				nCho = CHO_DATA.index(KOR_KEY[p])
    			else:
    				if (nJong == -1):
    					nJong = JONG_DATA.index(KOR_KEY[p])
    					if (nJong == -1):
    						res += makeHangul(nCho, nJung, nJong)
    						nCho = CHO_DATA.index(KOR_KEY[p])
    						nJung = -1
    				elif (nJong == 0 && p == 9):
			        	nJong = 2	
			      	elif (nJong == 3 && p == 12):
			            nJong = 4
			      	elif (nJong == 3 && p == 18):
			            nJong = 5
			        elif (nJong == 7 && p == 0):
			            nJong = 8
			      	elif (nJong == 7 && p == 6):
			            nJong = 9
			      	elif (nJong == 7 && p == 7):
			            nJong = 10
			      	elif (nJong == 7 && p == 9):
			            nJong = 11
			      	elif (nJong == 7 && p == 16):
			        	nJong = 12
			      	elif (nJong == 7 && p == 17):
			            nJong = 13
			      	elif (nJong == 7 && p == 18):
			            nJong = 14
			      	elif (nJong == 16 && p == 9):
			            nJong = 17
			      	else:
				    



