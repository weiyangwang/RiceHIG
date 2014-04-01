edmConfigFromDB --cff --configName /dev/CMSSW_4_4_2/HIon --nopaths > ../test/setup_cff.py
hltGetConfiguration --offline --full --data --unprescale /users/davidlw/HLT_HIon_HighpT_MasterTable --process HLT1 > ../test/HLT_HighpT_RAW2011_cfg.py
hltGetConfiguration --offline --full --data --unprescale /users/davidlw/HLT_HIon_UCC_MasterTable --process HLT1 > ../test/HLT_UCC_RAW2011_cfg.py
