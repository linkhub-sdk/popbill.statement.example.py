# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService, PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest

try:
    print("팝빌 URL 확인")

    TOGO = "CHRG" # LOGIN-팝빌 로그인, CHRG-포인트충전 
    url = statementService.getPopbillURL(testValue.testCorpNum,testValue.testUserID, TOGO)

    print("URL: %s" % url)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))