import FWCore.ParameterSet.Config as cms

hiGoodTightTracks = cms.EDFilter("TrackSelector",
    src = cms.InputTag("hiSelectedTracks"),
    cut = cms.string('quality("highPurity")')
)

hiGoodTightTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hiGoodTightTracks" ),
    particleType = cms.string( "pi+" )
)       

hiSingleTrackFilter20 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( "hiSelectedVertex" ),
    trackCollection = cms.InputTag( "hiGoodTightTrackCands" ),
    MinPt = cms.double( 20.0 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.4 ),
    MaxVz = cms.double( 15.0 ),
    MinTrks = cms.int32( 1 ),
    MinSep = cms.double( 1 )
)     

hiSingleTrackFilter12 = hiSingleTrackFilter20.clone( 
    MinPt = cms.double( 12.0 )
)

hiSingleTrackFilter14 = hiSingleTrackFilter20.clone(
    MinPt = cms.double( 14.0 )
)

hiGoodTightTrackSequence = cms.Sequence(
                                         hiGoodTightTracks
                                       * hiGoodTightTrackCands 
                                       )
hiSingleTrackFilterSequence20 = cms.Sequence(
                                         hiGoodTightTrackSequence
                                       * hiSingleTrackFilter20
                                       )
hiSingleTrackFilterSequence14 = cms.Sequence(
                                         hiGoodTightTrackSequence
                                       * hiSingleTrackFilter14
                                       )
hiSingleTrackFilterSequence12 = cms.Sequence(
                                         hiGoodTightTrackSequence
                                       * hiSingleTrackFilter12
                                       )
