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

process.hltHM130 = process.hltHM100.clone()
process.hltHM130.HLTPaths = ['HLT_PAPixelTracks_Multiplicity130_*']
process.hltHM160 = process.hltHM100.clone()
process.hltHM160.HLTPaths = ['HLT_PAPixelTracks_Multiplicity160_*']
process.hltHM190 = process.hltHM100.clone()
process.hltHM190.HLTPaths = ['HLT_PAPixelTracks_Multiplicity190_*']
process.hltHM220 = process.hltHM100.clone()
process.hltHM220.HLTPaths = ['HLT_PAPixelTracks_Multiplicity220_*']
process.hltHM100Pt12 = process.hltHM100.clone()
process.hltHM100Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity100_FullTrack12_*']
process.hltHM130Pt12 = process.hltHM100.clone()
process.hltHM130Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity130_FullTrack12_*']
process.hltHM160Pt12 = process.hltHM100.clone()
process.hltHM160Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity160_FullTrack12_*']
process.hltHF100 = process.hltHM100.clone()
process.hltHF100.HLTPaths = ['HLT_PAHFSumET100_*']
process.hltHF140 = process.hltHM100.clone()
process.hltHF140.HLTPaths = ['HLT_PAHFSumET140_*']
process.hltHF170 = process.hltHM100.clone()
process.hltHF170.HLTPaths = ['HLT_PAHFSumET170_*']
process.hltHF210 = process.hltHM100.clone()
process.hltHF210.HLTPaths = ['HLT_PAHFSumET210_*']
process.hltPt12 = process.hltHM100.clone()
process.hltPt12.HLTPaths = ['HLT_PAFullTrack12_*']
process.hltPt20 = process.hltHM100.clone()
process.hltPt20.HLTPaths = ['HLT_PAFullTrack20_*']
process.hltPt30 = process.hltHM100.clone()
process.hltPt30.HLTPaths = ['HLT_PAFullTrack30_*']
process.hltPt50 = process.hltHM100.clone()
process.hltPt50.HLTPaths = ['HLT_PAFullTrack50_*']

process.eventFilter_HM100 = cms.Sequence( 
    process.hltHM100 *
    process.PAcollisionEventSelection )
