import FWCore.ParameterSet.Config as cms

from FlowCorrAna.DiHadronCorrelationAnalyzer.epetadeco_cfi import *

epetadeco_ana_HI_hfp = epetadeco_ana.clone(
  TrgTrackCollection = cms.string('hiLowPtPixelTracks'),
  VertexCollection = cms.string('hiSelectedVertex'),
  GenParticleCollection = cms.string('hiGenParticles'),

  etaassmin = cms.double(3.0),
  etaassmax = cms.double(3.5),
  pttrgmin = cms.vdouble(0.3)
)

epetadeco_ana_HI_nocorr = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(-1),
  centmax = cms.int32(-1),
  IsCorr = cms.bool(False)
)

epetadeco_ana_HI_hfm = epetadeco_ana_HI_hfp.clone(
  etaassmin = cms.double(-3.5),
  etaassmax = cms.double(-3.0)
)

epetadeco_ana_HI_hfp_cent002 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(110),
  centmax = cms.int32(1000)
)

epetadeco_ana_HI_hfm_cent002 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(110),
  centmax = cms.int32(1000)
)

epetadeco_ana_HI_hfp_cent05 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(0),
  centmax = cms.int32(10)
)

epetadeco_ana_HI_hfm_cent05 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(0),
  centmax = cms.int32(10)
)

epetadeco_ana_HI_hfp_cent510 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(10),
  centmax = cms.int32(20)
)

epetadeco_ana_HI_hfm_cent510 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(10),
  centmax = cms.int32(20)
)

epetadeco_ana_HI_hfp_cent1020 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(20),
  centmax = cms.int32(40)
)

epetadeco_ana_HI_hfm_cent1020 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(20),
  centmax = cms.int32(40)
)

epetadeco_ana_HI_hfp_cent2030 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(40),
  centmax = cms.int32(60)
)

epetadeco_ana_HI_hfm_cent2030 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(40),
  centmax = cms.int32(60)
)

epetadeco_ana_HI_hfp_cent3040 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(60),
  centmax = cms.int32(80)
)

epetadeco_ana_HI_hfm_cent3040 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(60),
  centmax = cms.int32(80)
)

epetadeco_ana_HI_hfp_cent4050 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(80),
  centmax = cms.int32(100)
)

epetadeco_ana_HI_hfm_cent4050 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(80),
  centmax = cms.int32(100)
)

epetadeco_ana_HI_hfp_cent5060 = epetadeco_ana_HI_hfp.clone(
  centmin = cms.int32(100),
  centmax = cms.int32(120)
)

epetadeco_ana_HI_hfm_cent5060 = epetadeco_ana_HI_hfm.clone(
  centmin = cms.int32(100),
  centmax = cms.int32(120)
)
