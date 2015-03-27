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
    print("전자명세서 첨부파일 삭제")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" # 전자명세서 문서관리번호
    FileID = "E9DCCC9B-6DA8-4F48-8698-A1DFBCAD85D2.PBF"  # 삭제할 FileID, 첨부파일목록(getFiles API) 응답 전문의 attachedFile 값
    UserID = testValue.testUserID # 팝빌회원 아이디

    result = statementService.deleteFile(testValue.testCorpNum,ItemCode,MgtKey,FileID,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))