import FWCore.ParameterSet.Config as cms
process = cms.Process("ANASKIM")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/cms/store/hidata/HIRun2010/HIAllPhysics/RECO/SDmaker_3SD_1CS_PDHIAllPhysicsZSv2_SD_JetHI-v1/0000/A8934EC1-904B-E011-862C-003048F17528.root'
)
)

# =============== Other Statements =====================

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_R_39X_V6B::All'

# =============== Import Sequences =====================
process.load("HeavyIonsAnalysis.Configuration.collisionEventSelection_cff")
process.load("davidlw.HighPtFlow2011.HiExtraReco_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
#import HLTrigger.HLTfilters.hltHighLevel_cfi
#process.hltMinBiasHF = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
#process.hltMinBiasHF.HLTPaths = ['HLT_HIMinBiasHfOrBSC','HLT_HIJet35U','HLT_HIJet50U'] # for allphysics
#process.hltMinBiasHF.andOr = cms.bool(True)
#process.hltMinBiasHF.throw = cms.bool(False)

process.eventFilter = cms.Sequence( 
#    process.hltMinBiasHF * 
    process.collisionEventSelection 
)

process.eventFilter_step = cms.Path( process.eventFilter )
process.extraTrks_step   = cms.Path( process.eventFilter * process.hiextraTrack)
process.trackFilter_step = cms.Path( process.eventFilter * process.hiextraTrack * process.hiSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.hianalysisSkimContentFull_cff")
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('hiHighPtTrack.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('trackFilter_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('hiHighPtTrack'))
)

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.eventFilter_step,
    process.extraTrks_step,
    process.trackFilter_step,
    process.output_step
)
