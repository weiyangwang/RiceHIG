import FWCore.ParameterSet.Config as cms
process = cms.Process("ANASKIM")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
#        'file:/mnt/hadoop/cms/store/hidata/HIRun2010/HIAllPhysics/RECO/SDmaker_3SD_1CS_PDHIAllPhysicsZSv2_SD_JetHI-v1/0000/A8934EC1-904B-E011-862C-003048F17528.root'
'/store/data/Run2012A/MinimumBias/RECO/PromptReco-v1/000/190/949/3A5054BB-7486-E111-A825-0025B324400C.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_R_44_V10::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMinBiasHF = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMinBiasHF.HLTPaths = ['HLT_PixelTracks_Multiplicity100_*'] 
process.hltMinBiasHF.andOr = cms.bool(True)
process.hltMinBiasHF.throw = cms.bool(False)

process.eventFilter = cms.Sequence( 
    process.hltMinBiasHF  
#    process.collisionEventSelection 
)

process.eventFilter_step = cms.Path( process.eventFilter )
#process.extraTrks_step   = cms.Path( process.eventFilter * process.ppSingleTrackFilterSequence )

process.extraTrks_step   = cms.Path( process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl'))
)

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.eventFilter_step,
#    process.extraTrks_step,
    process.output_step
)

