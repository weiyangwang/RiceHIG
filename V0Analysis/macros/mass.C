void mass()
{
  TFile* f[10];
  f[0] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0validation_match075_v4.root");
  f[1] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0validation_match06_v4.root");
  f[2] = new TFile("/net/hisrv0001/home/davidlw/scratch1/v0validation_match05_v4.root");

  TH1D* ksmassall[10];
  TH1D* ksmassfake[10];
  TH1D* ksmassgood[10];

  TH1D* lamassall[10];
  TH1D* lamassfake[10];
  TH1D* lamassgood[10];

  for(int i=0;i<3;i++)
  {
    ksmassall[i] = (TH1D*)f[i]->Get("v0Validator/ksMassAll");
    ksmassgood[i] = (TH1D*)f[i]->Get("v0Validator/ksMassGood");
    ksmassfake[i] = (TH1D*)f[i]->Get("v0Validator/ksMassFake");
    ksmassgood[i]->SetMarkerColor(i+1);
    ksmassfake[i]->SetMarkerColor(i+1);

    lamassall[i] = (TH1D*)f[i]->Get("v0Validator/lamMassAll");
    lamassgood[i] = (TH1D*)f[i]->Get("v0Validator/lamMassGood");
    lamassfake[i] = (TH1D*)f[i]->Get("v0Validator/lamMassFake");
    lamassgood[i]->SetMarkerColor(i+1);
    lamassfake[i]->SetMarkerColor(i+1);
  }

  TCanvas* c = new TCanvas("c","c",600,500);
  ksmassfake[0]->SetAxisRange(0.43,0.56,"X");
  ksmassfake[0]->Draw("PE");
  ksmassfake[1]->Draw("PESAME");
  ksmassfake[2]->Draw("PESAME");

  TCanvas* c1 = new TCanvas("c1","c1",600,500);
  lamassfake[0]->SetAxisRange(1.08,1.16,"X");
  lamassfake[0]->Draw("PE");
  lamassfake[1]->Draw("PESAME");
  lamassfake[2]->Draw("PESAME");

  TCanvas* c2 = new TCanvas("c2","c2",600,500);
  ksmassgood[0]->SetAxisRange(0.43,0.56,"X");
  ksmassgood[0]->Draw("PE");
  ksmassgood[1]->Draw("PESAME");
  ksmassgood[2]->Draw("PESAME");

  TCanvas* c3 = new TCanvas("c3","c3",600,500);
  lamassgood[0]->SetAxisRange(1.08,1.16,"X");
  lamassgood[0]->Draw("PE");
  lamassgood[1]->Draw("PESAME");
  lamassgood[2]->Draw("PESAME");

  SaveCanvas(c,"HI/V0","ksmassfake");
  SaveCanvas(c1,"HI/V0","lammassfake");
  SaveCanvas(c2,"HI/V0","ksmassgood");
  SaveCanvas(c3,"HI/V0","lammassgood");
}
