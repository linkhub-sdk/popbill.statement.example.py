# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import PopbillException, StatementService

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
1건의 전자명세서 상태/요약 정보를 확인합니다.
- https://developers.popbill.com/reference/statement/python/api/info#GetInfo
"""

try:
    print("=" * 15 + " 전자명세서 상태/요약 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서번호
    MgtKey = "20220803-001"

    statementInfo = statementService.getInfo(CorpNum, ItemCode, MgtKey)

    print("itemCode (문서종류코드): %s" % statementInfo.itemCode)
    print("itemKey (팝빌번호): %s" % statementInfo.itemKey)
    print("invoiceNum (팝빌승인번호): %s" % statementInfo.invoiceNum)
    print("mgtKey (문서번호): %s" % statementInfo.mgtKey)
    print("taxType (세금형태): %s" % statementInfo.taxType)
    print("writeDate (작성일자): %s" % statementInfo.writeDate)
    print("regDT (임시저장일시): %s" % statementInfo.regDT)
    print("senderCorpName (발신자 상호): %s" % statementInfo.senderCorpName)
    print("senderCorpNum (발신자 사업자등록번호): %s" % statementInfo.senderCorpNum)
    print("senderPrintYN (발신자 인쇄여부): %s" % statementInfo.senderPrintYN)
    print("receiverCorpName (수신자 상호): %s" % statementInfo.receiverCorpName)
    print("receiverCorpNum (수신자 사업자등록번호): %s" % statementInfo.receiverCorpNum)
    print("receiverPrintYN (수신자 인쇄여부): %s" % statementInfo.receiverPrintYN)
    print("supplyCostTotal (공급가액 합계): %s" % statementInfo.supplyCostTotal)
    print("taxTotal (세액 합계): %s" % statementInfo.taxTotal)
    print("purposeType (영수/청구): %s" % statementInfo.purposeType)
    print("issueDT (발행일시): %s" % statementInfo.issueDT)
    print("stateCode (상태코드): %s" % statementInfo.stateCode)
    print("stateDT (상태 변경일시): %s" % statementInfo.stateDT)
    print("stateMemo (상태메모): %s" % statementInfo.stateMemo)
    print("openYN (개봉 여부): %s" % statementInfo.openYN)
    print("openDT (개봉 일시): %s" % statementInfo.openDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
