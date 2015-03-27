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
    print("전자명세서 처리이력 목록")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" # 전자명세서 문서관리번호
   
    LogList = statementService.getLogs(testValue.testCorpNum,ItemCode,MgtKey)

    ''' StatementLog 구성: 
            docLogType : 이력유형
            log : 문서이력 설명
            procType : 처리유형
            procCorpName : 처리회사명
            procMemo : 처리시 메모
            regDT : 처리일시
    '''
    i = 1
    for f in LogList:
        print("%d:" % i)
        print("    docLogType : %s" % f.docLogType)
        print("    log : %s" % f.log)
        print("    procType : %s" % f.procType)
        print("    procCorpName : %s" % f.procCorpName)
        print("    procMemo : %s" % f.procMemo)
        print("    regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))