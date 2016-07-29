# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Statement, StatementDetail, StatementService, PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 선팩스 전송 " + "=" * 15)

    # 팩스발신번호
    SendNum = "070-7510-3710"

    # 팩스수신번호
    ReceiveNum = "070-111-222"

    # 전자명세서 정보
    statement = Statement(writeDate = "20150326",       # 작성일자 yyyyMMdd
                          purposeType = "영수",          # '영수'/'청구'
                          taxType = "과세",              # 세금형태, '과세'/'영세'/'면세'
                          formCode = "",                # 맞춤양식코드, 미기재시 기본양식으로 처리
                          itemCode = 121,               # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
                          mgtKey = "20160729-01",       # 파트너 부여 전자명세서 관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
                          senderCorpNum = testValue.testCorpNum, #공급자 사업자번호, '-' 제외 10자리
                          senderCorpName = "공급자 상호",
                          senderAddr = "공급자 주소",
                          senderCEOName = "공급자 대표자 성명",
                          senderTaxRegID = "",              # 공급자 종사업장번호, 필요시 4자리 숫자 기재
                          senderBizClass = "업종",
                          senderBizType = "업태",
                          senderContactName = "공급자 담당자명",
                          senderEmail = "test@test.com",
                          senderTEL = "070-7510-3710",
                          senderHP = "010-000-222",

                          receiverCorpNum = "8888888888",           #공급받는자 사업자번호 '-'제외 10자리
                          receiverCorpName = "공급받는자 상호",
                          receiverCEOName = "공급받는자 대표자 성명",
                          receiverAddr = "공급받는자 주소",
                          receiverTaxRegID = "",                    #공급받는자 종사업장번호, 필요시 4자리 숫자 기재
                          receiverBizClass = "공급받는자 업종",
                          receiverBizType = "공급받는자 업태",
                          receiverContactName = "공급받는자 담당자명",

                          receiverEmail = "test@test.com",
                          receiverTEL = "070111222",
                          receiverHP = "010-111-222",

                          supplyCostTotal = "20000",    # 공급가액 합계
                          taxTotal = "2000",            # 세액 합계
                          totalAmount = "22000",        # 합계금액, 공금가액+세액

                          serialNum = "123",            # 기재 상 '일련번호' 항목
                          remark1 = "비고1",
                          remark2 = "비고2",
                          remark3 = "비고3",

                          businessLicenseYN = False, # 사업자등록증 첨부 여부
                          bankBookYN = False, # 통장사본 첨부 여부

                          # 상세항목(품목) 정보
                          detailList = [
                                            StatementDetail(serialNum = 1,          #일련번호, 1부터 순차기재
                                                            itemName = "품목1",
                                                            purchaseDT = "20150323", # 거래일자
                                                            qty = 1,                # 수량
                                                            supplyCost = "20000",   # 공급가액
                                                            tax = "2000" #세액
                                                            ),
                                            StatementDetail(serialNum = 2,          #일련번호, 1부터 순차기재
                                                            itemName = "품목2"
                                                            )
                                        ],
                          # 추가속성정보, 명세서 종류별 추가적인 속성을{key:value}형식의 Dictionary로 정의
                          # 자세한 정보는 "전자명세서 API 연동매뉴얼 > [5.2. 기본양식 추가속성 테이블] 참조
                          propertyBag = {
                                        'Balance': '20000', # 전잔액
                                        'Deposit' : '5000', # 입금액
                                        'CBalance': '25000' # 현잔액
                                        }
                          )

    result = statementService.FAXSend(testValue.testCorpNum, statement, SendNum, ReceiveNum, testValue.testUserID)

    print("팩스 접수번호 : " + result)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
