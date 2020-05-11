#coding: utf-8
"""
Algumas funções para aritmética Dekatriana
Roberto "Pena" Spinelli - 11\10\\2017
dekatrian.com
"""
def Dek2week(dekDay, dekMonth, dekYear):
    """Encontra o dia da semana gregoriano a partir de uma data dekatriana.
    1 = domingo; 2 = segunda; 3 = terça ... 7 = sábado."""
    weekDay = ((WeekdayOnFirstAuroran(dekYear) + DekatrianWeek(dekDay, dekMonth) - 2) % 7) + 1
    if dekMonth == 0:
        weekDay = ((weekDay - 3 + dekDay) % 7) + 1
    return weekDay

def DekatrianWeek(dekDay, dekMonth):
    """Encontra o dia da semana dekatriano a partir de uma data dekatriana.
    A elegância do calendário aparece aqui, pois não é necessário passar o ano. Na verdade quase não é preciso passar o mês, ele só entra para checar se é o Achronian.
    0 = Achronian; 1 = primeiro dia da semana; 2 = segundo dia ... 7 = sétimo dia."""
    if dekMonth == 0:
        return 0
    else:
        dekWeekDay = ((dekDay-1) % 7) + 1
        return dekWeekDay
    
def WeekdayOnFirstAuroran(dekYear):
    """Calcula o dia da semana gregoriano para o 1 Auroran de um dado ano"""
    weekDay = ((1 + 5*((dekYear) % 4) + 4*((dekYear) % 100) + 6*((dekYear) % 400)) % 7) + 1
    return weekDay

def CheckLeapYear(dekYear):
    if (dekYear%4 == 0) and (dekYear%100 != 0 or dekYear%400 == 0):
        return 1
    else:
        return 0

def YearDayOnDekaDate(dekDay, dekMonth, dekYear):
    """Calcula qual o dia do ano de uma data Dekatrian.
    Achronian é o dia 1.
    Sinchronian é dia 2 quando houver."""
    if dekMonth == 0:
        return dekDay
    else:
        return (CheckLeapYear(dekYear)) + 1 +(dekMonth-1)*28 + dekDay

def YearDayOnGregDate(day, month, year):
    """Calcula qual o dia do ano de uma data Gregoriana.
    1 Jan é o dia 1.
    31 Dez é o dia 365 ou 366 se for bissexto"""
    Jan = 31
    Fev = 28 + CheckLeapYear(year)
    Mar = 31
    Apr = 30
    Mai = 31
    Jun = 30
    Jul = 31
    Ago = 31
    Set = 30
    Out = 31
    Nov = 30
    Dez = 31
    Meses = (Jan, Fev, Mar, Apr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez)
    i=0
    days = 0
    while i < (month-1):
        days += Meses[i]
        i += 1
    return days + day


def Dek2Greg(dekDay, dekMonth, dekYear):
    """Converte uma data Dekatrian para data Gregoriana"""
    YearDay = YearDayOnDekaDate(dekDay, dekMonth, dekYear)
    Jan = 31
    Fev = 28 + CheckLeapYear(dekYear)
    Mar = 31
    Apr = 30
    Mai = 31
    Jun = 30
    Jul = 31
    Ago = 31
    Set = 30
    Out = 31
    Nov = 30
    Dez = 31
    Meses = (Jan, Fev, Mar, Apr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez)
    for mes, dias in enumerate(Meses, start=1):
        if YearDay > dias:
            YearDay -= dias
        else:
            break
    return (YearDay, mes, dekYear)

def Greg2Dek(day, month, year):
    """Converte uma data Gregoriana para data Dekatrian"""
    YearDay = YearDayOnGregDate(day, month, year)
    LeapYear = CheckLeapYear(year)
    print YearDay
    if YearDay > (1 + LeapYear):
        YearDay -= 1 + LeapYear
        print YearDay
        dekMonth = int((YearDay-1) / 28) + 1
        dekDay = (YearDay-1) % 28 + 1
    else:
        dekMonth = 0
        dekDay = day
    return (dekDay, dekMonth, year)

### Exemplos ###
#print Dek2week(28, 13, 2015)
#print Dek2week(1, 0, 2016)
#print Dek2week(2, 0, 2016)
#print Dek2week(1, 1, 2016)
#print DekatrianWeek(1, 0)
#print WeekdayOnFirstAuroran(2016)
#print YearDayOnDekaDate(3, 1, 2017)
#print Dek2Greg(10, 10, 2017)
#print YearDayOnGregDate (29, 12, 2016)
#print Greg2Dek(3, 1, 2016)