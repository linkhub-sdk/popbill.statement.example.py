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
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
파트너가 전자명세서 관리 목적으로 할당하는 문서번호의 사용여부를 확인합니다.
- 이미 사용 중인 문서번호는 중복 사용이 불가하고, 전자명세서가 삭제된 경우에만 문서번호의 재사용이 가능합니다.
- https://docs.popbill.com/statement/python/api#CheckMgtKeyInUse
'''

try:
    print("=" * 15 + " 문서번호 사용여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 발신자별 고유번호 생성
    MgtKey = "20220803-001"

    bIsInUse = statementService.checkMgtKeyInUse(CorpNum, ItemCode, MgtKey)
    print("사용여부 : 사용중" if bIsInUse else "사용여부 : 미사용중")
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
