import FWCore.ParameterSet.Config as cms

from RiceHIG.V0Analysis.v0selector_cfi import *
selectV0CandidatesNew_kshort = selectV0CandidatesNew.clone()
selectV0CandidatesNew_lambda = selectV0CandidatesNew.clone(v0IDName = cms.string("Lambda"))
