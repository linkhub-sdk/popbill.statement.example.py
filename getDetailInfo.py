# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import StatementService, PopbillException

statementService =  StatementService(testValue.LinkID,testValue.SecretKey)
statementService.IsTest = testValue.IsTest

try:
    print("전자명세서 상세정보 확인")
    
    ItemCode = 121 # 명세서 코드, [121-거래명세서], [122-청구서], [123-견적서] [124-발주서], [125-입금표], [126-영수증]
    MgtKey = "20150326-01" #파트너 부여 전자명세서 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
 
    #전자명세서 임시저장시 구성한 정보를 반환한다.
    statement = statementService.getDetailInfo(testValue.testCorpNum,ItemCode,MgtKey)
    
    print ("itemCode : %s" % (statement.itemCode))
    print ("mgtKey : %s" % (statement.mgtKey))
    print ("invoiceNum : %s" % (statement.invoiceNum))
    print ("formCode : %s" % (statement.formCode))
    print ("writeDate : %s" % (statement.writeDate))
    print ("taxType : %s" % (statement.taxType))
    print ("purposeType : %s" % (statement.purposeType))
    print ("serialNum : %s" % (statement.serialNum))
    print ("taxTotal : %s" % (statement.taxTotal))
    print ("supplyCostTotal : %s" % (statement.supplyCostTotal))
    print ("totalAmount : %s" % (statement.totalAmount))
    print ("remark1 : %s" % (statement.remark1))
    print ("remark2 : %s" % (statement.remark2))
    print ("remark3 : %s" % (statement.remark3)+"\n")

    print ("senderCorpNum : %s" % (statement.senderCorpNum))
    print ("senderTaxRegID : %s" % (statement.senderTaxRegID))
    print ("senderCorpName : %s" % (statement.senderCorpName))
    print ("senderCEOName : %s" % (statement.senderCEOName))
    print ("senderAddr : %s" % (statement.senderAddr))
    print ("senderBizType : %s" % (statement.senderBizType))
    print ("senderBizClass : %s" % (statement.senderBizClass))
    print ("senderContactName : %s" % (statement.senderContactName))
    print ("senderDeptName : %s" % (statement.senderDeptName))
    print ("senderTEL : %s" % (statement.senderTEL))
    print ("senderHP : %s" % (statement.senderHP))
    print ("senderEmail : %s" % (statement.senderEmail)+"\n")

    print ("receiverCorpNum : %s" % (statement.receiverCorpNum))
    print ("receiverTaxRegID : %s" % (statement.receiverTaxRegID))
    print ("receiverCorpName : %s" % (statement.receiverCorpName))
    print ("receiverCEOName : %s" % (statement.receiverCEOName))
    print ("receiverAddr : %s" % (statement.receiverAddr))
    print ("receiverBizClass : %s" % (statement.receiverBizClass))
    print ("receiverBizType : %s" % (statement.receiverBizType))
    print ("receiverContactName : %s" % (statement.receiverContactName))
    print ("receiverDeptName : %s" % (statement.receiverDeptName))
    print ("receiverTEL : %s" % (statement.receiverTEL))
    print ("receiverHP : %s" % (statement.receiverHP))
    print ("receiverEmail : %s" % (statement.receiverEmail)+"\n")

    for n in range(0, len(statement.detailList)):
        print ("detailList[%s] "% n)
        print ("       serialNum : %s "% statement.detailList[n].serialNum)
        print ("       purchaseDT : %s "% statement.detailList[n].purchaseDT)
        print ("       itemName : %s "% statement.detailList[n].itemName)
        print ("       spec : %s "% statement.detailList[n].spec)
        print ("       qty : %s "% statement.detailList[n].qty)
        print ("       unitCost : %s "% statement.detailList[n].unitCost)
        print ("       supplyCost : %s "% statement.detailList[n].supplyCost)
        print ("       tax : %s "% statement.detailList[n].tax+"\n")
        #print ("       spare1 : %s "% statement.detailList[n].spare1)
        #print ("       spare2 : %s "% statement.detailList[n].spare2)
        #print ("       spare3 : %s "% statement.detailList[n].spare3)
        #print ("       spare4 : %s "% statement.detailList[n].spare4)
        #print ("       spare5 : %s "% statement.detailList[n].spare5)
    
    if statement.propertyBag is not None:
        print ("propertyBag : ")
        for key, value in statement.propertyBag.__dict__.items():
            print("       %s : %s" % (key,value))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
