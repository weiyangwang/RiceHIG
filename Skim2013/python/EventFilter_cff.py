import FWCore.ParameterSet.Config as cms
from RiceHIG.Skim2013.eventSelection_cff import *
from RiceHIG.Skim2013.ppExtraReco_cff import *

nTrkOffFilter120150Sequence = cms.Sequence(
                            hltN120150pA *
                            nTrkOffTracks *
                            nTrkOffFilter120 *
                            ~nTrkOffFilter150
                          )

nTrkOffFilter150185Sequence = cms.Sequence(
                            hltN150185pA *
                            nTrkOffTracks *
                            nTrkOffFilter150 *
                            ~nTrkOffFilter185
                          )

nTrkOffFilter185220Sequence = cms.Sequence(
                            hltN185220pA *
                            nTrkOffTracks *
                            nTrkOffFilter185 *
                            ~nTrkOffFilter220
                          )

nTrkOffFilter220260Sequence = cms.Sequence(
                            hltN220260pA *
                            nTrkOffTracks *
                            nTrkOffFilter220 *
                            ~nTrkOffFilter260
                          )

nTrkOffFilter260300Sequence = cms.Sequence(
                            hltN260pA *
                            nTrkOffTracks *
                            nTrkOffFilter260 *
                            ~nTrkOffFilter300
                          )
