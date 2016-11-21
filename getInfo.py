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
1건의 전자명세서 상태/요약 정보를 확인합니다.
- 응답항목에 대한 자세한 정보는 "[전자명세서 API 연동매뉴얼] > 3.3.1.
  GetInfo (상태 확인)"을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 전자명세서 상태/요약 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    ItemCode = 121

    # 전자명세서 문서관리번호
    MgtKey = "20150326-01"

    statementInfo = statementService.getInfo(CorpNum, ItemCode, MgtKey)

    print ("itemCode : %s" % (statementInfo.itemCode))
    print ("itemKey : %s" % (statementInfo.itemKey))
    print ("invoiceNum : %s" % (statementInfo.invoiceNum))
    print ("mgtKey : %s" % (statementInfo.mgtKey))
    print ("taxType : %s" % (statementInfo.taxType))
    print ("writeDate : %s" % (statementInfo.writeDate))
    print ("regDT : %s" % (statementInfo.regDT))

    print ("senderCorpNum : %s" % (statementInfo.senderCorpNum))
    print ("senderCorpName : %s" % (statementInfo.senderCorpName))
    print ("receiverCorpNum : %s" % (statementInfo.receiverCorpNum))
    print ("receiverCorpName : %s" % (statementInfo.receiverCorpName))

    print ("supplyCostTotal : %s" % (statementInfo.supplyCostTotal))
    print ("taxTotal : %s" % (statementInfo.taxTotal))
    print ("purposeType : %s" % (statementInfo.purposeType))
    print ("isseuDT : %s" % (statementInfo.isseuDT))
    print ("stateCode : %s" % (statementInfo.stateCode))
    print ("stateDT : %s" % (statementInfo.stateDT))
    print ("stateMemo : %s" % (statementInfo.stateMemo))
    print ("openYN : %s" % (statementInfo.openYN))
    print ("openDT : %s" % (statementInfo.openDT))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
