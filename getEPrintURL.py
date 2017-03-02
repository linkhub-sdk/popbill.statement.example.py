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
전자명세서 인쇄(공급받는자) URL을 반환합니다.
- 반환된 URL은 보안정책에 따라 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 전자명세서 공급받는자 인쇄 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20161123-01"

    url = statementService.getEPrintURL(CorpNum, ItemCode, MgtKey)
    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
