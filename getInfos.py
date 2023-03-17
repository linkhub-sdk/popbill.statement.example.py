# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import StatementService, PopbillException

statementService = StatementService(testValue.LinkID, testValue.SecretKey)
statementService.IsTest = testValue.IsTest
statementService.IPRestrictOnOff = testValue.IPRestrictOnOff
statementService.UseStaticIP = testValue.UseStaticIP
statementService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
다수건의 전자명세서 상태 및 요약정보 확인합니다. (1회 호출 시 최대 1,000건 확인 가능)
- https://developers.popbill.com/reference/statement/python/api/info#GetInfos
"""

try:
    print("=" * 15 + " 전자명세서 상태/요약 정보 확인 (대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 문서번호 배열, 최대 1000건
    MgtKeyList = []
    MgtKeyList.append("20220803-001")
    MgtKeyList.append("20220803-002")
    MgtKeyList.append("20220803-003")

    InfoList = statementService.getInfos(CorpNum, ItemCode, MgtKeyList)

    for info in InfoList:
        print("itemCode (문서종류코드): %s" % info.itemCode)
        print("itemKey (팝빌번호): %s" % info.itemKey)
        print("invoiceNum (팝빌승인번호)): %s" % info.invoiceNum)
        print("mgtKey (문서번호): %s" % info.mgtKey)
        print("taxType (세금형태): %s" % info.taxType)
        print("writeDate (작성일자): %s" % info.writeDate)
        print("regDT (임시저장일시): %s" % info.regDT)
        print("senderCorpName (발신자 상호): %s" % info.senderCorpName)
        print("senderCorpNum (발신자 사업자등록번호): %s" % info.senderCorpNum)
        print("senderPrintYN (발신자 인쇄여부): %s" % info.senderPrintYN)
        print("receiverCorpName (수신자 상호): %s" % info.receiverCorpName)
        print("receiverCorpNum (수신자 사업자등록번호): %s" % info.receiverCorpNum)
        print("receiverPrintYN (수신자 인쇄여부): %s" % info.receiverPrintYN)
        print("supplyCostTotal (공급가액 합계): %s" % info.supplyCostTotal)
        print("taxTotal (세액 합계): %s" % info.taxTotal)
        print("purposeType (영수/청구): %s" % info.purposeType)
        print("issueDT (발행일시): %s" % info.issueDT)
        print("stateCode (상태코드): %s" % info.stateCode)
        print("stateDT (상태 변경일시): %s" % info.stateDT)
        print("stateMemo (상태메모): %s" % info.stateMemo)
        print("openYN (개봉 여부): %s" % info.openYN)
        print("openDT (개봉 일시): %s" % info.openDT + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
