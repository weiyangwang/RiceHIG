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
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
'/store/hidata/data/PARun2012/PAPhysics/RECO/PromptReco-v2/000/202/654/A404793B-6BFE-E111-92DD-001D09F24DA8.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")
#process.load("davidlw.HighPtFlow2011.EventFilter_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM100.HLTPaths = ['HLT_PAPixelTracks_Multiplicity100_*']
process.hltHM100.andOr = cms.bool(True)
process.hltHM100.throw = cms.bool(False)

process.hltPt12 = process.hltHM100.clone()
process.hltPt12.HLTPaths = ['HLT_PAFullTrack12_*']
process.hltPt20 = process.hltHM100.clone()
process.hltPt20.HLTPaths = ['HLT_PAFullTrack20_*']
process.hltPt30 = process.hltHM100.clone()
process.hltPt30.HLTPaths = ['HLT_PAFullTrack30_*']
process.hltPt50 = process.hltHM100.clone()
process.hltPt50.HLTPaths = ['HLT_PAFullTrack50_*']

process.eventFilter_Pt12 = cms.Sequence(
    process.hltPt12 *
    process.PAcollisionEventSelection )
process.eventFilter_Pt12_step = cms.Path( process.eventFilter_Pt12 )
process.extraTrks_Pt12_step   = cms.Path( process.eventFilter_Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_Pt20 = cms.Sequence(
    process.hltPt20 *
    process.PAcollisionEventSelection )
process.eventFilter_Pt20_step = cms.Path( process.eventFilter_Pt20 )
process.extraTrks_Pt20_step   = cms.Path( process.eventFilter_Pt20 * process.ppSingleTrackFilterSequence )

process.eventFilter_Pt30 = cms.Sequence(
    process.hltPt30 *
    process.PAcollisionEventSelection )
process.eventFilter_Pt30_step = cms.Path( process.eventFilter_Pt30 )
process.extraTrks_Pt30_step   = cms.Path( process.eventFilter_Pt30 * process.ppSingleTrackFilterSequence )

process.eventFilter_Pt50 = cms.Sequence(
    process.hltPt50 *
    process.PAcollisionEventSelection )
process.eventFilter_Pt50_step = cms.Path( process.eventFilter_Pt50 )
process.extraTrks_Pt50_step   = cms.Path( process.eventFilter_Pt50 * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HM100 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM100'))
)
process.output_Pt12 = process.output_HM100.clone()
process.output_Pt12.fileName = cms.untracked.string('pPb_Pt12.root')
process.output_Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_Pt12_step'))
process.output_Pt12.dataset.filterName = cms.untracked.string('pPb_Pt12')
process.output_Pt20 = process.output_HM100.clone()
process.output_Pt20.fileName = cms.untracked.string('pPb_Pt20.root')
process.output_Pt20.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_Pt20_step'))
process.output_Pt20.dataset.filterName = cms.untracked.string('pPb_Pt20')
process.output_Pt30 = process.output_HM100.clone()
process.output_Pt30.fileName = cms.untracked.string('pPb_Pt30.root')
process.output_Pt30.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_Pt30_step'))
process.output_Pt30.dataset.filterName = cms.untracked.string('pPb_Pt30')
process.output_Pt50 = process.output_HM100.clone()
process.output_Pt50.fileName = cms.untracked.string('pPb_Pt50.root')
process.output_Pt50.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_Pt50_step'))
process.output_Pt50.dataset.filterName = cms.untracked.string('pPb_Pt50')

process.output_Pt12_step = cms.EndPath(process.output_Pt12)
process.output_Pt20_step = cms.EndPath(process.output_Pt20)
process.output_Pt30_step = cms.EndPath(process.output_Pt30)
process.output_Pt50_step = cms.EndPath(process.output_Pt50)

process.schedule = cms.Schedule(
    process.eventFilter_Pt12_step,
    process.eventFilter_Pt20_step,
    process.eventFilter_Pt30_step,
    process.eventFilter_Pt50_step,
    process.extraTrks_Pt12_step,
    process.extraTrks_Pt20_step,
    process.extraTrks_Pt30_step,
    process.extraTrks_Pt50_step,
    process.output_Pt12_step,
    process.output_Pt20_step,
    process.output_Pt30_step,
    process.output_Pt50_step
)
