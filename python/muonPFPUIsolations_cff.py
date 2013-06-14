import FWCore.ParameterSet.Config as cms
import MyAnalysis.IsolationTools.muonPFIsoSingleType_cfi

### DR=0.3 cone
# Charged Hadron isolation
muonPUPFIsoChHad03 = MyAnalysis.IsolationTools.muonPFIsoSingleType_cfi.muonPFIsoSingleTypeMapProd.clone()
muonPUPFIsoChHad03.pfTypes = cms.untracked.vint32(1)
muonPUPFIsoChHad03.deltaR = 0.3
muonPUPFIsoChHad03.pfLabel = cms.untracked.InputTag("pfPileUp")

### DR=0.4 cone
# Charged Hadron isolation
muonPUPFIsoChHad04 = MyAnalysis.IsolationTools.muonPFIsoSingleType_cfi.muonPFIsoSingleTypeMapProd.clone()
muonPUPFIsoChHad04.pfTypes = cms.untracked.vint32(1)
muonPUPFIsoChHad04.deltaR = 0.4
muonPUPFIsoChHad04.pfLabel = cms.untracked.InputTag("pfPileUp")
