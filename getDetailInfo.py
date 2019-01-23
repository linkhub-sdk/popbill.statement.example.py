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

'''
전자명세서 1건의 상세정보를 조회합니다.
- 응답항목에 대한 자세한 사항은 "[전자명세서 API 연동매뉴얼] > 4.1. 전자명세서 구성" 을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 전자명세서 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서, 125-입금표, 126-영수증
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20190117-001"

    statement = statementService.getDetailInfo(CorpNum, ItemCode, MgtKey)

    print ("itemCode(문서종류코드) : %s" % (statement.itemCode))
    print ("mgtKey(관리번호) : %s" % (statement.mgtKey))
    print ("invoiceNum(문서고유번호) : %s" % (statement.invoiceNum))
    print ("formCode(맞춤양식 코드) : %s" % (statement.formCode))
    print ("writeDate(작성일자) : %s" % (statement.writeDate))
    print ("taxType(세금형태) : %s" % (statement.taxType))
    print ("purposeType(영수/청구) : %s" % (statement.purposeType))
    print ("serialNum(일련번호) : %s" % (statement.serialNum))
    print ("taxTotal(세액 합계) : %s" % (statement.taxTotal))
    print ("supplyCostTotal(공급가액 합계) : %s" % (statement.supplyCostTotal))
    print ("totalAmount(합계금액) : %s" % (statement.totalAmount))
    print ("remark1(비고1) : %s" % (statement.remark1))
    print ("remark2(비고2) : %s" % (statement.remark2))
    print ("remark3(비고3) : %s" % (statement.remark3) + "\n")

    print ("senderCorpNum(발신자 사업자번호) : %s" % (statement.senderCorpNum))
    print ("senderTaxRegID(발신자 종사업장번호) : %s" % (statement.senderTaxRegID))
    print ("senderCorpName(발신자 상호) : %s" % (statement.senderCorpName))
    print ("senderCEOName(발신자 대표자성명) : %s" % (statement.senderCEOName))
    print ("senderAddr(발신자 주소) : %s" % (statement.senderAddr))
    print ("senderBizType(발신자 업태) : %s" % (statement.senderBizType))
    print ("senderBizClass(발신자 종목) : %s" % (statement.senderBizClass))
    print ("senderContactName(발신자 성명) : %s" % (statement.senderContactName))
    print ("senderDeptName(발신자 부서명) : %s" % (statement.senderDeptName))
    print ("senderTEL(발신자 연락처) : %s" % (statement.senderTEL))
    print ("senderHP(발신자 휴대전화) : %s" % (statement.senderHP))
    print ("senderEmail(발신자 이메일주소) : %s" % (statement.senderEmail))
    print ("senderFax(발신자 팩스번호) : %s" % (statement.senderFax) + "\n")

    print ("receiverCorpNum(수신자 사업자번호) : %s" % (statement.receiverCorpNum))
    print ("receiverTaxRegID(수신자 종사업장번호) : %s" % (statement.receiverTaxRegID))
    print ("receiverCorpName(수신자 상호) : %s" % (statement.receiverCorpName))
    print ("receiverCEOName(수신자 대표자성명) : %s" % (statement.receiverCEOName))
    print ("receiverAddr(수신자 주소) : %s" % (statement.receiverAddr))
    print ("receiverBizClass(수신자 업태) : %s" % (statement.receiverBizClass))
    print ("receiverBizType(수신자 종목) : %s" % (statement.receiverBizType))
    print ("receiverContactName(수신자 성명) : %s" % (statement.receiverContactName))
    print ("receiverDeptName(수신자 부서명) : %s" % (statement.receiverDeptName))
    print ("receiverTEL(수신자 연락처) : %s" % (statement.receiverTEL))
    print ("receiverHP(수신자 휴대전화) : %s" % (statement.receiverHP))
    print ("receiverEmail(수신자 이메일주소) : %s" % (statement.receiverEmail))
    print ("receiverFax(수신자 팩스번호) : %s" % (statement.receiverFax) + "\n")

    for n in range(0, len(statement.detailList)):
        print ("detailList[%s] " % (n + 1))
        print ("       serialNum(일련번호) : %s " % statement.detailList[n].serialNum)
        print ("       purchaseDT(거래일자) : %s " % statement.detailList[n].purchaseDT)
        print ("       itemName(품목명) : %s " % statement.detailList[n].itemName)
        print ("       spec(규격) : %s " % statement.detailList[n].spec)
        print ("       qty(수량) : %s " % statement.detailList[n].qty)
        print ("       unitCost(단가) : %s " % statement.detailList[n].unitCost)
        print ("       supplyCost(공급가액) : %s " % statement.detailList[n].supplyCost)
        print ("       tax(세액) : %s " % statement.detailList[n].tax + "\n")
        # print ("       spare1(비고1) : %s "% statement.detailList[n].spare1)
        # print ("       spare2(비고2) : %s "% statement.detailList[n].spare2)
        # print ("       spare3(비고3) : %s "% statement.detailList[n].spare3)
        # print ("       spare4(비고4) : %s "% statement.detailList[n].spare4)
        # print ("       spare5(비고5) : %s "% statement.detailList[n].spare5)

    if statement.propertyBag is not None:
        print ("propertyBag : ")
        for key, value in statement.propertyBag.__dict__.items():
            print("       %s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
