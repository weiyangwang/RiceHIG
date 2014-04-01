import FWCore.ParameterSet.Config as cms

process = cms.Process("ANASKIM1")

#process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
                              fileNames = cms.untracked.vstring(
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_77_1_w7O.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_96_1_Qkj.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_88_1_Bqd.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_76_1_fJH.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_80_1_s5F.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_82_1_kWX.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_83_1_rii.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_86_2_IaM.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_69_1_N7L.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_20_1_ABX.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_19_1_kIt.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_21_1_kan.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_15_1_0iW.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_14_1_CJC.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_18_1_Q1d.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_24_1_G7d.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_31_1_QqG.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_16_1_Ikz.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_28_1_RGK.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_32_1_oEn.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_25_1_fZM.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_17_1_K9r.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_33_2_Vq8.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_36_1_S4n.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_35_1_Jfl.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_93_1_TaR.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_93_2_JyD.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_37_2_ZDg.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_40_1_i4B.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_22_1_Ejl.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_27_2_U6g.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_29_1_F8T.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_26_1_7zp.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_23_1_2lN.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_30_1_TFt.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_34_1_foU.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_2_1_mEE.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_10_1_6W2.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_6_1_bt0.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_39_1_2KG.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_4_2_khe.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_7_1_FxW.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_11_1_Hs1.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_5_1_uE4.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_9_1_10e.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_3_1_sjI.root',
'/store/user/davidlw/HIHighPt/PR_HighPtTrack20_TRKANASKIM_v2/fc85781cd9e6faa59252f5f110b41ada/hiHighPtTrack_8_1_Ucp.root'
),
#                              eventsToProcess = cms.untracked.VEventRange('151350:34594-151350:34594',
#                                                                          '151350:51521-151350:51521',
#                                                                          '151350:62060-151350:62060')
)

############################################################################
### Get list of files from a directory
#import os
#indir = "/mnt/hadoop/cms/store/user/vzhukova/SKIM_HIGHPT_EXPRESS_2"
#infileroot = ""
#ffrom = 1
#fto = 15
# get a list of files from a specified directory and add a specified  
#number to the list of fileNames
#mylist = os.listdir(indir)

#for i in range(ffrom,fto):
#        process.source.fileNames.append('file:%s/%s' % (indir,mylist[i]))  #add files from directory list
############################################################################

process.out = cms.OutputModule("PoolOutputModule", 
 fileName = cms.untracked.string("/net/hisrv0001/home/davidlw/scratch1/hiHighPtTrack_1.root")
)

process.p = cms.EndPath(process.out)
