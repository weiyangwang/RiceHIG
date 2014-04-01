void L1_ETT()
{
  TFile* f1 = new TFile("/mnt/hadoop/cms/store/user/velicanu/openhlt/hiexp-hirun2011-r181611-reco-v1-collisionEvents_lowerSC_autohlt.root");
  TFile* f2 = new TFile("/mnt/hadoop/cms/store/user/velicanu/openhlt/hiexp-hirun2011-r181693-reco-v1-collisionEvents_lowerSC_autohlt.root");
  TFile* f = new TFile("/net/hisrv0001/home/davidlw/scratch1/hiexp-hirun2011-r181532-reco-v1-collisionEvents_lowerSC_1.root");
  TFile* f3 = new TFile("/net/hisrv0001/home/davidlw/scratch1/3000Hz.root");

  TTree* tr1 = (TTree*)f1->Get("skimanalysis/HltTree");
  TTree* tr2 = (TTree*)f2->Get("skimanalysis/HltTree");
  TTree* tr = (TTree*)f->Get("hltana/HltTree");
  TTree* tr3 = (TTree*)f3->Get("skimanalysis/HltTree");

  TH1D* h = new TH1D("h",";L1_ETT (GeV)",2200,0,2200);
  TH1D* h1 = new TH1D("h1",";L1_ETT (GeV)",2200,0,2200);
  TH1D* h2 = new TH1D("h2",";L1_ETT (GeV)",2200,0,2200);
  TH1D* h3 = new TH1D("h3",";L1_ETT (GeV)",2200,0,2200);

/*
  tr->Draw("L1EtTot>>h","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
  tr1->Draw("L1EtTot>>h1","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
  tr2->Draw("L1EtTot>>h2","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
  tr3->Draw("L1EtTot>>h3","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
*/

  tr2->Draw("L1EtTot>>h2","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND && pcollisionEventSelection","GOFF");
  tr1->Draw("L1EtTot>>h1","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND && pcollisionEventSelection","GOFF");
  tr->Draw("L1EtTot>>h","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
  tr3->Draw("L1EtTot>>h3","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND && pcollisionEventSelection","GOFF");

/*
  tr2->Draw("L1EtTot>>h2","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND","GOFF");
  tr1->Draw("L1EtTot>>h1","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND","GOFF");
  tr->Draw("L1EtTot>>h","HLT_HIMinBiasHfOrBSC_v1==1","GOFF");
  tr3->Draw("L1EtTot>>h3","L1_HcalHfCoincPmORBscMinBiasThresh1_BptxAND","GOFF");
*/
  h->Scale(1.0/h->Integral());
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());

  TCanvas* c = new TCanvas("c","",500,500);
  c->SetLogy();
  h->SetMarkerColor(kRed);
  h1->SetMarkerColor(kBlue);
  h2->SetMarkerColor(kGreen);
  h->Draw("PE");
  h1->Draw("PESAME");
  h2->Draw("PESAME");
  h3->Draw("PESAME");
  TLegend* legend = new TLegend(0.4,0.7,0.8,0.9);
  legend->SetTextFont(62);
  legend->SetFillColor(0);
  legend->AddEntry(h,"Run 181532","P");
  legend->AddEntry(h1,"Run 181611","P");
  legend->AddEntry(h2,"Run 181693","P");
  legend->AddEntry(h3,"Run 181759-181783","P");
  legend->Draw("same");

  TLatex* latex = new TLatex();
  latex->SetNDC();
  latex->DrawLatex(0.25,0.25,"HLT_HIMinBiasHfOrBSC_v1");
//  latex->DrawLatex(0.25,0.2,"&& collisionEventSelection");

  cout<<"Run 181532: "<<h->Integral(101,10000)<<" "<<h->Integral(2001,10000)<<endl;
  cout<<"Run 181611: "<<h1->Integral(101,10000)<<" "<<h1->Integral(2001,10000)<<endl;
  cout<<"Run 181693: "<<h2->Integral(101,10000)<<" "<<h2->Integral(2001,10000)<<endl;
  cout<<"Run 181759-181783: "<<h3->Integral(101,10000)<<" "<<h3->Integral(2001,10000)<<endl;
}

void strangeL1()
{
   TFile* f = new TFile("/mnt/hadoop/cms/store/user/davidlw/hiForest_181969.root");
   TTree* tr = f->Get("hltanalysis/HltTree");  

   TH1D* h_total = new TH1D("h_total",";L1_ETT (GeV)",30,0,150);
   TH1D* h_coll = new TH1D("h_coll",";L1_ETT (GeV)",30,0,150);
   TH1D* h_noncoll = new TH1D("h_noncoll",";L1_ETT (GeV)",30,0,150);
   TH2D* hl1jet_etaphi_coll = new TH2D("hl1jet_etaphi_coll",";#eta;#phi",64,-3.2,3.2,64,-3.2,3.2);
   TH2D* hl1jet_etaphi_noncoll = new TH2D("hl1jet_etaphi_noncoll",";#eta;#phi",64,-3.2,3.2,64,-3.2,3.2);

   tr->Draw("L1EtTot>>h_total","HLT_HIL1CaloMonitor_v1","GOFF");
   tr->AddFriend("skimTree=skimanalysis/HltTree");
   tr->Draw("L1EtTot>>h_coll","HLT_HIL1CaloMonitor_v1&&skimTree.pcollisionEventSelection","GOFF");
   tr->Draw("L1EtTot>>h_noncoll","HLT_HIL1CaloMonitor_v1&&!skimTree.pcollisionEventSelection","GOFF");
   tr->Draw("L1CenJetEta:L1CenJetPhi>>hl1jet_etaphi_noncoll","HLT_HIL1CaloMonitor_v1&&!skimTree.pcollisionEventSelection","GOFF"); 
   tr->Draw("L1CenJetEta:L1CenJetPhi>>hl1jet_etaphi_coll","HLT_HIL1CaloMonitor_v1&&skimTree.pcollisionEventSelection","GOFF");

   TCanvas* c0 = new TCanvas("c0","",550,500);
   hl1jet_etaphi_coll->Draw("colz");

   TCanvas* c1 = new TCanvas("c1","",550,500);
   hl1jet_etaphi_noncoll->Draw("colz");

   TCanvas* c = new TCanvas("c","",550,500);
   h_coll->SetMarkerColor(kBlue);
   h_noncoll->SetMarkerColor(kRed);
   h_total->Draw("PE");
   h_coll->Draw("PESAME");
   h_noncoll->Draw("PESAME");

   TLegend* l = new TLegend(0.45,0.75,0.9,0.9);
   l->SetTextFont(62);
   l->SetFillColor(0);
   l->AddEntry(h_total,"HLT_HIL1CaloMonitor_v1","P");
   l->AddEntry(h_coll,"HLT_HIL1CaloMonitor_v1, collision","P");
   l->AddEntry(h_noncoll,"HLT_HIL1CaloMonitor_v1, non-collision","P");   
   l->Draw();
}
