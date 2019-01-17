# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest

'''
1건의 [임시저장] 상태의 전자명세서를 발행처리합니다.
- 발행시 포인트가 차감됩니다.
'''

try:
    print("=" * 15 + " 전자명세서 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20190117-001"

    result = statementService.issue(CorpNum, ItemCode, MgtKey)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
