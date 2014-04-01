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
process.load("davidlw.HighPtFlow2011.EventFilter_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltTrigger100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltTrigger100.HLTPaths = ['HLT_PixelTracks_Multiplicity100_*'] 
process.hltTrigger100.andOr = cms.bool(True)
process.hltTrigger100.throw = cms.bool(False)

process.hltTrigger80 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltTrigger80.HLTPaths = ['HLT_PixelTracks_Multiplicity80_*']
process.hltTrigger80.andOr = cms.bool(True)
process.hltTrigger80.throw = cms.bool(False)

process.eventFilter_trigger80 = cms.Sequence( 
    process.hltTrigger80 * 
    process.collisionEventSelection 
)

process.eventFilter_trigger100 = cms.Sequence(
    process.hltTrigger100 * 
    process.collisionEventSelection
)

process.eventFilter_trigger80_step = cms.Path( process.eventFilter_trigger80 )
process.eventFilter_trigger100_step = cms.Path( process.eventFilter_trigger100 )
process.extraTrks_trigger80_step   = cms.Path( process.eventFilter_trigger80 * process.ppSingleTrackFilterSequence )
process.extraTrks_trigger100_step   = cms.Path( process.eventFilter_trigger100 * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_trigger100 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_trigger100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_trigger100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_trigger100'))
)
process.output_trigger80 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_trigger80.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_trigger80_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_trigger80'))
)

process.output_trigger80_step = cms.EndPath(process.output_trigger80)
process.output_trigger100_step = cms.EndPath(process.output_trigger100)

process.schedule = cms.Schedule(
    process.eventFilter_trigger80_step,
    process.eventFilter_trigger100_step,
    process.extraTrks_trigger80_step,
    process.extraTrks_trigger100_step,
    process.output_trigger80_step,
    process.output_trigger100_step
)

