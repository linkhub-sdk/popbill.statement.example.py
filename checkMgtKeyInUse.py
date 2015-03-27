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
    print("파트너 관리번호 사용여부 확인")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" # 전자명세서 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성

    bIsInUse = statementService.checkMgtKeyInUse(testValue.testCorpNum,ItemCode,MgtKey)
    print("사용여부 : %s" % "사용중" if bIsInUse else '미사용중')
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))