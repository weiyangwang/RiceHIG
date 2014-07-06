void pT_spectra()
{
  TFile* f = new TFile("/net/hisrv0001/home/davidlw/scratch1/DiHadronCorrelations/outputs_312/HIData_Minbias_2760GeV/merged/HIData_Minbias_2760GeV_UCC2011_pixeltracks_INCLMULT_nmin-1_nmax-1_etatrg-2.4-2.4_etaass-2.4-2.4_centmin110_centmax1000.root");

  TH1D* hpt = (TH1D*)f->Get("ptall_trg");
  TH1D* hpt_corr = (TH1D*)f->Get("ptcorrall_trg");
  TH1D* hmult = (TH1D*)f->Get("multrawall");

  hpt->Scale(1.0/hmult->Integral());
  hpt_corr->Scale(1.0/hmult->Integral());
  
  hpt_corr->SetMarkerColor(kRed);
  hpt_corr->SetYTitle("dN/dp_{T}");

  TCanvas* c = new TCanvas("c","c",650,500);
  c->SetLogy();
  hpt_corr->GetXaxis()->CenterTitle();
  hpt_corr->GetYaxis()->CenterTitle();
  hpt_corr->Draw("PE");
  hpt->Draw("PESAME");

  TLegend* legend = new TLegend(0.5,0.75,0.9,0.9);
  legend->SetFillStyle(0);
  legend->SetTextFont(42);
  legend->AddEntry(hpt,"Before correction","P");
  legend->AddEntry(hpt_corr,"After correction","P");
  legend->Draw("same");

  SaveCanvas(c,"HI/UCC","pTspectra_compare");
}
