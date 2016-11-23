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
다수건의 전자명세서 상태/요약 정보를 확인합니다.
- 응답항목에 대한 자세한 정보는 "[전자명세서 API 연동매뉴얼] > 3.3.2. GetInfos (상태 대량 확인)"
  을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 전자명세서 상태/요약 정보 확인 (대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    ItemCode = 121

    # 문서관리번호 배열, 최대 1000건
    MgtKeyList = []
    MgtKeyList.append("20161121-01")
    MgtKeyList.append("20161121-02")
    MgtKeyList.append("20161121-03")


    InfoList = statementService.getInfos(CorpNum, ItemCode, MgtKeyList)

    for info in InfoList:
        print("info : %s" % info.invoicerMgtKey)
        for key, value in info.__dict__.items():
            if not key.startswith("__"):
                print("     %s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
