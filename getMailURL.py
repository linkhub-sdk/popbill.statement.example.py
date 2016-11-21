# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService, PopbillException

statementService =  StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest

'''
공급받는자 메일링크 URL을 반환합니다.
- 메일링크 URL은 유효시간이 존재하지 않습니다.
'''

try:
    print("=" * 15 + " 전자명세서 메일 링크 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20161121-01"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    url = statementService.getMailURL(CorpNum, ItemCode, MgtKey, UserID)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
