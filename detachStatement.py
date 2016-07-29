# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService,PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest

try:
    print( "=" * 15 + " 다른전자명세서 첨부 " + "=" * 15)

    ItemCode = "121"          # 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    MgtKey = "r7aobdc60n"     # 전자명세서 문서관리번호
    SubItemCode = "121"       # 첨부할 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    SubMgtKey = "fbrdavxpsn"  # 첨부할 전자명세서 문서관리번호

    result = statementService.detachStatement(testValue.testCorpNum, ItemCode, MgtKey, SubItemCode, SubMgtKey, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
