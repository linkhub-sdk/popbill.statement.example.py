# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP

'''
다수건의 전자명세서 인쇄팝업 URL을 반환합니다.
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
- https://docs.popbill.com/statement/python/api#GetMassPrintURL
'''

try:
    print("=" * 15 + " 전자명세서 대량 인쇄 팝업 URL (최대 100건) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 인쇄할 문서번호 배열, 최대 100건
    MgtKeyList = []
    MgtKeyList.append("20190117-001")
    MgtKeyList.append("20190117-002")
    MgtKeyList.append("20190117-003")

    url = statementService.getMassPrintURL(CorpNum, ItemCode, MgtKeyList)
    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
