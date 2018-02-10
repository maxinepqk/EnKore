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
    for i in range(len(src)):
        ch = src[i] 
        p = ENG_KEY.index(ch)
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
                    elif (nJong == 0 and p == 9):
                        nJong = 2   
                    elif (nJong == 3 and p == 12):
                        nJong = 4
                    elif (nJong == 3 and p == 18):
                        nJong = 5
                    elif (nJong == 7 and p == 0):
                        nJong = 8
                    elif (nJong == 7 and p == 6):
                        nJong = 9
                    elif (nJong == 7 and p == 7):
                        nJong = 10
                    elif (nJong == 7 and p == 9):
                        nJong = 11
                    elif (nJong == 7 and p == 16):
                        nJong = 12
                    elif (nJong == 7 and p == 17):
                        nJong = 13
                    elif (nJong == 7 and p == 18):
                        nJong = 14
                    elif (nJong == 16 and p == 9):
                        nJong = 17
                    else:
                        res += makeHangul(nCho,nJung,nJong)
                        nCho = CHO_DATA.index(KOR_KEY[p])
                        nJung = -1
                        nJong = -1



            else:
                if (nCho == -1):
                    if (nJong != -1):
                        res += JONG_DATA[nJong]
                        nJong = -1

                    nCho = CHO_DATA.index(KOR_KEY[p])
                elif (nCho == 0 and p == 9):
                    nCho = -1
                    nJong = 2
                elif (nCho == 2 and p == 12):
                    nCho = -1
                    nJong = 4
                elif (nCho == 2 and p == 18):
                    nCho = -1
                    nJong = 5
                elif (nCho == 5 and p == 0):
                    nCho = -1
                    nJong = 8
                elif (nCho == 5 and p == 6):
                    nCho = -1
                    nJong = 9
                elif (nCho == 5 and p == 7):
                    nCho = -1
                    nJong = 10
                elif (nCho == 5 and p == 9):
                    nCho = -1
                    nJong = 11
                elif (nCho == 5 and p == 16):
                    nCho = -1
                    nJong = 12
                elif (nCho == 5 and p == 17):
                    nCho = -1
                    nJong = 13
                elif (nCho == 5 and p == 18):
                    nCho = -1
                    nJong = 14
                elif (nCho == 7 and p == 9):
                    nCho = -1
                    nJong = 17
                else:
                    res += CHO_DATA[nCho]
                    nCho = CHO_DATA.index(KOR_KEY[p])
            

        else:
            if (nJong != -1):

                newCho;
                if (nJong ==2):
                    nJong = 0
                    newCho = 9
                elif(nJong == 4):
                    nJong = 3
                    newCho = 12
                elif(nJong == 5):
                    nJong = 3
                    newCho = 18
                elif(nJong == 8):
                    nJong = 7
                    newCho = 0
                elif(nJong == 9):
                    nJong = 7
                    newCho = 6
                elif(nJong == 10):
                    nJong = 7
                    newCho = 7
                elif(nJong == 11):
                    nJong = 7
                    newCho = 9
                elif(nJong == 12):
                    nJong = 7
                    newCho = 16
                elif(nJong == 13):
                    nJong = 7
                    newCho = 17
                elif(nJong == 14):
                    nJong = 7
                    newCho = 18
                elif(nJong == 17):
                    nJong = 16
                    newCho = 9
                else:
                    newCho = CHO_DATA.index(JONG_DATA[nJong])
                    nJong = -1

                if (nCho != -1):
                    res += makeHangul(nCho, nJung, nJong)
                else:
                    res += JONG_DATA[nJong]

                nCho = newCho
                nJung = -1
                nJong = -1

            if (nJung == -1):
                nJung = JUNG_DATA.index(KOR_KEY[p])
            elif (nJung == 8 and p == 19):
                nJung = 9;
            elif (nJung == 8 and p == 20):
                nJung = 10;
            elif (nJung == 8 and p == 32):
                nJung = 11;
            elif (nJung == 13 and p == 23):
                nJung = 14;
            elif (nJung == 13 and p == 24):
                nJung = 15;
            elif (nJung == 13 and p == 32):
                nJung = 16;
            elif (nJung == 18 and p == 32):
                nJung = 19;
            else:
                if (nCho != -1):
                    res += makeHangul(nCho, nJung, nJong)
                    nCho = -1
                else:
                    res += JUNG_DATA[nJung]
                nJung = -1
                res += KOR_KEY[p]





        if (nCho != -1):
            if (nJung != -1):
                res += makeHangul(nCho, nJung, nJong)
            else:
                res += CHO_DATA[nCho]
        else:
            if (nJung != -1):
                res += JUNG_DATA[nJung]
            else:
                if (nJong != -1):
                    res += JONG_DATA[nJong]

            i+=1

        return res; 









