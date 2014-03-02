void eff_HI()
{
  TFile* f[10];
  f[0] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0AnalyzerNT_HICent2540_v7.root");
//  f[1] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0validation_match06_v4.root");
//  f[2] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0validation_match05_v4.root");

  TH1D* kspt_num[10];
  TH1D* kspt_denom[10];
  TH1D* lapt_num[10];
  TH1D* lapt_denom[10];

  TH2D* ksetapt_num[10];
  TH2D* ksetapt_denom[10];
  TH2D* laetapt_num[10];
  TH2D* laetapt_denom[10];

  for(int i=0;i<1;i++)
  {
    kspt_num[i] = (TH1D*)f[i]->Get("v0ValidatorHI/K0sEffVsPt_num");
    kspt_denom[i] = (TH1D*)f[i]->Get("v0ValidatorHI/K0sEffVsPt_denom");
    kspt_num[i]->SetMarkerColor(i+1);
    kspt_denom[i]->SetMarkerColor(i+1);

    lapt_num[i] = (TH1D*)f[i]->Get("v0ValidatorHI/LamEffVsPt_num");
    lapt_denom[i] = (TH1D*)f[i]->Get("v0ValidatorHI/LamEffVsPt_denom");
    lapt_num[i]->SetMarkerColor(i+1);
    lapt_denom[i]->SetMarkerColor(i+1);

    kspt_num[i]->Divide(kspt_denom[i]);
    lapt_num[i]->Divide(lapt_denom[i]);

    ksetapt_num[i] = (TH2D*)f[i]->Get("v0ValidatorHI/K0sEffVsEtaPt_num");
    ksetapt_denom[i] = (TH2D*)f[i]->Get("v0ValidatorHI/K0sEffVsEtaPt_denom");
    ksetapt_num[i]->SetMarkerColor(i+1);
    ksetapt_denom[i]->SetMarkerColor(i+1);

    laetapt_num[i] = (TH2D*)f[i]->Get("v0ValidatorHI/LamEffVsEtaPt_num");
    laetapt_denom[i] = (TH2D*)f[i]->Get("v0ValidatorHI/LamEffVsEtaPt_denom");
    laetapt_num[i]->SetMarkerColor(i+1);
    laetapt_denom[i]->SetMarkerColor(i+1);

    ksetapt_num[i]->Divide(ksetapt_denom[i]);
    laetapt_num[i]->Divide(laetapt_denom[i]);
  }

  TCanvas* c = new TCanvas("c","c",600,500);
  kspt_num[0]->SetAxisRange(0.,12,"X");
  kspt_num[0]->Draw("PE");

  TCanvas* c1 = new TCanvas("c1","c1",600,500);
  lapt_num[0]->SetAxisRange(0.,12,"X");
  lapt_num[0]->Draw("PE");

  TCanvas* c2 = new TCanvas("c2","c2",600,500);
  ksetapt_num[0]->Draw("lego2"); 

  TCanvas* c3 = new TCanvas("c3","c3",600,500);
  laetapt_num[0]->Draw("lego2"); 
/*
  SaveCanvas(c,"HI/V0","KsEffvsPt");
  SaveCanvas(c1,"HI/V0","LamEffvsPt");
  SaveCanvas(c2,"HI/V0","KsEffvsEtaPt");
  SaveCanvas(c3,"HI/V0","LamEffvsEtaPt");

  TFile* fout = new TFile("V0Eff_matching.root","recreate");
  kspt_num[2]->Write();
  lapt_num[2]->Write();
  ksetapt_num[2]->Write();
  laetapt_num[2]->Write();
  fout->Close();
*/
}
