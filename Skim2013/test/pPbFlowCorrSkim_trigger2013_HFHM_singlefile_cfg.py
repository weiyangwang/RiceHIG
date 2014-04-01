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
process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2013A/PAHighPt/RECO/PromptReco-v1/000/210/634/FA4E6B7E-7366-E211-8DD0-0019B9F581C9.root'
)
)
# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(4000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")
process.load("davidlw.HighPtFlow2011.PAHighMultiplicityPileUpFilter_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHF = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHF.HLTPaths = ['HLT_PAHFSumET*_v*']
process.hltHF.andOr = cms.bool(True)
process.hltHF.throw = cms.bool(False)

process.eventFilter_HF = cms.Sequence(
    process.hltHF *
    process.PAcollisionEventSelection *
    process.pAHighMultiplicityPileUpFilter_2Sigma_mode1
)
process.eventFilter_HF_step = cms.Path( process.eventFilter_HF )
process.extraTrks_HF_step   = cms.Path( process.eventFilter_HF * process.ppSingleTrackFilterSequence )

process.pACentrality_step = cms.Path( process.eventFilter_HF * process.pACentrality)
process.pACentrality.producePixelhits = False

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HF = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HF.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HF'))
)

process.output_HF_step = cms.EndPath(process.output_HF)

process.schedule = cms.Schedule(
    process.eventFilter_HF_step,
    process.extraTrks_HF_step,
    process.pACentrality_step,
    process.output_HF_step,
)