process.eventFilter_HM100_step = cms.Path( process.eventFilter_HM100 )
process.extraTrks_HM100_step   = cms.Path( process.eventFilter_HM100 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM130 = cms.Sequence(
    process.hltHM130 *
    process.PAcollisionEventSelection )
process.eventFilter_HM130_step = cms.Path( process.eventFilter_HM130 )
process.extraTrks_HM130_step   = cms.Path( process.eventFilter_HM130 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM160 = cms.Sequence(
    process.hltHM160 *
    process.PAcollisionEventSelection )
process.eventFilter_HM160_step = cms.Path( process.eventFilter_HM160 )
process.extraTrks_HM160_step   = cms.Path( process.eventFilter_HM160 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM190 = cms.Sequence(
    process.hltHM190 *
    process.PAcollisionEventSelection )
process.eventFilter_HM190_step = cms.Path( process.eventFilter_HM190 )
process.extraTrks_HM190_step   = cms.Path( process.eventFilter_HM190 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM220 = cms.Sequence(
    process.hltHM220 *
    process.PAcollisionEventSelection )
process.eventFilter_HM220_step = cms.Path( process.eventFilter_HM220 )
process.extraTrks_HM220_step   = cms.Path( process.eventFilter_HM220 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM100Pt12 = cms.Sequence(
    process.hltHM100Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM100Pt12_step = cms.Path( process.eventFilter_HM100Pt12 )
process.extraTrks_HM100Pt12_step   = cms.Path( process.eventFilter_HM100Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM130Pt12 = cms.Sequence(
    process.hltHM130Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM130Pt12_step = cms.Path( process.eventFilter_HM130Pt12 )
process.extraTrks_HM130Pt12_step   = cms.Path( process.eventFilter_HM130Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM160Pt12 = cms.Sequence(
    process.hltHM160Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM160Pt12_step = cms.Path( process.eventFilter_HM160Pt12 )
process.extraTrks_HM160Pt12_step   = cms.Path( process.eventFilter_HM160Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF100 = cms.Sequence(
    process.hltHF100 *
    process.PAcollisionEventSelection )
process.eventFilter_HF100_step = cms.Path( process.eventFilter_HF100 )
process.extraTrks_HF100_step   = cms.Path( process.eventFilter_HF100 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF140 = cms.Sequence(
    process.hltHF140 *
    process.PAcollisionEventSelection )
process.eventFilter_HF140_step = cms.Path( process.eventFilter_HF140 )
process.extraTrks_HF140_step   = cms.Path( process.eventFilter_HF140 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF170 = cms.Sequence(
    process.hltHF170 *
    process.PAcollisionEventSelection )
process.eventFilter_HF170_step = cms.Path( process.eventFilter_HF170 )
process.extraTrks_HF170_step   = cms.Path( process.eventFilter_HF170 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF210 = cms.Sequence(
    process.hltHF210 *
    process.PAcollisionEventSelection )
process.eventFilter_HF210_step = cms.Path( process.eventFilter_HF210 )
process.extraTrks_HF210_step   = cms.Path( process.eventFilter_HF210 * process.ppSingleTrackFilterSequence )

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
process.output_HM130 = process.output_HM100.clone()
process.output_HM130.fileName = cms.untracked.string('pPb_HM130.root')
process.output_HM130.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM130_step'))
process.output_HM130.dataset.filterName = cms.untracked.string('pPb_HM130')
process.output_HM160 = process.output_HM100.clone()
process.output_HM160.fileName = cms.untracked.string('pPb_HM160.root')
process.output_HM160.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM160_step'))
process.output_HM160.dataset.filterName = cms.untracked.string('pPb_HM160')
process.output_HM190 = process.output_HM100.clone()
process.output_HM190.fileName = cms.untracked.string('pPb_HM190.root')
process.output_HM190.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM190_step'))
process.output_HM190.dataset.filterName = cms.untracked.string('pPb_HM190')
process.output_HM220 = process.output_HM100.clone()
process.output_HM220.fileName = cms.untracked.string('pPb_HM220.root')
process.output_HM220.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM220_step'))
process.output_HM220.dataset.filterName = cms.untracked.string('pPb_HM220')
process.output_HM100Pt12 = process.output_HM100.clone()
process.output_HM100Pt12.fileName = cms.untracked.string('pPb_HM100Pt12.root')
process.output_HM100Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100Pt12_step'))
process.output_HM100Pt12.dataset.filterName = cms.untracked.string('pPb_HM100Pt12')
process.output_HM130Pt12 = process.output_HM100.clone()
process.output_HM130Pt12.fileName = cms.untracked.string('pPb_HM130Pt12.root')
process.output_HM130Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM130Pt12_step'))
process.output_HM130Pt12.dataset.filterName = cms.untracked.string('pPb_HM130Pt12')
process.output_HM160Pt12 = process.output_HM100.clone()
process.output_HM160Pt12.fileName = cms.untracked.string('pPb_HM160Pt12.root')
process.output_HM160Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM160Pt12_step'))
process.output_HM160Pt12.dataset.filterName = cms.untracked.string('pPb_HM160Pt12')
process.output_HF100 = process.output_HM100.clone()
process.output_HF100.fileName = cms.untracked.string('pPb_HF100.root')
process.output_HF100.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF100_step'))
process.output_HF100.dataset.filterName = cms.untracked.string('pPb_HF100')
process.output_HF140 = process.output_HM100.clone()
process.output_HF140.fileName = cms.untracked.string('pPb_HF140.root')
process.output_HF140.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF140_step'))
process.output_HF140.dataset.filterName = cms.untracked.string('pPb_HF140')
process.output_HF170 = process.output_HM100.clone()
process.output_HF170.fileName = cms.untracked.string('pPb_HF170.root')
process.output_HF170.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF170_step'))
process.output_HF170.dataset.filterName = cms.untracked.string('pPb_HF170')
process.output_HF210 = process.output_HM100.clone()
process.output_HF210.fileName = cms.untracked.string('pPb_HF210.root')
process.output_HF210.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF210_step'))
process.output_HF210.dataset.filterName = cms.untracked.string('pPb_HF210')
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

process.output_HM100_step = cms.EndPath(process.output_HM100)
process.output_HM130_step = cms.EndPath(process.output_HM130)
process.output_HM160_step = cms.EndPath(process.output_HM160)
process.output_HM190_step = cms.EndPath(process.output_HM190)
process.output_HM220_step = cms.EndPath(process.output_HM220)
process.output_HM100Pt12_step = cms.EndPath(process.output_HM100Pt12)
process.output_HM130Pt12_step = cms.EndPath(process.output_HM130Pt12)
process.output_HM160Pt12_step = cms.EndPath(process.output_HM160Pt12)
process.output_HF100_step = cms.EndPath(process.output_HF100)
process.output_HF140_step = cms.EndPath(process.output_HF140)
process.output_HF170_step = cms.EndPath(process.output_HF170)
process.output_HF210_step = cms.EndPath(process.output_HF210)
process.output_Pt12_step = cms.EndPath(process.output_Pt12)
process.output_Pt20_step = cms.EndPath(process.output_Pt20)
process.output_Pt30_step = cms.EndPath(process.output_Pt30)
process.output_Pt50_step = cms.EndPath(process.output_Pt50)

process.schedule = cms.Schedule(
    process.eventFilter_HM100_step,
    process.eventFilter_HM130_step,
    process.eventFilter_HM160_step,
    process.eventFilter_HM190_step,
    process.eventFilter_HM220_step,
    process.eventFilter_HM100Pt12_step,
    process.eventFilter_HM130Pt12_step,
    process.eventFilter_HM160Pt12_step,
    process.eventFilter_HF100_step,
    process.eventFilter_HF140_step,
    process.eventFilter_HF170_step,
    process.eventFilter_HF210_step,
    process.eventFilter_Pt12_step,
    process.eventFilter_Pt20_step,
    process.eventFilter_Pt30_step,
    process.eventFilter_Pt50_step,
    process.extraTrks_HM100_step,
    process.extraTrks_HM130_step,
    process.extraTrks_HM160_step,
    process.extraTrks_HM190_step,
    process.extraTrks_HM220_step,
    process.extraTrks_HM100Pt12_step,
    process.extraTrks_HM130Pt12_step,
    process.extraTrks_HM160Pt12_step,
    process.extraTrks_HF100_step,
    process.extraTrks_HF140_step,
    process.extraTrks_HF170_step,
    process.extraTrks_HF210_step,
    process.extraTrks_Pt12_step,
    process.extraTrks_Pt20_step,
    process.extraTrks_Pt30_step,
    process.extraTrks_Pt50_step,
    process.output_HM100_step,
    process.output_HM130_step,
    process.output_HM160_step,
    process.output_HM190_step,
    process.output_HM220_step,
    process.output_HM100Pt12_step,
    process.output_HM130Pt12_step,
    process.output_HM160Pt12_step,
    process.output_HF100_step,
    process.output_HF140_step,
    process.output_HF170_step,
    process.output_HF210_step,
    process.output_Pt12_step,
    process.output_Pt20_step,
    process.output_Pt30_step,
    process.output_Pt50_step
)
