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
'/store/hidata/HIRun2011/HIHighPt/RECO/PromptReco-v1/000/182/591/52A4830E-051C-E111-B58F-BCAEC532971C.root'
   )
)

process.load("davidlw.HighPtFlow2011.HiExtraReco_cff")
process.load("FirstHi2011.PbPbSpectraAna.HiExtraReco_cff")
process.hiPreCaloCompTracks.srcTracks = cms.InputTag("hiSelectedTracks")
process.hiPreCaloCompTracks.copyTrajectories = cms.untracked.bool(False)
process.hiPreCaloCompTracks.copyExtras = cms.untracked.bool(False)
process.hiPreOptimalTightTracks.copyTrajectories = cms.untracked.bool(False)
process.hiPreOptimalTightTracks.copyExtras = cms.untracked.bool(False)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(500))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'GR_R_44_V10::All' # GR_E_V22::All for express stream

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHIHighPtTrack = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHIHighPtTrack.HLTPaths = ['HLT_HIFullTrack20_*','HLT_HIFullTrack25_*'] # for allphysics
process.hltHIHighPtTrack.andOr = cms.bool(True)
process.hltHIHighPtTrack.throw = cms.bool(False)

process.eventFilter = cms.Sequence (process.collisionEventSelection * process.hltHIHighPtTrack)
process.eventFilter_step = cms.Path( process.eventFilter )
process.trackFilter_step = cms.Path( process.eventFilter * process.hiGoodTightTracks * process.hiOptTrack)

process.load("davidlw.HighPtFlow2011.hianalysisSkimContentFull_cff")
process.output = cms.OutputModule("PoolOutputModule",
   outputCommands = process.analysisSkimContent.outputCommands,
   fileName = cms.untracked.string('hiHighPtTrack.root'),
#   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('trackFilter_step')),
   SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_step')),
   dataset = cms.untracked.PSet(
     dataTier = cms.untracked.string('AOD'),
     filterName = cms.untracked.string('hiHighPtTrack'))
)
process.output.outputCommands.append('keep *recoTracks_hiSelectedTracks_*_*')
process.output.outputCommands.append('keep *recoTracks_hiOptimalTightTracks_*_*')
#process.output.outputCommands.append('keep *')

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
   process.eventFilter_step,
   process.trackFilter_step,
   process.output_step
)
