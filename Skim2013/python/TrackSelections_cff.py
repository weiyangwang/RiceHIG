import FWCore.ParameterSet.Config as cms

###
### select high-purity tracks
###

highPurityTracks = cms.EDFilter("TrackSelector",
    src = cms.InputTag("generalTracks"),
    cut = cms.string('quality("highPurity") && (ptError/pt<0.1) && (pt>0.1) && (abs(eta)<2.4)')
)

selectTracks = cms.EDProducer("AnalyticalTrackSelector",
    src = cms.InputTag("highPurityTracks"),
    keepAllTracks = cms.bool(False), ## if set to true tracks failing this filter are kept in the output
    beamspot = cms.InputTag("offlineBeamSpot"),

    # vertex selection 
    useVertices = cms.bool(True),
    useVtxError = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    vtxNumber = cms.int32(1),
    vertexCut = cms.string('!isFake && ndof>=2 && abs(z)<=15.0 && abs(position.rho)<=2.0'),

    #untracked bool copyTrajectories = true // when doing retracking before
    copyTrajectories = cms.untracked.bool(False),
    copyExtras = cms.untracked.bool(False), ## set to false on AOD
    qualityBit = cms.string(''), ## set to '' or comment out if you don't want to set the bit

    # parameters for adapted optimal cuts on chi2 and primary vertex compatibility
    chi2n_par = cms.double(9999.0),
    chi2n_no1Dmod_par = cms.double(9999.0),
    res_par = cms.vdouble(99999.0, 99999.0),
    d0_par1 = cms.vdouble(9999.0, 0.0),
    dz_par1 = cms.vdouble(9999.0, 0.0),
    d0_par2 = cms.vdouble(3.0, 0.0),
    dz_par2 = cms.vdouble(3.0, 0.0),
    # Boolean indicating if adapted primary vertex compatibility cuts are to be applied.
    applyAdaptedPVCuts = cms.bool(True),

    # Impact parameter absolute cuts.
    max_d0 = cms.double(100.),
    max_z0 = cms.double(100.),
    nSigmaZ = cms.double(100),

    # Cuts on numbers of layers with hits/3D hits/lost hits. 
    minNumberLayers = cms.uint32(0),
    minNumber3DLayers = cms.uint32(0),
    maxNumberLostLayers = cms.uint32(999),                                

    # Absolute cuts in case of no PV. If yes, please define also max_d0NoPV and max_z0NoPV 
    applyAbsCutsIfNoPV = cms.bool(True),
    max_d0NoPV = cms.double(100.),
    max_z0NoPV = cms.double(100.),

    # parameters for cutting on pterror/pt and number of valid hits
    max_relpterr = cms.double(9999.),
    min_nhits = cms.uint32(0)
)

chargedCandidates = cms.Sequence(highPurityTracks+selectTracks)
