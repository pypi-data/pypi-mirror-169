#! /usr/bin/python
# -*-coding:utf-8-*-

import sys
import requests
import time
import datetime
import os
from chinese_calendar import is_holiday, is_workday

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def setEncodingToUtf8():
    '''
    python default encoding is ASCII.
    for url date error 'ascii' codec can't decode byte 0xe4 in position 4: ordinal not in range(128)
    '''
    defaultencoding = 'utf-8'
    if sys.getdefaultencoding() != defaultencoding:
        reload(sys)
        sys.setdefaultencoding(defaultencoding)
    return

class DateTime(object):
    def __init__(self):
        '''
        Process workday and holiday.
        Process common string.
        '''
        pass
    
    def getTodayWeekday(self):
        weekday = datetime.datetime.now().weekday()
        sWeekday = ''
        if weekday == 6:
            sWeekday = '星期日'
        elif weekday == 5:
            sWeekday = '星期六'
        elif weekday == 4:
            sWeekday = '星期五'
        elif weekday == 3:
            sWeekday = '星期四'
        elif weekday == 2:
            sWeekday = '星期三'
        elif weekday == 1:
            sWeekday = '星期二'
        elif weekday == 0:
            sWeekday = '星期一'
        else:
            sWeekday = ''
        return sWeekday

    def getTodaydate(self):
        return str(datetime.date.today())

    def getYesterday(self): 
        today=datetime.date.today()
        oneday=datetime.timedelta(days=1)
        
        #today = datetime.date(2022, 5, 1)
        yesterday=today-oneday
        return yesterday
        
    #return bool of today if it is a workday.
    def isWorkday(self):
        today=datetime.date.today()
        
        #today = datetime.date(2022, 5, 1)
        if self.isAWorkDay(today):
            return True
        else:
            return False

    #return bool of today if it is a workday or last day is a workday.
    def isWorkdayOrLastdayIsWorkday(self):
        today=datetime.date.today()
        
        #today = datetime.date(2022, 5, 1)
        if self.isAWorkDay(today) or self.isAWorkDay(self.getYesterday()):
            return True
        else:
            return False

    def isAWorkDay(self,StandardDay):
        try:
            if is_workday(StandardDay):
                return True
            else:
                return False
        except NotImplementedError:
            return True
      
    def getLastWorkdayOfMonth(self):
        today=datetime.date.today()
        monthHave31Days = [1,3,5,7,8,10,12]
       
        if today.month in monthHave31Days:
            lastDay = 31
        else:
            lastDay = 30
        
        if today.year%4 == 0:
            lastDayFeb = 29
        else:
            lastDayFeb = 28

        if today.month == 2:
            lastDate = datetime.date(today.year, today.month, lastDayFeb)
        else:
            lastDate = datetime.date(today.year, today.month, lastDay)
        
        oneday=datetime.timedelta(days=1)
        while True:
            if self.isAWorkDay(lastDate):
                break
            lastDate=lastDate-oneday
        
        return lastDate 
        
    def isLastWorkdayOfAMonth(self):
        today=datetime.date.today()

        lastWorkDate = self.getLastWorkdayOfMonth()
        
        if today == lastWorkDate:
            return True
        else:
            return False
     
    def isHolidaysComing(self):
        #today = datetime.date(2022, 6, 1)
        oneday=datetime.timedelta(days=1)
        
        today=datetime.date.today()
        
        if not self.isAWorkDay(today + oneday):
            if not self.isAWorkDay(today + oneday + oneday):
                if not self.isAWorkDay(today + oneday + oneday + oneday):
                    return True
        return False
       
    def getLastWorkdate(self):
        today=datetime.date.today()
        oneday=datetime.timedelta(days=1)
        
        #today = datetime.date(2022, 5, 4)
        LastWorkdate=today-oneday
        while True:
            if self.isAWorkDay(LastWorkdate):
                break
            LastWorkdate=LastWorkdate-oneday
        return LastWorkdate
        
    def getLastWorkWeekday(self):
        weekday = self.getLastWorkdate().weekday()
        sWeekday = ''
        if weekday == 6:
            sWeekday = '星期日'
        elif weekday == 5:
            sWeekday = '星期六'
        elif weekday == 4:
            sWeekday = '星期五'
        elif weekday == 3:
            sWeekday = '星期四'
        elif weekday == 2:
            sWeekday = '星期三'
        elif weekday == 1:
            sWeekday = '星期二'
        elif weekday == 0:
            sWeekday = '星期一'
        else:
            sWeekday = ''
        return sWeekday

class LocalFile(object):
    def __init__(self):
        '''
        Local file auto process, useful common functions..
        '''
        pass

def getModifiedTime(self, fileName):
    '''
    return a fileName's modify time in struct_time format
    '''
    if os.path.exists(fileName):
        local_time = time.localtime(os.path.getmtime(fileName))
    return local_time

def isModifiedOnToday(self, fileName):
    '''
    return bool Ture if file modified on today.
    '''
    today = datetime.date.today()
    modifyDay = self.getModifiedTime(fileName)

    if today.year == modifyDay.tm_year:
        if today.month == modifyDay.tm_mon:
            if today.day == modifyDay.tm_mday:
                return True
    return False