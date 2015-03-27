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
    print("전자명세서 첨부파일 목록")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" # 전자명세서 문서관리번호

    fileList = statementService.getFiles(testValue.testCorpNum,ItemCode,MgtKey)
    
    ''' attachedFile 구성: 
            attachedFile : #파일 삭제시에 활용되는 파일 ID
            regDT :    #등록일시 yyyyMMddHHmmss
            displayName : 표시명
            serialNum : 일련번호
    '''
    i = 1
    for f in fileList:
        print("%d:" % i)
        print("    serialNum : %s" % f.serialNum)
        print("    attachedFile : %s" % f.attachedFile)
        print("    displayName : %s" % f.displayName)
        print("    regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))