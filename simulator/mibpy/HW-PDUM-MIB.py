#
# PySNMP MIB module HW-PDUM-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/HW-PDUM-MIB.txt
# Produced by pysmi-0.1.1 at Mon Apr  3 21:29:04 2017
# On host localhost.localdomain platform Linux version 3.10.0-123.el7.x86_64 by user root
# Using Python version 2.7.5 (default, Nov  6 2016, 00:28:07) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwPDUSmm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1))
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
hwOSTA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 82))
hwUSP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1))
hwPDU = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101))
hwPDUNode = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 1)).setObjects(("HW-PDUM-MIB", "hwSoftVersion"), ("HW-PDUM-MIB", "hwPduLinkStatus"), ("HW-PDUM-MIB", "hwPduVersion"), ("HW-PDUM-MIB", "hwBuzzerSw"), ("HW-PDUM-MIB", "hwMonitorStatus"), ("HW-PDUM-MIB", "hwLoadProc"), ("HW-PDUM-MIB", "hwLoadFile"), ("HW-PDUM-MIB", "hwBase2Status"), ("HW-PDUM-MIB", "hwBase1Status"), ("HW-PDUM-MIB", "hwPduLoadProc"), ("HW-PDUM-MIB", "hwPduLoadFile"), ("HW-PDUM-MIB", "hwAllLoadFile"), ("HW-PDUM-MIB", "hwAllLoadProc"), ("HW-PDUM-MIB", "hwPduResetReason"), ("HW-PDUM-MIB", "hwPduConfigData"), ("HW-PDUM-MIB", "hwPduWarningMask"), ("HW-PDUM-MIB", "hwPduAnalog"), ("HW-PDUM-MIB", "hwPduWarningStatus"), ("HW-PDUM-MIB", "hwPduLinkStatusNode"), ("HW-PDUM-MIB", "hwPduLinkStatusIndex"), ("HW-PDUM-MIB", "hwPduVersionIndex"), ("HW-PDUM-MIB", "hwPduVersioNode"), ("HW-PDUM-MIB", "hwPduConfigDataIndex"), ("HW-PDUM-MIB", "hwPduConfigDataNode"), ("HW-PDUM-MIB", "hwPduWarningMaskIndex"), ("HW-PDUM-MIB", "hwPduWarningMaskNode"), ("HW-PDUM-MIB", "hwPduAnalogIndex"), ("HW-PDUM-MIB", "hwPduAnalogNode"), ("HW-PDUM-MIB", "hwBuzzerSwIndex"), ("HW-PDUM-MIB", "hwBuzzerSwNode"), ("HW-PDUM-MIB", "hwPduResetReasoIndex"), ("HW-PDUM-MIB", "hwPduResetReasonNode"), ("HW-PDUM-MIB", "hwPduWarningStatusIndex"), ("HW-PDUM-MIB", "hwPduWarningStatusNode"), ("HW-PDUM-MIB", "hwSmmVer"), ("HW-PDUM-MIB", "hwPdumReset"), ("HW-PDUM-MIB", "hwBladeVerIndex"), ("HW-PDUM-MIB", "hwBladeVerNode"), ("HW-PDUM-MIB", "hwAllLoadMulProc"), ("HW-PDUM-MIB", "hwPdumDebug"), ("HW-PDUM-MIB", "bladeverion"), ("HW-PDUM-MIB", "versionindex"), ("HW-PDUM-MIB", "hwPdumTrapIpAddr"), ("HW-PDUM-MIB", "hwSmmInfo"), ("HW-PDUM-MIB", "hwPduAlmsNode"), ("HW-PDUM-MIB", "hwPduAlmsIndex"), ("HW-PDUM-MIB", "hwPduEidNode"), ("HW-PDUM-MIB", "hwPduEidIndex"))
hwPDUM = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2))
hwSoftVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduConfigData = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPduWarningMask = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPduAnalog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwBuzzerSw = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 7), OctetString().clone('on')).setMaxAccess("readwrite")
hwPduResetReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduWarningStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduLoadFile = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPduLoadProc = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
hwPduReset = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPdumTrapIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 102), )
hwPduLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 102, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduLinkStatusIndex"))
hwPduLinkStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 102, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduLinkStatusNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 102, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduVersionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 103), )
hwPduVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 103, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduVersionIndex"))
hwPduVersionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 103, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduVersioNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 103, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduConfigDataTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 104), )
hwPduConfigDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 104, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduConfigDataIndex"))
hwPduConfigDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 104, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduConfigDataNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 104, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPduWarningMaskTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 105), )
hwPduWarningMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 105, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduWarningMaskIndex"))
hwPduWarningMaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 105, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduWarningMaskNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 105, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
hwPduAnalogTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 106), )
hwPduAnalogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 106, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduAnalogIndex"))
hwPduAnalogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 106, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduAnalogNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 106, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwBuzzerSwTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 107), )
hwBuzzerSwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 107, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwBuzzerSwIndex"))
hwBuzzerSwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 107, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwBuzzerSwNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 107, 1, 2), OctetString()).setMaxAccess("readwrite")
hwPduResetReasonTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 108), )
hwPduResetReasonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 108, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduResetReasoIndex"))
hwPduResetReasoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 108, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduResetReasonNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 108, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduWarningStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 109), )
hwPduWarningStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 109, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduWarningStatusIndex"))
hwPduWarningStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 109, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduWarningStatusNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 109, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduEidTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111), )
hwPduEidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduEidIndex"))
hwPduEidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduEidNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048))).setMaxAccess("readonly")
hwPduE2pEidNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048))).setMaxAccess("readonly")
hwPduLogNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 111, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048))).setMaxAccess("readonly")
hwPduAlmsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 112), )
hwPduAlmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 112, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduAnalogIndex"))
hwPduAlmsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 112, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduAlmsNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 112, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
hwPduTimeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 113), )
hwPduTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 113, 1), ).setIndexNames((0, "HW-PDUM-MIB", "hwPduAnalogIndex"))
hwPduTimeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 113, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
hwPduTimeNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 82, 1, 101, 1, 2, 113, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
mibBuilder.exportSymbols("HW-PDUM-MIB", hwPdumTrapIpAddr=hwPdumTrapIpAddr, hwPduWarningMask=hwPduWarningMask, hwBuzzerSwIndex=hwBuzzerSwIndex, hwPduVersionTable=hwPduVersionTable, hwPduAlmsEntry=hwPduAlmsEntry, hwPduTimeTable=hwPduTimeTable, hwPduVersionEntry=hwPduVersionEntry, hwPduAlmsIndex=hwPduAlmsIndex, hwPDU=hwPDU, hwPduLogNode=hwPduLogNode, hwPduConfigData=hwPduConfigData, hwPduTimeEntry=hwPduTimeEntry, hwPDUSmm=hwPDUSmm, hwPduTimeNode=hwPduTimeNode, hwPduWarningMaskTable=hwPduWarningMaskTable, PYSNMP_MODULE_ID=hwPDUSmm, hwPduE2pEidNode=hwPduE2pEidNode, hwPduWarningMaskNode=hwPduWarningMaskNode, hwPduResetReasonNode=hwPduResetReasonNode, hwPduWarningStatusNode=hwPduWarningStatusNode, hwPduLinkStatusTable=hwPduLinkStatusTable, hwPduConfigDataEntry=hwPduConfigDataEntry, hwPduLinkStatusEntry=hwPduLinkStatusEntry, hwPduAnalogIndex=hwPduAnalogIndex, hwPduEidIndex=hwPduEidIndex, hwBuzzerSwEntry=hwBuzzerSwEntry, hwPduLinkStatus=hwPduLinkStatus, hwPduResetReasonEntry=hwPduResetReasonEntry, hwPduAnalogEntry=hwPduAnalogEntry, hwBuzzerSwTable=hwBuzzerSwTable, hwPduConfigDataIndex=hwPduConfigDataIndex, hwPDUM=hwPDUM, products=products, huawei=huawei, hwPDUNode=hwPDUNode, hwPduEidEntry=hwPduEidEntry, hwUSP=hwUSP, hwPduVersioNode=hwPduVersioNode, hwPduLinkStatusNode=hwPduLinkStatusNode, hwOSTA=hwOSTA, hwPduWarningStatus=hwPduWarningStatus, hwPduTimeIndex=hwPduTimeIndex, hwPduAlmsNode=hwPduAlmsNode, hwPduResetReasoIndex=hwPduResetReasoIndex, hwPduEidNode=hwPduEidNode, hwPduResetReasonTable=hwPduResetReasonTable, hwPduResetReason=hwPduResetReason, hwSoftVersion=hwSoftVersion, hwPduAnalogTable=hwPduAnalogTable, hwPduWarningStatusEntry=hwPduWarningStatusEntry, hwPduWarningStatusTable=hwPduWarningStatusTable, hwPduConfigDataNode=hwPduConfigDataNode, hwBuzzerSwNode=hwBuzzerSwNode, hwPduVersion=hwPduVersion, hwPduEidTable=hwPduEidTable, hwPduVersionIndex=hwPduVersionIndex, hwPduWarningMaskIndex=hwPduWarningMaskIndex, hwBuzzerSw=hwBuzzerSw, hwPduAnalogNode=hwPduAnalogNode, hwPduConfigDataTable=hwPduConfigDataTable, hwPduAlmsTable=hwPduAlmsTable, hwPduAnalog=hwPduAnalog, hwPduWarningStatusIndex=hwPduWarningStatusIndex, hwPduLinkStatusIndex=hwPduLinkStatusIndex, hwPduReset=hwPduReset, hwPduLoadFile=hwPduLoadFile, hwPduLoadProc=hwPduLoadProc, hwPduWarningMaskEntry=hwPduWarningMaskEntry)
