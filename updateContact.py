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

from popbill import ContactInfo, StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
연동회원 사업자번호에 등록된 담당자(팝빌 로그인 계정) 정보를 수정합니다.
- https://docs.popbill.com/statement/python/api#UpdateContact
'''

try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 담당자 정보
    updateInfo = ContactInfo(

        # 담당자 아이디
        id=UserID,

        # 담당자 성명 (최대 100자)
        personName="담당자 성명",

        # 연락처 (최대 20자)
        tel="",

        # 메일주소 (최대 100자)
        email="",

        #담당자 조회권한, 1(개인) 2(읽기) 3(회사)
        searchRole=1
    )

    result = statementService.updateContact(CorpNum, updateInfo)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
