import FWCore.ParameterSet.Config as cms
process = cms.Process("ANASKIM3")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
'root://xrootd2.cmsaf.mit.edu//store/results/heavy-ions/MinimumBias/StoreResults-PP2010A_Apr21ReReco_TRKANASKIM_HIGHMULT_v2-d3b00b9920e9d4ebdfcff6a3f8ddc689-ppGoodColl_minbias/MinimumBias/USER/StoreResults-PP2010A_Apr21ReReco_TRKANASKIM_HIGHMULT_v2-d3b00b9920e9d4ebdfcff6a3f8ddc689-ppGoodColl_minbias/0000/38A9025B-853E-E211-A433-90B11C0BCCA0.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V43F::All'

########## V0 candidate rereco ############################################################### 
process.generalV0CandidatesNew = process.generalV0Candidates.clone (
    tkNhitsCut = cms.int32(0),
    tkChi2Cut = cms.double(7.0),
    dauTransImpactSigCut = cms.double(1.0),
    dauLongImpactSigCut = cms.double(1.0),
    xiVtxSignificance3DCut = cms.double(0.0),
    xiVtxSignificance2DCut = cms.double(0.0),
    vtxSignificance2DCut = cms.double(0.0),
    vtxSignificance3DCut = cms.double(4.0),
    innerHitPosCut = cms.double(-1)
)   

process.v0rereco_step = cms.Path( process.generalV0CandidatesNew )

###############################################################################################

process.load("RiceHIG.Skim2013.ppanalysisSkimContentFull_cff")
process.output_HM = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM.root'),
#    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM'))
)
#process.output_HM.outputCommands.extend(cms.untracked.vstring('keep *_*_*_*'))
#process.output_HM.outputCommands.extend(cms.untracked.vstring('drop *_*_*_ANASKIM2'))
#process.output_HM.outputCommands.extend(cms.untracked.vstring('keep *_generalV0CandidatesNew_Xi_ANASKIM2'))
#process.output_HM.outputCommands.extend(cms.untracked.vstring('keep *_generalV0CandidatesNew_Omega_ANASKIM2'))

process.output_HM_step = cms.EndPath(process.output_HM)

process.schedule = cms.Schedule(
    process.v0rereco_step,
    process.output_HM_step
)
