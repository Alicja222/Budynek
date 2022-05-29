
def ile_osob(dl, szer, pietra):
    if isinstance(dl,(int,float)) and dl >= 1 and isinstance(szer,(int, float)) and szer >= 1 and isinstance(pietra,int) and pietra >= 1:
        return dl * szer * pietra
    elif dl == 0 or szer == 0 or pietra == 0:
        return 0
    else:
        return 'none'



def ile_ze_srodkami(ilosc_osob,srodki):
    if srodki == 'T':
        return int(ilosc_osob * 1.1)
    else:
        return ilosc_osob * 0.5