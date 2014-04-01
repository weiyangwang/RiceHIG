import FWCore.ParameterSet.Config as cms
process = cms.Process("RAWSKIM")

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
'/store/hidata/data/PARun2012/PAPhysics/RECO/PromptReco-v2/000/202/654/A404793B-6BFE-E111-92DD-001D09F24DA8.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMinBiasHF = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMinBiasHF.HLTPaths = ['HLT_PAZeroBiasPixel_SingleTrack_*']
process.hltMinBiasHF.andOr = cms.bool(True)
process.hltMinBiasHF.throw = cms.bool(False)

process.eventFilter = cms.Sequence( 
    process.hltMinBiasHF
)

process.eventFilter_step = cms.Path( process.eventFilter )

process.output = cms.OutputModule("PoolOutputModule",
#    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPbRAW.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('RAW'),
      filterName = cms.untracked.string('pPbRAW'))
)

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.eventFilter_step,
    process.output_step
)
