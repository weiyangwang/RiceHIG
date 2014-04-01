edmConfigFromDB --cff --configName /dev/CMSSW_4_4_2/HIon --nopaths > ../test/setup_cff.py
hltGetConfiguration --offline --full --data --unprescale --l1-emulator gct,gt --l1 L1GtTriggerMenu_L1Menu_CollisionsHeavyIons2011_v0_mc /users/davidlw/HLT_HIon_HighpT_MasterTable --globaltag START44_V6::All --process HLT1 > ../test/HLT_HighpT_RAW2010_cfg.py
hltGetConfiguration --offline --full --data --unprescale --l1-emulator gct,gt --l1 L1GtTriggerMenu_L1Menu_CollisionsHeavyIons2011_v0_mc /users/davidlw/HLT_HIon_UCC_MasterTable --globaltag START44_V6::All --process HLT1 > ../test/HLT_UCC_RAW2010_cfg.py
