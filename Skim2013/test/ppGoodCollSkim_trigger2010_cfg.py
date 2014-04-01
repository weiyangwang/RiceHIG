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
'/store/data/Run2010B/MinimumBias/RECO/Apr21ReReco-v1/0002/B6799295-1871-E011-9A1B-001A92971B1A.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_R_44_V10::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")
process.load("davidlw.HighPtFlow2011.EventFilter_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltTrigger100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltTrigger100.HLTPaths = ['HLT_PixelTracks_Multiplicity100'] 
process.hltTrigger100.andOr = cms.bool(True)
process.hltTrigger100.throw = cms.bool(False)

process.hltTrigger85 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltTrigger85.HLTPaths = ['HLT_PixelTracks_Multiplicity85']
process.hltTrigger85.andOr = cms.bool(True)
process.hltTrigger85.throw = cms.bool(False)

process.hltTrigger70 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltTrigger70.HLTPaths = ['HLT_PixelTracks_Multiplicity70']
process.hltTrigger70.andOr = cms.bool(True)
process.hltTrigger70.throw = cms.bool(False)

process.eventFilter_trigger70 = cms.Sequence(
    process.hltTrigger70 *
    process.collisionEventSelection
)

process.eventFilter_trigger85 = cms.Sequence( 
    process.hltTrigger85 * 
    process.collisionEventSelection 
)

process.eventFilter_trigger100 = cms.Sequence(
    process.hltTrigger100 * 
    process.collisionEventSelection
)

process.eventFilter_minbias = cms.Sequence(
    process.minBiasOrzeroBiasHLTBscFilter *
    process.collisionEventSelection
)

process.eventFilter_trigger70_step = cms.Path( process.eventFilter_trigger70 )
process.eventFilter_trigger85_step = cms.Path( process.eventFilter_trigger85 )
process.eventFilter_trigger100_step = cms.Path( process.eventFilter_trigger100 )
process.eventFilter_minbias_step = cms.Path( process.eventFilter_minbias )
process.extraTrks_trigger70_step   = cms.Path( process.eventFilter_trigger70 * process.ppSingleTrackFilterSequence ) 
process.extraTrks_trigger85_step   = cms.Path( process.eventFilter_trigger85 * process.ppSingleTrackFilterSequence )
process.extraTrks_trigger100_step   = cms.Path( process.eventFilter_trigger100 * process.ppSingleTrackFilterSequence )
process.extraTrks_minbias_step   = cms.Path( process.eventFilter_minbias * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_trigger100 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_trigger100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_trigger100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_trigger100'))
)
process.output_trigger85 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_trigger85.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_trigger85_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_trigger85'))
)
process.output_trigger70 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_trigger70.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_trigger70_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_trigger70'))
)
process.output_minbias = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('ppGoodColl_minbias.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_minbias_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('ppGoodColl_minbias'))
)

process.output_trigger70_step = cms.EndPath(process.output_trigger70)
process.output_trigger85_step = cms.EndPath(process.output_trigger85)
process.output_trigger100_step = cms.EndPath(process.output_trigger100)
process.output_minbias_step = cms.EndPath(process.output_minbias)

process.schedule = cms.Schedule(
    process.eventFilter_trigger70_step,
    process.eventFilter_trigger85_step,
    process.eventFilter_trigger100_step,
    process.eventFilter_minbias_step,
    process.extraTrks_trigger70_step,
    process.extraTrks_trigger85_step,
    process.extraTrks_trigger100_step,
    process.extraTrks_minbias_step,
    process.output_trigger70_step,
    process.output_trigger85_step,
    process.output_trigger100_step,
    process.output_minbias_step
)

