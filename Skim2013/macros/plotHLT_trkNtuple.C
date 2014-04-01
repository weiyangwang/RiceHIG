#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1.h>
#include <TH2.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <iostream>

void plotHLT_trkNtuple(double ptMin=0.0)
{
   TFile* f = new TFile("/mnt/hadoop/cms/store/user/velicanu/openhlt/hiexp-hirun2011-r181611-reco-v1-collisionEvents_lowerSC_autohlt.root");
   TTree* fChain = (TTree*)f->Get("anaTrack/trackTree");
   TTree* fChain1 = (TTree*)f->Get("hltanalysis/HltTree");
   TTree* fChain2 = (TTree*)f->Get("skimanalysis/HltTree");

   // Declaration of leaf types
   Int_t           nEv;
   Int_t           nLumi;
   Int_t           nBX;
   Int_t           nRun;
   Int_t           nv;
   Float_t         vx[2];   //[nv]
   Float_t         vy[2];   //[nv]
   Float_t         vz[2];   //[nv]
   Int_t           nTrk;
   Float_t         trkPt[1610];   //[nTrk]
   Float_t         trkPtError[1610];   //[nTrk]
   Int_t           trkChg[1610];   //[nTrk]
   Int_t           trkNHit[1610];   //[nTrk]
   Int_t           trkNlayer[1610];   //[nTrk]
   Int_t           trkNlayer3D[1610];   //[nTrk]
   Float_t         trkEta[1610];   //[nTrk]
   Float_t         trkPhi[1610];   //[nTrk]
   Int_t           trkQual[1610];   //[nTrk]
   Float_t         trkChi2[1610];   //[nTrk]
   Float_t         trkChi2hit1D[1610];   //[nTrk]
   Float_t         trkNdof[1610];   //[nTrk]
   Float_t         trkDz[1610];   //[nTrk]
   Float_t         trkDzError[1610];   //[nTrk]
   Float_t         trkDzError1[1610];   //[nTrk]
   Float_t         trkDzError2[1610];   //[nTrk]
   Float_t         trkDxy[1610];   //[nTrk]
   Float_t         trkDxyBS[1610];   //[nTrk]
   Float_t         trkDxy1[1610];   //[nTrk]
   Float_t         trkDxy2[1610];   //[nTrk]
   Float_t         trkDxyError[1610];   //[nTrk]
   Float_t         trkDxyErrorBS[1610];   //[nTrk]
   Float_t         trkDxyError1[1610];   //[nTrk]
   Float_t         trkDxyError2[1610];   //[nTrk]
   Float_t         trkDz1[1610];   //[nTrk]
   Float_t         trkDz2[1610];   //[nTrk]
   Float_t         trkVx[1610];   //[nTrk]
   Float_t         trkVy[1610];   //[nTrk]
   Float_t         trkVz[1610];   //[nTrk]
   Bool_t          trkFake[1610];   //[nTrk]
   Float_t         trkAlgo[1610];   //[nTrk]

   Int_t           HLT_HIFullTrack12_L1Central_v1;
   Int_t           HLT_HIFullTrack14_L1Central_v1;
   Int_t           HLT_HIFullTrack20_L1Central_v1;
   Int_t           HLT_HIFullTrack25_L1Central_v1;
   Int_t           HLT_HIFullTrack12_L1Peripheral_v1;
   Int_t           HLT_HIFullTrack14_L1Peripheral_v1;
   Int_t           HLT_HIFullTrack20_L1Peripheral_v1;
   Int_t           HLT_HIFullTrack25_L1Peripheral_v1;
   Int_t           HLT_HIMinBiasHfOrBSC_v1;

   Int_t           pcollisionEventSelection; 

   // List of branches
   TBranch        *b_nEv;   //!
   TBranch        *b_nLumi;   //!
   TBranch        *b_nBX;   //!
   TBranch        *b_nRun;   //!
   TBranch        *b_nv;   //!
   TBranch        *b_vx;   //!
   TBranch        *b_vy;   //!
   TBranch        *b_vz;   //!
   TBranch        *b_nTrk;   //!
   TBranch        *b_trkPt;   //!
   TBranch        *b_trkPtError;   //!
   TBranch        *b_trkChg;   //!
   TBranch        *b_trkNHit;   //!
   TBranch        *b_trkNlayer;   //!
   TBranch        *b_trkNlayer3D;   //!
   TBranch        *b_trkEta;   //!
   TBranch        *b_trkPhi;   //!
   TBranch        *b_trkQual;   //!
   TBranch        *b_trkChi2;   //!
   TBranch        *b_trkChi2hit1D;   //!
   TBranch        *b_trkNdof;   //!
   TBranch        *b_trkDz;   //!
   TBranch        *b_trkDzError;   //!
   TBranch        *b_trkDzError1;   //!
   TBranch        *b_trkDzError2;   //!
   TBranch        *b_trkDxy;   //!
   TBranch        *b_trkDxyBS;   //!
   TBranch        *b_trkDxy1;   //!
   TBranch        *b_trkDxy2;   //!
   TBranch        *b_trkDxyError;   //!
   TBranch        *b_trkDxyErrorBS;   //!
   TBranch        *b_trkDxyError1;   //!
   TBranch        *b_trkDxyError2;   //!
   TBranch        *b_trkDz1;   //!
   TBranch        *b_trkDz2;   //!
   TBranch        *b_trkVx;   //!
   TBranch        *b_trkVy;   //!
   TBranch        *b_trkVz;   //!
   TBranch        *b_trkFake;   //!
   TBranch        *b_trkAlgo;   //!   

   TBranch        *b_HLT_HIFullTrack12_L1Central_v1;   //! 
   TBranch        *b_HLT_HIFullTrack14_L1Central_v1;   //!
   TBranch        *b_HLT_HIFullTrack20_L1Central_v1;   //!
   TBranch        *b_HLT_HIFullTrack25_L1Central_v1;   //!
   TBranch        *b_HLT_HIFullTrack12_L1Peripheral_v1;   //!
   TBranch        *b_HLT_HIFullTrack14_L1Peripheral_v1;   //!
   TBranch        *b_HLT_HIFullTrack20_L1Peripheral_v1;   //!
   TBranch        *b_HLT_HIFullTrack25_L1Peripheral_v1;   //!
   TBranch        *b_HLT_HIMinBiasHfOrBSC_v1;  //!
   TBranch        *b_pcollisionEventSelection; //!

   fChain->SetBranchAddress("nEv", &nEv, &b_nEv);
   fChain->SetBranchAddress("nLumi", &nLumi, &b_nLumi);
   fChain->SetBranchAddress("nBX", &nBX, &b_nBX);
   fChain->SetBranchAddress("nRun", &nRun, &b_nRun);
   fChain->SetBranchAddress("nv", &nv, &b_nv);
   fChain->SetBranchAddress("vx", vx, &b_vx);
   fChain->SetBranchAddress("vy", vy, &b_vy);
   fChain->SetBranchAddress("vz", vz, &b_vz);
   fChain->SetBranchAddress("nTrk", &nTrk, &b_nTrk);
   fChain->SetBranchAddress("trkPt", trkPt, &b_trkPt);
   fChain->SetBranchAddress("trkPtError", trkPtError, &b_trkPtError);
   fChain->SetBranchAddress("trkChg", trkChg, &b_trkChg);
   fChain->SetBranchAddress("trkNHit", trkNHit, &b_trkNHit);
   fChain->SetBranchAddress("trkNlayer", trkNlayer, &b_trkNlayer);
   fChain->SetBranchAddress("trkNlayer3D", trkNlayer3D, &b_trkNlayer3D);
   fChain->SetBranchAddress("trkEta", trkEta, &b_trkEta);
   fChain->SetBranchAddress("trkPhi", trkPhi, &b_trkPhi);
   fChain->SetBranchAddress("trkQual", trkQual, &b_trkQual);
   fChain->SetBranchAddress("trkChi2", trkChi2, &b_trkChi2);
   fChain->SetBranchAddress("trkChi2hit1D", trkChi2hit1D, &b_trkChi2hit1D);
   fChain->SetBranchAddress("trkNdof", trkNdof, &b_trkNdof);
   fChain->SetBranchAddress("trkDz", trkDz, &b_trkDz);
   fChain->SetBranchAddress("trkDzError", trkDzError, &b_trkDzError);
   fChain->SetBranchAddress("trkDzError1", trkDzError1, &b_trkDzError1);
   fChain->SetBranchAddress("trkDzError2", trkDzError2, &b_trkDzError2);
   fChain->SetBranchAddress("trkDxy", trkDxy, &b_trkDxy);
   fChain->SetBranchAddress("trkDxyBS", trkDxyBS, &b_trkDxyBS);
   fChain->SetBranchAddress("trkDxy1", trkDxy1, &b_trkDxy1);
   fChain->SetBranchAddress("trkDxy2", trkDxy2, &b_trkDxy2);
   fChain->SetBranchAddress("trkDxyError", trkDxyError, &b_trkDxyError);
   fChain->SetBranchAddress("trkDxyErrorBS", trkDxyErrorBS, &b_trkDxyErrorBS);
   fChain->SetBranchAddress("trkDxyError1", trkDxyError1, &b_trkDxyError1);
   fChain->SetBranchAddress("trkDxyError2", trkDxyError2, &b_trkDxyError2);
   fChain->SetBranchAddress("trkDz1", trkDz1, &b_trkDz1);
   fChain->SetBranchAddress("trkDz2", trkDz2, &b_trkDz2);
   fChain->SetBranchAddress("trkVx", trkVx, &b_trkVx);
   fChain->SetBranchAddress("trkVy", trkVy, &b_trkVy);
   fChain->SetBranchAddress("trkVz", trkVz, &b_trkVz);
   fChain->SetBranchAddress("trkFake", trkFake, &b_trkFake);
   fChain->SetBranchAddress("trkAlgo", trkAlgo, &b_trkAlgo);

   fChain1->SetBranchAddress("HLT_HIFullTrack12_L1Central_v1", &HLT_HIFullTrack12_L1Central_v1, &b_HLT_HIFullTrack12_L1Central_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack14_L1Central_v1", &HLT_HIFullTrack14_L1Central_v1, &b_HLT_HIFullTrack14_L1Central_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack20_L1Central_v1", &HLT_HIFullTrack20_L1Central_v1, &b_HLT_HIFullTrack20_L1Central_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack25_L1Central_v1", &HLT_HIFullTrack25_L1Central_v1, &b_HLT_HIFullTrack25_L1Central_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack12_L1Peripheral_v1", &HLT_HIFullTrack12_L1Peripheral_v1, &b_HLT_HIFullTrack12_L1Peripheral_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack14_L1Peripheral_v1", &HLT_HIFullTrack14_L1Peripheral_v1, &b_HLT_HIFullTrack14_L1Peripheral_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack20_L1Peripheral_v1", &HLT_HIFullTrack20_L1Peripheral_v1, &b_HLT_HIFullTrack20_L1Peripheral_v1);
   fChain1->SetBranchAddress("HLT_HIFullTrack25_L1Peripheral_v1", &HLT_HIFullTrack25_L1Peripheral_v1, &b_HLT_HIFullTrack25_L1Peripheral_v1);
   fChain1->SetBranchAddress("HLT_HIMinBiasHfOrBSC_v1", &HLT_HIMinBiasHfOrBSC_v1, &b_HLT_HIMinBiasHfOrBSC_v1);
   fChain2->SetBranchAddress("pcollisionEventSelection", &pcollisionEventSelection, &b_pcollisionEventSelection);

   Long64_t nentries = fChain->GetEntriesFast();
   Long64_t nbytes = 0, nb = 0;

   double PI = 3.141593;
   TH1D* hTrkPt = new TH1D("hTrkPt",";p_{T} (GeV/c)",50,0,50);
   TH1D* hTrkPtMax_minbias = new TH1D("hTrkPtMax_minbias",";p^{max}_{T} (GeV/c)",100,0,100);
   TH1D* hTrkPtMax_tracktrigger = new TH1D("hTrkPtMax_tracktrigger",";p^{max}_{T} (GeV/c)",100,0,100);
   TH2D* hTrkEtaPhi = new TH2D("hTrkEtaPhi",";#eta;#phi",100,-3.0,3.0,100,-PI,PI);
   TH1D* hTrkEta = new TH1D("hTrkEta",";#eta",40,-3.0,3.0);
   TH1D* hTrkPhi = new TH1D("hTrkPhi",";#phi",40,-PI,PI);
   TH1D* hTrkdzNorm = new TH1D("hTrkdzNorm",";d_{z}/#sigma(d_{z})",50,-5,5);
   TH1D* hTrkdxyNorm = new TH1D("hTrkdxyNorm",";d_{xy}/#sigma(d_{xy})",50,-5,5);
   TH1D* hTrkNHit = new TH1D("hTrkNHit",";NHit",20,10,30); 
   TH1D* hTrkPtError = new TH1D("hTrkPtError",";#sigma(p_{T})/p_{T}",100,0,0.06);
   TH1D* hTrkChi2Ndf = new TH1D("hTrkChi2Ndf",";#chi^{2}/NDF",50,0,3);
   TH1D* hZVtx = new TH1D("hZVtx",";z_{vtx} (cm)",150,-15,15);
   TH2D* hXYVtx = new TH2D("hXYVtx",";x_{vtx} (cm);y_{vtx} (cm)",50,-0.5,0.5,50,-0.5,0.5);

   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      fChain1->GetEntry(jentry);
      fChain2->GetEntry(jentry);

      if(!pcollisionEventSelection) continue;

      int istracktrigger = 0;
      if(HLT_HIFullTrack12_L1Central_v1 || HLT_HIFullTrack14_L1Central_v1 || HLT_HIFullTrack20_L1Central_v1 || HLT_HIFullTrack25_L1Central_v1 || HLT_HIFullTrack12_L1Peripheral_v1 || HLT_HIFullTrack14_L1Peripheral_v1 || HLT_HIFullTrack20_L1Peripheral_v1 || HLT_HIFullTrack25_L1Peripheral_v1) istracktrigger = 1;

      int isminbias = 0;
      if(HLT_HIMinBiasHfOrBSC_v1) isminbias = 1;

      if(fabs(vz[1])>15.0) continue;

      if(vz[1]) hZVtx->Fill(vz[1]);
      if(vx[1]&&vy[1]) hXYVtx->Fill(vx[1],vy[1]);
 
      double trkPtMax = 0;
      for (int iTrk = 0; iTrk<nTrk; iTrk++)
      {
        if(trkPt[iTrk] > ptMin)
        {
          hTrkdzNorm->Fill(trkDz1[iTrk]/trkDzError1[iTrk]);
          hTrkdxyNorm->Fill(trkDxy1[iTrk]/trkDxyError1[iTrk]);
          hTrkNHit->Fill(trkNHit[iTrk]);
          hTrkPtError->Fill(trkPtError[iTrk]/trkPt[iTrk]);
          hTrkChi2Ndf->Fill(trkChi2[iTrk]/trkNdof[iTrk]);
        }

//        if(abs(trkDz1[iTrk]/trkDzError1[iTrk])<4
//           && abs(trkDxy1[iTrk]/trkDxyError1[iTrk])<4
//           && trkNHit[iTrk]>=12
//           && trkPtError[iTrk]/trkPt[iTrk]<0.05)
//        {
          if(trkPt[iTrk] > trkPtMax) trkPtMax = trkPt[iTrk]; 
          hTrkPt->Fill(trkPt[iTrk]); 
          if(trkPt[iTrk] < ptMin) continue;
          hTrkEtaPhi->Fill(trkEta[iTrk],trkPhi[iTrk]);
          hTrkEta->Fill(trkEta[iTrk]); hTrkPhi->Fill(trkPhi[iTrk]);
//        }
      }
      if(istracktrigger) hTrkPtMax_tracktrigger->Fill(trkPtMax);
      if(isminbias) hTrkPtMax_minbias->Fill(trkPtMax);
   }

   hTrkPt->Scale(1.0/hZVtx->Integral());
   hTrkEtaPhi->Scale(1.0/hZVtx->Integral());
   hTrkEta->Scale(1.0/hZVtx->Integral());
   hTrkPhi->Scale(1.0/hZVtx->Integral());
   hTrkdzNorm->Scale(1.0/hZVtx->Integral());
   hTrkdxyNorm->Scale(1.0/hZVtx->Integral());
   hTrkNHit->Scale(1.0/hZVtx->Integral());
   hTrkPtError->Scale(1.0/hZVtx->Integral());
   hTrkChi2Ndf->Scale(1.0/hZVtx->Integral());
   hZVtx->Scale(1.0/hZVtx->Integral());
   hXYVtx->Scale(1.0/hXYVtx->Integral());
 
   std::cout << "Counts of high pT track events:" << std::endl;
   std::cout << "Total: "<< hTrkPtMax_tracktrigger->Integral() << std::endl;
   std::cout << "pT > 12GeV/c: "<< hTrkPtMax_tracktrigger->Integral(hTrkPtMax_tracktrigger->FindBin(12.),100000) << std::endl;
   std::cout << "pT > 14GeV/c: "<< hTrkPtMax_tracktrigger->Integral(hTrkPtMax_tracktrigger->FindBin(14.),100000) << std::endl;
   std::cout << "pT > 20GeV/c: "<< hTrkPtMax_tracktrigger->Integral(hTrkPtMax_tracktrigger->FindBin(20.),100000) << std::endl;
   std::cout << "pT > 25GeV/c: "<< hTrkPtMax_tracktrigger->Integral(hTrkPtMax_tracktrigger->FindBin(25.),100000) << std::endl;

   TFile* f1 = new TFile("/net/hisrv0001/home/davidlw/scratch1/openhlt/trackntuple_minbias_2010.root");
   TTree* fChain_2010 = (TTree*)f1->Get("anaTrack/trackTree");
   TH1D* hTrkPt_2010 = new TH1D("hTrkPt_2010",";p_{T} (GeV/c)",50,0,50);
   TH2D* hTrkEtaPhi_2010 = new TH2D("hTrkEtaPhi_2010",";#eta;#phi",100,-3.0,3.0,100,-PI,PI);
   TH1D* hTrkEta_2010 = new TH1D("hTrkEta_2010",";#eta",40,-3.0,3.0);
   TH1D* hTrkPhi_2010 = new TH1D("hTrkPhi_2010",";#phi",40,-PI,PI);
   TH1D* hTrkdzNorm_2010 = new TH1D("hTrkdzNorm_2010",";d_{z}/#sigma(d_{z})",50,-5,5);
   TH1D* hTrkdxyNorm_2010 = new TH1D("hTrkdxyNorm_2010",";d_{xy}/#sigma(d_{xy})",50,-5,5);
   TH1D* hTrkNHit_2010 = new TH1D("hTrkNHit_2010",";NHit",20,10,30);
   TH1D* hTrkPtError_2010 = new TH1D("hTrkPtError_2010",";#sigma(p_{T})/p_{T}",100,0,0.06);
   TH1D* hTrkChi2Ndf_2010 = new TH1D("hTrkChi2Ndf_2010",";#chi^{2}/NDF",50,0,3);
   TH1D* hZVtx_2010 = new TH1D("hZVtx_2010",";z_{vtx} (cm)",150,-15,15);
   TH2D* hXYVtx_2010 = new TH2D("hXYVtx_2010",";x_{vtx} (cm);y_{vtx} (cm)",50,-0.5,0.5,50,-0.5,0.5);
   fChain_2010->Draw("trkPt>>hTrkPt_2010","abs(vz[1])<15","GOFF");
   fChain_2010->Draw("trkPhi:trkEta>>hTrkEtaPhi_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkEta>>hTrkEta_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkPhi>>hTrkPhi_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkDz1/trkDzError1>>hTrkdzNorm_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkDxy1/trkDxyError1>>hTrkdxyNorm_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkNHit>>hTrkNHit_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkPtError/trkPt>>hTrkPtError_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("trkChi2/trkNdof>>hTrkChi2Ndf_2010",Form("trkPt>%.1f && abs(vz[1])<15.0",ptMin),"GOFF");
   fChain_2010->Draw("vz[1]>>hZVtx_2010","abs(vz[1])<15.0","GOFF");
   fChain_2010->Draw("vy[1]:vx[1]>>hXYVtx_2010","abs(vz[1])<15.0","GOFF");
   hTrkPt_2010->SetMarkerStyle(24);
   hTrkEtaPhi_2010->SetMarkerStyle(24);
   hTrkEta_2010->SetMarkerStyle(24);
   hTrkPhi_2010->SetMarkerStyle(24);
   hTrkdzNorm_2010->SetMarkerStyle(24);
   hTrkdxyNorm_2010->SetMarkerStyle(24);
   hTrkNHit_2010->SetMarkerStyle(24);
   hTrkPtError_2010->SetMarkerStyle(24);
   hTrkChi2Ndf_2010->SetMarkerStyle(24);
   hZVtx_2010->SetMarkerStyle(24);
   hXYVtx_2010->SetMarkerStyle(24);

   hTrkPt_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkEtaPhi_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkEta_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkPhi_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkdzNorm_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkdxyNorm_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkNHit_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkPtError_2010->Scale(1.0/hZVtx_2010->Integral());
   hTrkChi2Ndf_2010->Scale(1.0/hZVtx_2010->Integral());
   hZVtx_2010->Scale(1.0/hZVtx_2010->Integral());
   hXYVtx_2010->Scale(1.0/hXYVtx_2010->Integral());
   
   TCanvas* c = new TCanvas("c","Track Kinematic Variables",650,600);
   c->Divide(2,2);
   c->cd(1);
   c->GetPad(1)->SetLogy();
   hTrkPt_2010->Draw("PE");
   hTrkPt->Draw("PESAME");
   c->cd(2);
   hTrkEtaPhi->Draw("colz");
   c->cd(3);
   hTrkEta_2010->Draw("PE");
   hTrkEta->Draw("PESAME");
   c->cd(4);
   hTrkPhi_2010->SetAxisRange(0,hTrkPhi_2010->GetMaximum()*1.5,"Y");
   hTrkPhi_2010->Draw("PE");
   hTrkPhi->Draw("PESAME");

   TCanvas* c0 = new TCanvas("c0","Event Vertex",650,300);
   c0->Divide(2,1);
   c0->cd(1);
   hZVtx_2010->Draw("PE");
   hZVtx->Draw("PESAME");
   c0->cd(2);
   hXYVtx->Draw("colz");

   TCanvas* c1 = new TCanvas("c1","Track Quality Variables",850,500);
   c1->Divide(3,2);
   c1->cd(1);
   hTrkdzNorm_2010->Draw("PE");
   hTrkdzNorm->Draw("PESAME");
   c1->cd(2);
   hTrkdxyNorm_2010->Draw("PE");
   hTrkdxyNorm->Draw("PESAME");
   c1->cd(3);
   hTrkNHit_2010->Draw("PE");
   hTrkNHit->Draw("PESAME");
   c1->cd(4);
   c1->GetPad(4)->SetLogy();
   hTrkPtError_2010->Draw("PE");
   hTrkPtError->Draw("PESAME");
   c1->cd(5);
   hTrkChi2Ndf_2010->Draw("PE");
   hTrkChi2Ndf->Draw("PESAME");

   TCanvas* c2 = new TCanvas("c2","Leading Track Pt",450,450);
   c2->SetLogy();
   hTrkPtMax_minbias->SetAxisRange(1.1,32,"X");
   hTrkPtMax_minbias->SetMarkerStyle(25);
   hTrkPtMax_minbias->SetMarkerSize(1.2);
   hTrkPtMax_minbias->Draw("PE");
   hTrkPtMax_tracktrigger->SetMarkerColor(kRed);
   hTrkPtMax_tracktrigger->Draw("PESAME");
   TLegend* legend = new TLegend(0.5,0.7,0.9,0.8);
   legend->SetFillColor(0);
   legend->SetTextFont(62);
   legend->AddEntry(hTrkPtMax_minbias,"HLT_HIMinBiasHfOrBSC_v1","P");
   legend->AddEntry(hTrkPtMax_tracktrigger,"HLT_HIFullTrackXX_L1XXX_v1","P");
   legend->Draw("same");

   SaveCanvas(c,"HI/tracking","trackpt10_kinematics_20102011");
   SaveCanvas(c0,"HI/tracking","trackpt10_vertex_20102011");
   SaveCanvas(c1,"HI/tracking","trackpt10_quality_20102011");
   SaveCanvas(c2,"HI/tracking","trackpt10_leadpt");
}
