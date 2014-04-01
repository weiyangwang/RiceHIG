import FWCore.ParameterSet.Config as cms

process = cms.Process("Reconstruction")

process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Mixing")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Simulation_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")

# Tracker local reco
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")

# Beamspot
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
process.load("RecoPixelVertexing.PixelLowPtUtilities.MinBiasTracking_cff")

# Simulation
process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")

###############################################################################
# Source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    skipEvents = cms.untracked.uint32(0),
    fileNames  = cms.untracked.vstring()
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

###############################################################################
# Agglomerative vertexing
import UserCode.FerencSiklerVertexing.NewVertexProducer_cfi

process.allVertices = UserCode.FerencSiklerVertexing.NewVertexProducer_cfi.newVertices.clone()
process.allVertices.TrackCollection = 'allTracks'
process.allVertices.PtMin  = cms.double(0.1)

###############################################################################
# V0
process.pixelVZeros.trackCollection  = cms.InputTag("allTracks")
process.pixelVZeros.vertexCollection = cms.InputTag("allVertices")

# FIXME
process.pixelVZeros.minImpactPositiveDaughter = cms.double(0.2)
process.pixelVZeros.minImpactNegativeDaughter = cms.double(0.2)

###############################################################################
# Track associator
process.TrackAssociatorByHits.SimToRecoDenominator = 'reco'

process.TrackAssociatorByHits.Quality_SimToReco = cms.double(0.5)
process.TrackAssociatorByHits.Purity_SimToReco  = cms.double(0.5)
process.TrackAssociatorByHits.Cut_RecoToSim     = cms.double(0.5)

process.TrackAssociatorByHits.associatePixel    = cms.bool(True)
process.TrackAssociatorByHits.associateStrip    = cms.bool(False)

###############################################################################
# Track analyzer
process.analyzeTracks = cms.EDAnalyzer("HadronAnalyzer",
    hasSimInfo             = cms.bool(False),
    addClusterShapes       = cms.bool(False),
    pixelVertices          = cms.string('pixel3Vertices'),
    allVertices            = cms.string('allVertices'),
    allTracks              = cms.string('allTracks')
)

###############################################################################
# Event plotter
process.plotEvent = cms.EDAnalyzer("HadronPlotter",
    hasSimInfo             = cms.bool(False),
    trackProducer          = cms.string('allTracks')
)

###############################################################################
# Message logger
process.MessageLogger = cms.Service("MessageLogger",
    categories = cms.untracked.vstring(
    ),
    debugModules = cms.untracked.vstring('*'),
    cerr = cms.untracked.PSet(
        threshold = cms.untracked.string('DEBUG'),
        DEBUG = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        )
    ),
    destinations = cms.untracked.vstring('cerr'),
    suppressDebug   = cms.untracked.vstring('primTrackCandidates'),
    suppressInfo    = cms.untracked.vstring('primTrackCandidates'),
    suppressWarning = cms.untracked.vstring('primTrackCandidates')
)

###############################################################################
# Source
process.source.fileNames = cms.untracked.vstring(
#  'file:/afs/cern.ch/work/s/sikler/group/044CA650-26FF-E111-9E4C-003048D2BDD8.root' 
   'file:/afs/cern.ch/user/s/sikler/public/DE267F07-3EFD-E111-ADCF-001D09F28D4A.root'
)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(20)
)
process.source.skipEvents = cms.untracked.uint32(0)

###############################################################################
# Clusters
process.analyzeTracks.addClusterShapes = cms.bool(True)

###############################################################################
# Filters
process.load('HLTrigger.special.hltPhysicsDeclared_cfi')
process.hltPhysicsDeclared.L1GtReadoutRecordTag = 'gtDigis'

## Selection of at least a two-track fitted vertex
#primaryVertexFilter = cms.EDFilter("VertexSelector",
#    src = cms.InputTag("hiSelectedVertex"),
#    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"), 
#    filter = cms.bool(True),   # otherwise it won't filter the events
#)

# Cluster-shape filter re-run offline
#from RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi import *
#from HLTrigger.special.hltPixelClusterShapeFilter_cfi import *
import HLTrigger.special.hltPixelClusterShapeFilter_cfi

process.hltPixelClusterShapeFilter = HLTrigger.special.hltPixelClusterShapeFilter_cfi.hltPixelClusterShapeFilter.clone()
process.hltPixelClusterShapeFilter.inputTag = "siPixelRecHits"

###############################################################################
# Paths
process.reco = cms.Path(process.hltPhysicsDeclared
                      * process.siPixelRecHits
                      * process.hltPixelClusterShapeFilter
                      * process.siStripMatchedRecHits
                      * process.minBiasTracking
                      * process.allVertices
                      * process.pixelVZeros
                      * process.analyzeTracks)

###############################################################################
# Global tag
process.GlobalTag.globaltag = 'GR_E_V31::All'

###############################################################################
# Schedule
process.schedule = cms.Schedule(process.reco)

