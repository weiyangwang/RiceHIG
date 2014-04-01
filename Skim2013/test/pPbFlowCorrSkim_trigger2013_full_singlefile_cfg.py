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
'/store/hidata/HIRun2013/PAHighPt/RECO/PromptReco-v1/000/210/885/00000/46BC7074-746A-E211-A2A1-BCAEC518FF74.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(4000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")
#process.load("davidlw.HighPtFlow2011.EventFilter_cff")
process.load("davidlw.HighPtFlow2011.PAHighMultiplicityPileUpFilter_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM.HLTPaths = ['HLT_PAPixelTracks_Multiplicity*_v*']
process.hltHM.andOr = cms.bool(True)
process.hltHM.throw = cms.bool(False)

process.hltHMPt12 = process.hltHM.clone()
process.hltHMPt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity*_FullTrack12_*']

process.hltHF = process.hltHM.clone()
process.hltHF.HLTPaths = ['HLT_PAHFSumET*_v*']

process.eventFilter_HM = cms.Sequence( 
    process.hltHM *
    process.PAcollisionEventSelection *
    process.pAHighMultiplicityPileUpFilter_2Sigma_mode1
)
process.eventFilter_HM_step = cms.Path( process.eventFilter_HM )
process.extraTrks_HM_step   = cms.Path( process.eventFilter_HM * process.ppSingleTrackFilterSequence )

process.eventFilter_HMPt12 = cms.Sequence(
    process.hltHMPt12 *
    process.PAcollisionEventSelection *
    process.pAHighMultiplicityPileUpFilter_2Sigma_mode1
)
process.eventFilter_HMPt12_step = cms.Path( process.eventFilter_HMPt12 )
process.extraTrks_HMPt12_step   = cms.Path( process.eventFilter_HMPt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF = cms.Sequence(
    process.hltHF *
    process.PAcollisionEventSelection *
    process.pAHighMultiplicityPileUpFilter_2Sigma_mode1
)
process.eventFilter_HF_step = cms.Path( process.eventFilter_HF )
process.extraTrks_HF_step   = cms.Path( process.eventFilter_HF * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HM = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM'))
)
process.output_HMPt12 = process.output_HM.clone()
process.output_HMPt12.fileName = cms.untracked.string('pPb_HMPt12.root')
process.output_HMPt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HMPt12_step'))
process.output_HMPt12.dataset.filterName = cms.untracked.string('pPb_HMPt12')

process.output_HF = process.output_HM.clone()
process.output_HF.fileName = cms.untracked.string('pPb_HF.root')
process.output_HF.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF_step'))
process.output_HF.dataset.filterName = cms.untracked.string('pPb_HF')

process.output_HM_step = cms.EndPath(process.output_HM)
process.output_HMPt12_step = cms.EndPath(process.output_HMPt12)
process.output_HF_step = cms.EndPath(process.output_HF)

process.schedule = cms.Schedule(
    process.eventFilter_HM_step,
    process.eventFilter_HMPt12_step,
    process.eventFilter_HF_step,
    process.extraTrks_HM_step,
    process.extraTrks_HMPt12_step,
    process.extraTrks_HF_step,
    process.output_HM_step,
    process.output_HMPt12_step,
    process.output_HF_step,
)
