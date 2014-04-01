import FWCore.ParameterSet.Config as cms

process = cms.Process("EnergyLoss")

process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Mixing")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')

# Tracker local reco
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")

# Refitter
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

###############################################################################
# Message logger
process.MessageLogger = cms.Service("MessageLogger",
    categories = cms.untracked.vstring(
      'TrackRefitter','refitterForDeDx','energyLossProducer','EnergyLossProducer'
    ),
    debugModules = cms.untracked.vstring('*'),
    cerr = cms.untracked.PSet(
        threshold = cms.untracked.string('DEBUG'),
        DEBUG = cms.untracked.PSet(
            limit = cms.untracked.int32(1000000000)
        )
    ),
    destinations = cms.untracked.vstring('cerr')
)

###############################################################################
# Source
process.source = cms.Source("PoolSource",
  skipEvents = cms.untracked.uint32(0),
  fileNames  = cms.untracked.vstring(
    '/store/hidata/HIRun2013A/PAHighPt/RECO/PromptReco-v1/000/210/634/FA4E6B7E-7366-E211-8DD0-0019B9F581C9.root'
#   'root://eoscms//eos/cms/store/hidata/express/PARun2012/ExpressPhysics/FEVT/Express-v1/000/202/792/000A5629-45FD-E111-8FFF-BCAEC5329719.root'
  )
)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10)
)

###############################################################################
# Track refitter
from RecoTracker.TrackProducer.TrackRefitter_cfi import *

process.refitterForDeDx     = TrackRefitter.clone()
process.refitterForDeDx.src = 'generalTracks'

###############################################################################
# Energy Loss
process.energyLossProducer = cms.EDProducer("EnergyLossProducer",
    trackProducer          = cms.string('refitterForDeDx'),
    trajectoryProducer     = cms.string('refitterForDeDx')
)

process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM.HLTPaths = ['HLT_*PixelTracks_Multiplicity*_v*']
process.hltHM.andOr = cms.bool(True)
process.hltHM.throw = cms.bool(False)

process.eventFilter_HM = cms.Sequence(
    process.hltHM *
    process.PAcollisionEventSelection 
#   process.pAHighMultiplicityPileUpFilter_2Sigma_mode1
)
process.eventFilter_HM_step = cms.Path( process.eventFilter_HM )
process.extraTrks_HM_step   = cms.Path( process.eventFilter_HM * process.ppSingleTrackFilterSequence )

process.dEdx = cms.Path(process.eventFilter_HM * process.refitterForDeDx *
                        process.energyLossProducer)

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HM = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM'))
)
process.output_HM_step = cms.EndPath(process.output_HM)

###############################################################################
# Global tag
process.GlobalTag.globaltag = 'GR_P_V41::All'

###############################################################################
# Schedule
process.schedule = cms.Schedule(
    process.eventFilter_HM_step,
    process.extraTrks_HM_step,
    process.dEdx,
    process.output_HM_step
)
