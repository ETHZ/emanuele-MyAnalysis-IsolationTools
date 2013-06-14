import FWCore.ParameterSet.Config as cms
import MyAnalysis.IsolationTools.electronPFIsoSingleType_cfi

### DR=0.3 cone
# Charged Hadron isolation
electronPUPFIsoChHad03 = MyAnalysis.IsolationTools.electronPFIsoSingleType_cfi.electronPFIsoSingleTypeMapProd.clone()
electronPUPFIsoChHad03.pfTypes = cms.untracked.vint32(1)
electronPUPFIsoChHad03.deltaR = 0.3
electronPUPFIsoChHad03.pfLabel = cms.untracked.InputTag("pfPileUp")

### DR=0.4 cone
# Charged Hadron isolation
electronPUPFIsoChHad04 = MyAnalysis.IsolationTools.electronPFIsoSingleType_cfi.electronPFIsoSingleTypeMapProd.clone()
electronPUPFIsoChHad04.pfTypes = cms.untracked.vint32(1)
electronPUPFIsoChHad04.deltaR = 0.4
electronPUPFIsoChHad04.pfLabel = cms.untracked.InputTag("pfPileUp")
