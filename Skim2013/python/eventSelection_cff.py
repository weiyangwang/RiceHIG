import FWCore.ParameterSet.Config as cms

# ================ Physics Declared Bit ================
physDeclFilter = cms.EDFilter("PhysDecl",
    applyfilter = cms.untracked.bool(True),
    HLTriggerResults = cms.InputTag("TriggerResults","","HLT")
    )

# ================ L1 Filters =====================
from L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff import *
from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed
from L1Trigger.Skimmer.l1Filter_cfi import l1Filter

bptxAnd = hltLevel1GTSeed.clone(
    L1TechTriggerSeeding = cms.bool(True),
    L1SeedsLogicalExpression = cms.string('0')
    )

bscOr = hltLevel1GTSeed.clone(
    L1TechTriggerSeeding = cms.bool(True),
    L1SeedsLogicalExpression = cms.string('34 OR 40 OR 41')
    )

bscNoHalo = hltLevel1GTSeed.clone(
    L1TechTriggerSeeding = cms.bool(True),
    L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)')
    )

bsc2plus = l1Filter.clone(
    algorithms = ["L1_Bsc2Plus_BptxPlus"]
    )

bsc2minus = l1Filter.clone(
    algorithms = ["L1_Bsc2Minus_BptxMinus"]
    ) 

bscOrBptxOr = l1Filter.clone(
    algorithms = ["L1_BscMinBiasOR_BptxPlusORMinus"]
    )

ett60 = l1Filter.clone(
    algorithms = ["L1_ETT60"]
    )

# ================ HLT Filters =====================
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel

hltHIMinBiasHF = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_HIMinBiasHF','HLT_HIMinBiasHF_Core'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltJets = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_L1Jet6U','HLT_Jet15U','HLT_Jet30U','HLT_Jet50U'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltJet70 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_Jet70U'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltJet100 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_Jet100U'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_HighMult40'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltBscHighMult = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_L1Tech_BSC_HighMultiplicity'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult50v1 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity50_Loose'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult60v1 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity60_Loose'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult70v1 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity70_Loose'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult70 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity70'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult85 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity85'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult100 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity100'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult80New = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity80_*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltHighMult100New = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PixelTracks_Multiplicity100_*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltBSCMinBias = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_L1_BscMinBiasOR_BptxPlusORMinus'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltZeroBias = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_ZeroBias'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltBSCMinBiasOrZeroBias = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_L1_BscMinBiasOR_BptxPlusORMinus','HLT_ZeroBias'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltBSCMinBiasv1 = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_L1BscMinBiasORBptxPlusANDMinus_v1'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltN120150pA = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PAPixelTracks_Multiplicity100_v*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltN150185pA = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PAPixelTracks_Multiplicity100_v*','HLT_PAPixelTracks_Multiplicity130_v*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltN185220pA = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PAPixelTracks_Multiplicity100_v*','HLT_PAPixelTracks_Multiplicity130_v*','HLT_PAPixelTracks_Multiplicity160_v*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltN220260pA = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PAPixelTracks_Multiplicity100_v*','HLT_PAPixelTracks_Multiplicity130_v*','HLT_PAPixelTracks_Multiplicity160_v*','HLT_PAPixelTracks_Multiplicity190_v*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

hltN260pA = hltHighLevel.clone(
    HLTPaths = cms.vstring('HLT_PAPixelTracks_Multiplicity100_v*','HLT_PAPixelTracks_Multiplicity130_v*','HLT_PAPixelTracks_Multiplicity160_v*','HLT_PAPixelTracks_Multiplicity190_v*','HLT_PAPixelTracks_Multiplicity220_v*'),
    andOr = cms.bool(True),
    throw = cms.bool(False)
    )

# ================ Monster Event Rejection ==============
purityFractionFilter = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
    )

# ================ Vertex Filter ========================
primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    minimumNDOF = cms.uint32(4),
    maxAbsZ = cms.double(15),	
    maxd0 = cms.double(2)	
    )

oneGoodVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && tracksSize > 3 && abs(z) <= 15 && position.Rho <= 2"),
   filter = cms.bool(True)   # otherwise it won't filter the events, just produce an empty vertex collection.
)

L1NoHaloFilter = cms.Sequence(bscNoHalo)
minBiasHLTBscFilterv1 = cms.Sequence(hltBSCMinBiasv1 * physDeclFilter * bptxAnd * bscNoHalo)
minBiasOrzeroBiasHLTBscFilter = cms.Sequence(hltBSCMinBiasOrZeroBias * physDeclFilter * bscOrBptxOr * bptxAnd * bscOr * bscNoHalo)
minBiasOrzeroBiasHLTBscHaloFilter = cms.Sequence(hltBSCMinBiasOrZeroBias * physDeclFilter * bscOrBptxOr * bptxAnd * bscOr * ~bscNoHalo)
zeroBiasHLTBscFilter = cms.Sequence(hltZeroBias * physDeclFilter * bscOrBptxOr * bptxAnd * bscOr * bscNoHalo)
minBiasHLTBscFilter = cms.Sequence(hltBSCMinBias * physDeclFilter * bscOrBptxOr * bptxAnd * bscOr * bscNoHalo)
minBiasBscFilter = cms.Sequence(physDeclFilter * bscOrBptxOr * bptxAnd * bscOr * bscNoHalo)
minBiasBscFilterMC = cms.Sequence(bscOr * bscNoHalo)
minBiasBscFilterFastSimMC = cms.Sequence(bscNoHalo)
