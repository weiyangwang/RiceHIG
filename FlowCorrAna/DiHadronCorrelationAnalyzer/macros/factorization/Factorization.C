#include "/net/hisrv0001/home/davidlw/useful_macros/CF.C"

void Factorization(TString tag = "UCC", int centmin=110, int centmax=1000)
{
//   TString filename = Form("/net/hisrv0001/home/davidlw/scratch1/DiHadronCorrelations/outputs_312/HIData_Minbias_2760GeV/merged/HIData_Minbias_2760GeV_%s2011_pixeltracks_INCLEFF1v1_nmin-1_nmax-1_etatrg-2.4-2.4_etaass-2.4-2.4_centmin%d_centmax%d.root",tag.Data(),centmin,centmax);
  TString filename = Form("/net/hisrv0001/home/davidlw/scratch1/DiHadronCorrelations/outputs_312/PAData_Minbias_5TeV/merged/PAData_Minbias_5TeV_MB_PromptRecoNewFinal_INCLEFF1Factorv1_nmin-1_nmax-1_etatrg-2.4-2.4_etaass-2.4-2.4_centmin-1_centmax-1.root");
  TFile* fdiff = new TFile(filename.Data());

  TString centtag="";
  if(centmin==110) centtag = "0-0.2% centrality";
  if(centmin==210) centtag = "0-0.02% centrality";
  if(centmin==50) centtag = "0-1% centrality";
  if(centmin==51) centtag = "0-1% centrality";
  if(centmin==0 && centmax==1) centtag = "0-2.5% centrality";
  if(centmin==1 && centmax==2) centtag = "2.5-5% centrality";

  TH1D* hpt[20];
  TH2D* hsignal[20][20];
  TH2D* hbackground[20][20];
  TH1D* hsignal_1D[20][20];
  TH1D* hbackground_1D[20][20];
  TH1D* hcorr_1D[20][20];
  TH1D* hcorr_dphi[20][20];
  TF1*  fitfunc_vn[20][20];

  double V1[20][20];
  double V1Error[20][20];
  double Vn[20][20];
  double VnError[20][20];
  double ratio_v2[20][20];
  double pt[20];
  double pt_error[20];

  for(int i=0;i<10;i++)
  {
    hpt[i] = (TH1D*)fdiff->Get(Form("pt_signal_trg_%d",i));
    pt[i] = hpt[i]->GetMean();
    pt_error[i] = 0.0;
   
//    for(int j=0;j<=i;j++)
    for(int j=0;j<10;j++)
    {
      hcorr_dphi[i][j] = (TH1D*)Get1DCFdPhiv3(filename.Data(),i,j,2,4);
      fitfunc_vn[i][j] = FitVnFunc(hcorr_dphi[i][j]);

      hsignal[i][j] = (TH2D*)fdiff->Get(Form("signalcosn_trg%d_ass%d",i,j));
      hbackground[i][j] = (TH2D*)fdiff->Get(Form("backgroundcosn_trg%d_ass%d",i,j));
      hsignal_1D[i][j] = (TH1D*)hsignal[i][j]->ProfileY(Form("signal_1D_trg%d_ass%d",i,j),1,-1,"e");
      hbackground_1D[i][j] = (TH1D*)hbackground[i][j]->ProfileY(Form("background_1D_trg%d_ass%d",i,j),1,-1,"e");
      hcorr_1D[i][j] = (TH1D*)hsignal_1D[i][j]->Clone(Form("corr_1D_trg%d_ass%d",i,j));
      hcorr_1D[i][j]->Add(hbackground_1D[i][j],-1);

//      for(int n=1;n<=hsignal_1D[i][j]->GetNbinsX();n++)
//      { 
        Vn[i][j]=hsignal_1D[i][j]->GetBinContent(2)-hbackground_1D[i][j]->GetBinContent(2);
        VnError[i][j]=sqrt(hsignal_1D[i][j]->GetBinError(2)*hsignal_1D[i][j]->GetBinError(2)+hbackground_1D[i][j]->GetBinError(2)*hsignal_1D[i][j]->GetBinError(2));

        V1[i][j]=hsignal_1D[i][j]->GetBinContent(1)-hbackground_1D[i][j]->GetBinContent(1);
        V1Error[i][j]=sqrt(hsignal_1D[i][j]->GetBinError(1)*hsignal_1D[i][j]->GetBinError(1)+hbackground_1D[i][j]->GetBinError(1)*hsignal_1D[i][j]->GetBinError(1));
//      }
    }
//cout<<sqrt(hcorr_1D[i][i]->GetBinContent(2))<<endl;
  }

  for(int i=0;i<10;i++)
  {
//    for(int j=0;j<=i;j++)
    for(int j=0;j<10;j++)
    {
//      cout<<i<<" "<<j<<" "<<Vn[i][j]<<" "<<fitfunc_vn[i][j]->GetParameter(2)<<endl;
//cout<<hcorr_1D[i][j]->GetBinContent(2)<<" "<<sqrt(hcorr_1D[i][i]->GetBinContent(2))<<" "<<sqrt(hcorr_1D[j][j]->GetBinContent(2))<<endl;
//      ratio_v2[i][j]=hcorr_1D[i][j]->GetBinContent(2)/sqrt(hcorr_1D[i][i]->GetBinContent(2));//sqrt(hcorr_1D[j][j]->GetBinContent(3));
//cout<<ratio_v2[i][j]<<endl;
//  cout<<fitfunc_vn[i][j]->GetParameter(3)<<" "<<fitfunc_vn[i][i]->GetParameter(3)<<" "<<fitfunc_vn[j][j]->GetParameter(3)<<endl;      
//        ratio_v2[i][j]=fitfunc_vn[i][j]->GetParameter(2)/sqrt(fitfunc_vn[i][i]->GetParameter(2))/sqrt(fitfunc_vn[j][j]->GetParameter(2));
//  cout<<ratio_v2[i][j]<<endl;
      ratio_v2[i][j]=Vn[i][j]/sqrt(Vn[i][i])/sqrt(Vn[j][j]);
//cout<<ratio_v2[i][j]<<endl;
    }    
  }

  TGraphErrors* gr_ratio[20];
  for(int i=0;i<10;i++)
  {
    gr_ratio[i] = new TGraphErrors(7,pt,ratio_v2[i]);
    gr_ratio[i]->SetName(Form("vnpt_ratio_%d",i));
    gr_ratio[i]->SetMarkerColor(i);
  }

  TGraphErrors* gr_V1[20];
  for(int i=0;i<10;i++)
  {
    gr_V1[i] = new TGraphErrors(10,pt,V1[i],pt_error,V1Error[i]);
    gr_V1[i]->SetMarkerColor(i+1);
  }

  TH2D* htmp = new TH2D("tmp",";p_{T};ratio",100,0,4,100,0.5,1.5);
  TCanvas* c = new TCanvas("c","c",550,500);
  htmp->Draw("");
  gr_ratio[2]->Draw("PESAME");
  gr_ratio[3]->Draw("PESAME");
  gr_ratio[4]->Draw("PESAME");
  gr_ratio[5]->Draw("PESAME");
  gr_ratio[6]->Draw("PESAME");

  TH2D* htmp1 = new TH2D("tmp1",";p_{T};V_{1#Delta}",100,0,8,100,-0.1,0.1);
  TCanvas* c1 = new TCanvas("c1","c1",550,500);
  htmp1->Draw("");
  gr_V1[2]->Draw("PESAME");
  gr_V1[3]->Draw("PESAME");
  gr_V1[4]->Draw("PESAME");
  gr_V1[5]->Draw("PESAME");
  gr_V1[6]->Draw("PESAME");
}
