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
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/E40EBDE1-1C63-E211-9534-003048D2C174.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/CA696CE5-1463-E211-9516-003048D2BF1C.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/98C44115-2363-E211-9AC3-BCAEC518FF63.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/34DCE00B-1663-E211-B26A-0025901D626C.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/FAC5DF87-1363-E211-A1D0-001D09F2910A.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/2EDB81E8-1263-E211-8B00-003048CFB40C.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/C8D68DB6-1163-E211-AE57-BCAEC518FF44.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/FE9808F1-1863-E211-B1E3-003048D2BC30.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/30C8776A-1A63-E211-B59D-001D09F253D4.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/B422720E-1663-E211-AD41-0025901D5D90.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/143B2EC3-2263-E211-A625-003048D2C01A.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/786B32A4-1763-E211-B994-001D09F28EA3.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/90C97669-1A63-E211-9165-001D09F29321.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/38895B72-1563-E211-B992-0025901D62A0.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/CE834B7B-1863-E211-AAFB-5404A638868F.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/ACC49F8C-1B63-E211-9711-001D09F24DA8.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/727B4DAB-1363-E211-818A-5404A63886B0.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/0850C6D9-1A63-E211-B905-001D09F23F2A.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/D076CD91-1763-E211-BDA1-001D09F2462D.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/28CF142A-1463-E211-B9BA-001D09F2441B.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/38458062-1263-E211-873B-5404A638868F.root',
'/store/hidata/HIRun2013/PAHighPt/RAW/v1/000/210/498/00000/AC1E5B44-1C63-E211-81AF-001D09F23F2A.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(2000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM100.HLTPaths = ['HLT_PAPixelTracks_Multiplicity100_*']
process.hltHM100.andOr = cms.bool(True)
process.hltHM100.throw = cms.bool(False)

process.eventFilter_HM100 = cms.Sequence(
    process.hltHM100 )
process.eventFilter_HM100_step = cms.Path( process.eventFilter_HM100 )

process.output_HM100 = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('pPb_HM100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM100'))
)

process.output_HM100_step = cms.EndPath(process.output_HM100)

process.schedule = cms.Schedule(
    process.eventFilter_HM100_step,
    process.output_HM100_step,
)
