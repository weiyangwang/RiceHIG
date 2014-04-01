import FWCore.ParameterSet.Config as cms

process = cms.Process("ANASKIM")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.load("Configuration.StandardSequences.ReconstructionHeavyIons_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
       # 'file:/net/hisrv0001/home/davidlw/scratch1/rereco_441.root'
'/store/express/HIRun2011/HIExpressPhysics/FEVT/Express-v1/000/181/530/06D2DB74-FB0C-E111-9E11-E0CB4E4408C4.root'
   )
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'GR_R_44_V10::All' # GR_E_V22::All for express stream

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHIMinBias = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHIMinBias.HLTPaths = ['HLT_HIMinBiasHfOrBSC_*'] # for allphysics
process.hltHIMinBias.andOr = cms.bool(True)
process.hltHIMinBias.throw = cms.bool(False)

process.load("davidlw.HighPtFlow2011.HiExtraReco_cff")
process.eventFilter = cms.Sequence (process.collisionEventSelection * process.hltHIMinBias)
process.eventFilter_step = cms.Path( process.eventFilter )
process.trackExtraReco_step = cms.Path( process.eventFilter * process.hiGoodTightTrackSequence )

process.load("davidlw.HighPtFlow2011.hianalysisSkimContentFull_cff")
process.output = cms.OutputModule("PoolOutputModule",
   outputCommands = process.analysisSkimContent.outputCommands,
   fileName = cms.untracked.string('hiGoodColl.root'),
   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('trackExtraReco_step')),
   dataset = cms.untracked.PSet(
     dataTier = cms.untracked.string('AOD'),
     filterName = cms.untracked.string('hiGoodColl'))
)

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
   process.eventFilter_step,
   process.trackExtraReco_step,
   process.output_step
)
