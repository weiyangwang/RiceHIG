import FWCore.ParameterSet.Config as cms

v0Validator = cms.EDAnalyzer('V0Validator',
    trackCollection = cms.InputTag('generalTracks'),
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    kShortCollection = cms.InputTag('generalV0Candidates:Kshort'),
    lambdaCollection = cms.InputTag('generalV0Candidates:Lambda'),
    isMatchByHitsOrChi2 = cms.bool(True)
)
