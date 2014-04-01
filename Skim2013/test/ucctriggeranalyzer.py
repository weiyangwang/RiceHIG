import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/net/hisrv0001/home/davidlw/scratch1/rereco_441.root'
#      '/store/data/Run2010A/MinimumBias/RECO/v2/000/137/024/567B76FB-7970-DF11-873C-001617C3B706.root'
      '/store/mc/Fall11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/GEN-SIM-RECO/RecoTest44_PU_S6_START44_V5-v1/0000/68DEFF49-B9E7-E011-BF62-90E6BA442F31.root'
    )
)

process.TFileService = cms.Service('TFileService',
     fileName = cms.string('output_ucctrigger.root')
)        

process.demo = cms.EDAnalyzer('UCCTriggerAnalyzer',
   srcPixelClusters = cms.untracked.InputTag("siPixelClusters"),
   srcSumET = cms.untracked.InputTag("met")
)


process.p = cms.Path(process.demo)
