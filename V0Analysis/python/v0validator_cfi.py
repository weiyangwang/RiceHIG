import FWCore.ParameterSet.Config as cms

v0Validator = cms.EDAnalyzer('V0Validator',
    kShortCollection = cms.InputTag('generalV0Candidates:Kshort'),
    lambdaCollection = cms.InputTag('generalV0Candidates:Lambda'),
)
