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
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/CEACE1ED-4C61-E211-9295-001D09F297EF.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/3048394B-4F61-E211-89FB-001D09F2525D.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/BE45724A-4F61-E211-9F85-003048F11112.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/345B5494-2E61-E211-A403-0025901D627C.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/BA2DF349-4F61-E211-99D3-0025901D6272.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/E02B0623-4E61-E211-B51C-0030486780E6.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/88FDF7EA-4C61-E211-9E7F-001D09F24D8A.root',
'/store/express/HIRun2013/ExpressPhysics/FEVT/Express-v1/000/210/353/00000/A80F7647-4F61-E211-90DF-BCAEC532971C.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM100.HLTPaths = ['HLT_PAPixelTracks_Multiplicity100_*']
process.hltHM100.andOr = cms.bool(True)
process.hltHM100.throw = cms.bool(False)

process.hltHF100 = process.hltHM100.clone()
process.hltHF100.HLTPaths = ['HLT_PAHFSumET100_v*']
process.hltHF140 = process.hltHM100.clone()
process.hltHF140.HLTPaths = ['HLT_PAHFSumET140_v*']
process.hltHF170 = process.hltHM100.clone()
process.hltHF170.HLTPaths = ['HLT_PAHFSumET170_v*']
process.hltHF210 = process.hltHM100.clone()
process.hltHF210.HLTPaths = ['HLT_PAHFSumET210_v*']

process.eventFilter_HF100 = cms.Sequence(
    process.hltHF100 )#*
#    process.PAcollisionEventSelection )
process.eventFilter_HF100_step = cms.Path( process.eventFilter_HF100 )
process.extraTrks_HF100_step   = cms.Path( process.eventFilter_HF100 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF140 = cms.Sequence(
    process.hltHF140 )#*
#    process.PAcollisionEventSelection )
process.eventFilter_HF140_step = cms.Path( process.eventFilter_HF140 )
process.extraTrks_HF140_step   = cms.Path( process.eventFilter_HF140 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF170 = cms.Sequence(
    process.hltHF170 )#*
#    process.PAcollisionEventSelection )
process.eventFilter_HF170_step = cms.Path( process.eventFilter_HF170 )
process.extraTrks_HF170_step   = cms.Path( process.eventFilter_HF170 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF210 = cms.Sequence(
    process.hltHF210 )#*
#    process.PAcollisionEventSelection )
process.eventFilter_HF210_step = cms.Path( process.eventFilter_HF210 )
process.extraTrks_HF210_step   = cms.Path( process.eventFilter_HF210 * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HM100 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM100'))
)
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

process.output_HF100_step = cms.EndPath(process.output_HF100)
process.output_HF140_step = cms.EndPath(process.output_HF140)
process.output_HF170_step = cms.EndPath(process.output_HF170)
process.output_HF210_step = cms.EndPath(process.output_HF210)

process.schedule = cms.Schedule(
    process.eventFilter_HF100_step,
    process.eventFilter_HF140_step,
    process.eventFilter_HF170_step,
    process.eventFilter_HF210_step,
    process.extraTrks_HF100_step,
    process.extraTrks_HF140_step,
    process.extraTrks_HF170_step,
    process.extraTrks_HF210_step,
    process.output_HF100_step,
    process.output_HF140_step,
    process.output_HF170_step,
    process.output_HF210_step
)
