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
    print("전자명세서 발행 단가 확인")

    ItemCode = 121  # 명세서 코드 [121-거래명세서], [122-청구서], [123-견적서], [124-발주서], [125-입금표], [126-영수증]
    
    unitCost = statementService.getUnitCost(testValue.testCorpNum, ItemCode)

    print("단가: %f" % unitCost)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))