import FWCore.ParameterSet.Config as cms

process = cms.Process("V0Val")
process.load("FWCore.MessageService.MessageLogger_cfi")

### standard includes
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'STARTHI53_V17::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
#'/store/user/vzhukova/HYDGET_PERIPH_batch7/HYDGET_PERIPH_RECO_batch7/b7d33bba7673cdb1ee6f4983c0800c79/HYDGET_PERIPH_RECO_10_1_7bq.root'
'/store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_4_2_RU0.root'
                )
                            )

### validation-specific includes
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.load("RiceHIG.V0Analysis.v0selector_cff")
process.load("RiceHIG.V0Analysis.v0validator_cff")
process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
process.load("DQMServices.Components.EDMtoMEConverter_cff")

process.generalV0CandidatesNew = process.generalV0Candidates.clone (
    tkNhitsCut = cms.int32(0),
    tkChi2Cut = cms.double(7.0),
    dauTransImpactSigCut = cms.double(1.0),
    dauLongImpactSigCut = cms.double(1.0),
    xiVtxSignificance3DCut = cms.double(0.0),
    xiVtxSignificance2DCut = cms.double(0.0),
    vtxSignificance2DCut = cms.double(0.0),
    vtxSignificance3DCut = cms.double(4.0)
)   

process.v0Validator.DQMRootFileName = 'v0validation.root'
process.v0Validator.kShortCollection = cms.InputTag('selectV0CandidatesNewkshort:Kshort')
process.v0Validator.lambdaCollection = cms.InputTag('selectV0CandidatesNewlambda:Lambda')

process.selectV0CandidatesNewlambda.v0CollName = cms.string("generalV0CandidatesNew")
process.selectV0CandidatesNewkshort.v0CollName = cms.string("generalV0CandidatesNew")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.v0validation = cms.Sequence(process.generalV0CandidatesNew*process.selectV0CandidatesNewlambda*process.selectV0CandidatesNewkshort*process.v0Validator)

process.p = cms.Path(process.v0validation)

process.schedule = cms.Schedule(process.p)
