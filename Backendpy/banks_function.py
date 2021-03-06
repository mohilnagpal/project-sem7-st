# -*- coding: utf-8 -*-
"""Banks_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HhExCH3SFafayKVGe0WGYd67B5PXvI1Q
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd 
import json 
def banks():
  def itcon(stockname,url1,url2):


    stock_name=stockname
    url = url1

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse HTML code for the entire site
    soup = BeautifulSoup(html_content, "lxml")
    # print(soup)

    mc = soup.find_all("div", attrs={"class": "oview_table"})
    # print("Number of tables on site: ",len(mc))

    data = dict()
    for tb in mc[:4]:
        body = tb.find_all("tr")
        for i in body:
            vals = i.find_all("td")
            title = vals[0].text.strip()
            try:
                value = float(vals[1].text.replace(',',''))
            except ValueError:
                value = vals[1].text.replace(',','')
            data[title] = value
    # print(data)



    excel_data=pd.read_csv(r"C:\Users\mohil\OneDrive\Desktop\STOCKS_new.csv")
    excel_data.drop(columns=['Name (largecap alpha.csv)', 'Ticker (largecap alpha.csv)'],inplace=True)
    # excel_data.head(10)

    avg_price=round((data['Open']+data['Previous Close'])/2,2)
    shareholding=round((data['Mkt Cap (Rs. Cr.)']/avg_price),2)
    shareholding

    parameters_dict = dict()
    def scrape_indicators(urls):
        for url in urls:
            html_content = requests.get(url).text

            # Parse HTML code for the entire site
            soup = BeautifulSoup(html_content, "lxml")
            stonks = soup.find_all("div", attrs={"id": "standalone-new"})

            body = stonks[0].find_all("tr")

            indicator_dict = dict()

            for record in body:
                indicator = record.find_all("td")[0].text.upper()
                temp_indicator_values = []
                try:
                    for table_data in (record.find_all('td')[1:-1]):
                        temp_indicator_values.append(
                            float(table_data.text.replace(',', '')))
                except ValueError:
                    continue
                indicator_dict[indicator] = temp_indicator_values

            parameters_dict.update(indicator_dict)

        yield(url, parameters_dict)
      
    urls=url2
    # urls = ["https://www.moneycontrol.com/financials/godfreyphillipsindia/balance-sheetVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/profit-lossVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/cash-flowVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/ratiosVI/GPI#GPI"]


    for request_url, indicator_data in scrape_indicators(urls):
        # print(request_url)
        # print(indicator_data)
        print()
        print()

    pepoints=0


    if(data['Mkt Cap (Rs. Cr.)']<20000.00 and data['Mkt Cap (Rs. Cr.)']>5000.00):
      cap="Mid Cap"
    elif (data['Mkt Cap (Rs. Cr.)']>20000.00):
      cap="Large Cap"
    else:
      cap="Small Cap"
    ##Indicator 1: Reserves & Surplus
    # print(indicator_data['RESERVES AND SURPLUS'])
    rands_list=[]
    count_reserves=0
    for i in range(len(indicator_data['RESERVES AND SURPLUS'])-1,0,-1):
      if(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i]>0):
        rands_list.append(round(((indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i])/indicator_data['RESERVES AND SURPLUS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_reserves=count_reserves+20
        pepoints+=1
        # print(indicator_data['RESERVES AND SURPLUS'][i-1] , "-" , indicator_data['RESERVES AND SURPLUS'][i],"=", round(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i],2))
      else:
        rands_list.append(round(((indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i])/indicator_data['RESERVES AND SURPLUS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_reserves=count_reserves-20
        pepoints-=1
        # print(indicator_data['RESERVES AND SURPLUS'][i-1],"-",indicator_data['RESERVES AND SURPLUS'][i],"=", round(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i],2))

    rands_list=rands_list[::-1]

    for i in range(len(indicator_data['RESERVES AND SURPLUS'])-1,-1,-1):
        if(indicator_data['RESERVES AND SURPLUS'][i]<0):
          count_reserves-=20
          pepoints-=1


    indicator_data['INTEREST EXPENDED']

    ##Indicator 2: Total Interest Earned
    # print(indicator_data['TOTAL INTEREST EARNED'])
    interest_list=[]
    count_interest=0
    for i in range(len(indicator_data['TOTAL INTEREST EARNED'])-1,0,-1):
      if(indicator_data['TOTAL INTEREST EARNED'][i-1]-indicator_data['TOTAL INTEREST EARNED'][i]>0):
        interest_list.append(round(((indicator_data['TOTAL INTEREST EARNED'][i-1]-indicator_data['TOTAL INTEREST EARNED'][i])/indicator_data['TOTAL INTEREST EARNED'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_interest=count_interest+20
        pepoints+=1
        # print(indicator_data['TOTAL INTEREST EARNED'][i-1] , "-" , indicator_data['TOTAL INTEREST EARNED'][i],"=", round(indicator_data['TOTAL INTEREST EARNED'][i-1]-indicator_data['TOTAL INTEREST EARNED'][i],2))
      else:
        interest_list.append(round(((indicator_data['TOTAL INTEREST EARNED'][i-1]-indicator_data['TOTAL INTEREST EARNED'][i])/indicator_data['TOTAL INTEREST EARNED'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_interest=count_interest-20
        pepoints-=1
        # print(indicator_data['TOTAL INTEREST EARNED'][i-1],"-",indicator_data['TOTAL INTEREST EARNED'][i],"=", round(indicator_data['TOTAL INTEREST EARNED'][i-1]-indicator_data['TOTAL INTEREST EARNED'][i],2))

    interest_list=interest_list[::-1]

    for i in range(len(indicator_data['TOTAL INTEREST EARNED'])-1,-1,-1):
        if(indicator_data['TOTAL INTEREST EARNED'][i]<0):
          count_interest-=20
          pepoints-=1


    ##Indicator 3: Total Interest Expended
    # print(indicator_data['INTEREST EXPENDED'])
    spend_list=[]
    count_spend=0
    for i in range(len(indicator_data['INTEREST EXPENDED'])-1,0,-1):
      if(indicator_data['INTEREST EXPENDED'][i-1]-indicator_data['INTEREST EXPENDED'][i]<0):
        spend_list.append(round(((indicator_data['INTEREST EXPENDED'][i-1]-indicator_data['INTEREST EXPENDED'][i])/indicator_data['INTEREST EXPENDED'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_spend=count_spend+20
        pepoints+=1
        # print(indicator_data['INTEREST EXPENDED'][i-1] , "-" , indicator_data['INTEREST EXPENDED'][i],"=", round(indicator_data['INTEREST EXPENDED'][i-1]-indicator_data['INTEREST EXPENDED'][i],2))
      else:
        spend_list.append(round(((indicator_data['INTEREST EXPENDED'][i-1]-indicator_data['INTEREST EXPENDED'][i])/indicator_data['INTEREST EXPENDED'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_spend=count_spend-20
        pepoints-=1
        # print(indicator_data['INTEREST EXPENDED'][i-1],"-",indicator_data['INTEREST EXPENDED'][i],"=", round(indicator_data['INTEREST EXPENDED'][i-1]-indicator_data['INTEREST EXPENDED'][i],2))

    spend_list=spend_list[::-1]

    for i in range(len(indicator_data['INTEREST EXPENDED'])-1,-1,-1):
        if(indicator_data['INTEREST EXPENDED'][i]<0):
          count_spend-=20
          pepoints-=1

    # print(count_spend)
    # print(spend_list)

    ##Indicator 4: Profit/Loss for the period
    count_profitloss=0
    profit_list=[]
    # print(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'])
    for i in range(len(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'])-1,0,-1):
      if(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1]-indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i]>0):
        profit_list.append(round(((indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1]-indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i])/indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i])*100,2))
        count_profitloss=count_profitloss+20
        # print(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1] , "-" , indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i],"=", round(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1]-indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i],2))
      else:
        profit_list.append(round(((indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1]-indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i])/indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i])*100,2))
        count_profitloss=count_profitloss-20
        # print(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1],"-",indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i],"=",round(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i-1]-indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i],2))

    profit_list=profit_list[::-1]

    for i in range(len(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'])-1,-1,-1):
        if(indicator_data['TOTAL PROFIT / LOSS AVAILABLE FOR APPROPRIATIONS'][i]<0):
          count_profitloss-=15

    # print(count_profitloss)
    # print(profit_list)

    indicator_data['DEPOSITS']

    ##Indicator 5: Total Deposits
    # print(indicator_data['DEPOSITS'])
    dep_list=[]
    count_dep=0
    for i in range(len(indicator_data['DEPOSITS'])-1,0,-1):
      if(indicator_data['DEPOSITS'][i-1]-indicator_data['DEPOSITS'][i]>0):
        dep_list.append(round(((indicator_data['DEPOSITS'][i-1]-indicator_data['DEPOSITS'][i])/indicator_data['DEPOSITS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_dep=count_dep+20
        pepoints+=1
        # print(indicator_data['DEPOSITS'][i-1] , "-" , indicator_data['DEPOSITS'][i],"=", round(indicator_data['DEPOSITS'][i-1]-indicator_data['DEPOSITS'][i],2))
      else:
        interest_list.append(round(((indicator_data['DEPOSITS'][i-1]-indicator_data['DEPOSITS'][i])/indicator_data['DEPOSITS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_dep=count_dep-20
        pepoints-=1
        # print(indicator_data['DEPOSITS'][i-1],"-",indicator_data['DEPOSITS'][i],"=", round(indicator_data['DEPOSITS'][i-1]-indicator_data['DEPOSITS'][i],2))

    interest_list=interest_list[::-1]

    for i in range(len(indicator_data['DEPOSITS'])-1,-1,-1):
        if(indicator_data['DEPOSITS'][i]<0):
          count_interest-=20
          pepoints-=1

    # print(count_dep)
    # print(dep_list)

    ##Indicator 6: Total Advances
    # print(indicator_data['ADVANCES'])
    adv_list=[]
    count_adv=0
    for i in range(len(indicator_data['ADVANCES'])-1,0,-1):
      if(indicator_data['ADVANCES'][i-1]-indicator_data['ADVANCES'][i]>0):
        adv_list.append(round(((indicator_data['ADVANCES'][i-1]-indicator_data['ADVANCES'][i])/indicator_data['ADVANCES'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_adv=count_adv+20
        pepoints+=1
        # print(indicator_data['ADVANCES'][i-1] , "-" , indicator_data['ADVANCES'][i],"=", round(indicator_data['ADVANCES'][i-1]-indicator_data['ADVANCES'][i],2))
      else:
        adv_list.append(round(((indicator_data['ADVANCES'][i-1]-indicator_data['ADVANCES'][i])/indicator_data['ADVANCES'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_adv=count_adv-20
        pepoints-=1
        # print(indicator_data['ADVANCES'][i-1],"-",indicator_data['ADVANCES'][i],"=", round(indicator_data['ADVANCES'][i-1]-indicator_data['ADVANCES'][i],2))

    adv_list=adv_list[::-1]

    for i in range(len(indicator_data['ADVANCES'])-1,-1,-1):
        if(indicator_data['ADVANCES'][i]<0):
          count_adv-=20
          pepoints-=1

    # print(count_adv)
    # print(adv_list)

    indicator_data['PROVISIONS AND CONTINGENCIES']

    ##Indicator 7: Provisions and Contingencies
    # print(indicator_data['PROVISIONS AND CONTINGENCIES'])
    pro_list=[]
    count_pro=0
    for i in range(len(indicator_data['PROVISIONS AND CONTINGENCIES'])-1,0,-1):
      if(indicator_data['PROVISIONS AND CONTINGENCIES'][i-1]-indicator_data['PROVISIONS AND CONTINGENCIES'][i]<0):
        pro_list.append(round(((indicator_data['PROVISIONS AND CONTINGENCIES'][i-1]-indicator_data['PROVISIONS AND CONTINGENCIES'][i])/indicator_data['PROVISIONS AND CONTINGENCIES'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_pro=count_pro+20
        pepoints+=1
        # print(indicator_data['PROVISIONS AND CONTINGENCIES'][i-1] , "-" , indicator_data['PROVISIONS AND CONTINGENCIES'][i],"=", round(indicator_data['PROVISIONS AND CONTINGENCIES'][i-1]-indicator_data['PROVISIONS AND CONTINGENCIES'][i],2))
      else:
        pro_list.append(round(((indicator_data['PROVISIONS AND CONTINGENCIES'][i-1]-indicator_data['PROVISIONS AND CONTINGENCIES'][i])/indicator_data['PROVISIONS AND CONTINGENCIES'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_pro=count_pro-20
        pepoints-=1
        # print(indicator_data['PROVISIONS AND CONTINGENCIES'][i-1],"-",indicator_data['PROVISIONS AND CONTINGENCIES'][i],"=", round(indicator_data['PROVISIONS AND CONTINGENCIES'][i-1]-indicator_data['PROVISIONS AND CONTINGENCIES'][i],2))

    pro_list=pro_list[::-1]

    # for i in range(len(indicator_data['ADVANCES'])-1,-1,-1):
    #     if(indicator_data['ADVANCES'][i]<0):
    #       count_adv-=20
    #       pepoints-=1
    prov_ind=round((indicator_data['PROVISIONS AND CONTINGENCIES'][0]-indicator_data['PROVISIONS AND CONTINGENCIES'][4])/indicator_data['PROVISIONS AND CONTINGENCIES'][4],2)*100

    # print(count_pro)
    # print(pro_list)
    # print(prov_ind)



    ##Indicator 8: NPA

    count_npa=0
    # print(indicator_data["NET NPA (%)"])

    for i in range(len(indicator_data['NET NPA (%)'])-1,0,-1):
      if(indicator_data['NET NPA (%)'][i-1]-indicator_data['NET NPA (%)'][i]<0):
        count_npa+=20
        pepoints+=1
        # print(indicator_data['NET NPA (%)'][i-1] , "-" , indicator_data['NET NPA (%)'][i],"=", round(indicator_data['NET NPA (%)'][i-1]-indicator_data['NET NPA (%)'][i],2))
      elif (indicator_data['NET NPA (%)'][i-1]-indicator_data['NET NPA (%)'][i]==0):
            count_npa+=20
            pepoints+=1
      else:
        count_npa-=10
        pepoints-=1
        # print(indicator_data['NET NPA (%)'][i-1],"-",indicator_data['NET NPA (%)'][i],"=",round(indicator_data['NET NPA (%)'][i-1]-indicator_data['NET NPA (%)'][i],2))
    # print(count_npa)

    ##Indicator 9: Gross NPA

    count_gnpa=0
    # print(indicator_data["GROSS NPA (%)"])

    for i in range(len(indicator_data['GROSS NPA (%)'])-1,0,-1):
      if(indicator_data['GROSS NPA (%)'][i-1]-indicator_data['GROSS NPA (%)'][i]<0):
        count_gnpa+=20
        pepoints+=1
        # print(indicator_data['GROSS NPA (%)'][i-1] , "-" , indicator_data['GROSS NPA (%)'][i],"=", round(indicator_data['GROSS NPA (%)'][i-1]-indicator_data['GROSS NPA (%)'][i],2))
      elif (indicator_data['GROSS NPA (%)'][i-1]-indicator_data['GROSS NPA (%)'][i]==0):
            count_gnpa+=20
            pepoints+=1
      else:
        count_gnpa-=10
        pepoints-=1
        # print(indicator_data['GROSS NPA (%)'][i-1],"-",indicator_data['GROSS NPA (%)'][i],"=",round(indicator_data['GROSS NPA (%)'][i-1]-indicator_data['GROSS NPA (%)'][i],2))
    # print(count_gnpa)

    ##Indicator 10: NPA to Advances

    count_adpa=0
    # print(indicator_data["NET NPA TO ADVANCES (%)"])

    for i in range(len(indicator_data['NET NPA TO ADVANCES (%)'])-1,0,-1):
      if(indicator_data['NET NPA TO ADVANCES (%)'][i-1]-indicator_data['NET NPA TO ADVANCES (%)'][i]<0):
        count_adpa+=20
        pepoints+=1
        # print(indicator_data['NET NPA TO ADVANCES (%)'][i-1] , "-" , indicator_data['NET NPA TO ADVANCES (%)'][i],"=", round(indicator_data['NET NPA TO ADVANCES (%)'][i-1]-indicator_data['NET NPA TO ADVANCES (%)'][i],2))
      elif (indicator_data['NET NPA TO ADVANCES (%)'][i-1]-indicator_data['NET NPA TO ADVANCES (%)'][i]==0):
            count_adpa+=20
            pepoints+=1
      else:
        count_adpa-=10
        pepoints-=1
        # print(indicator_data['NET NPA TO ADVANCES (%)'][i-1],"-",indicator_data['NET NPA TO ADVANCES (%)'][i],"=",round(indicator_data['NET NPA TO ADVANCES (%)'][i-1]-indicator_data['NET NPA TO ADVANCES (%)'][i],2))

    npa_ind=indicator_data['NET NPA TO ADVANCES (%)'][0]-indicator_data['NET NPA TO ADVANCES (%)'][4]


    # print(count_adpa)
    # print(npa_ind)

    indicator_data['CASA (%)']

    ##Indicator 11: CASA

    count_casa=0
    # print(indicator_data["CASA (%)"])

    for i in range(len(indicator_data['CASA (%)'])-1,0,-1):
      if(indicator_data['CASA (%)'][i-1]-indicator_data['CASA (%)'][i]>-0.5):
        count_casa+=20
        pepoints+=1
        # print(indicator_data['CASA (%)'][i-1] , "-" , indicator_data['CASA (%)'][i],"=", round(indicator_data['CASA (%)'][i-1]-indicator_data['CASA (%)'][i],2))
      elif (indicator_data['CASA (%)'][i-1]-indicator_data['CASA (%)'][i]==0):
            count_casa+=20
            pepoints+=1
      else:
        count_casa-=10
        pepoints-=1
        # print(indicator_data['CASA (%)'][i-1],"-",indicator_data['CASA (%)'][i],"=",round(indicator_data['CASA (%)'][i-1]-indicator_data['CASA (%)'][i],2))

    casa_ind=indicator_data['CASA (%)'][0]


    # print(count_casa)
    # print(casa_ind)



    ##Indicator 12: Free cash Flow
    stock_position=None
    stock_data=excel_data.values.tolist()
    stock_data
    for i in stock_data:
      for j in i:
        j=str(j)
        # print(j)
        if(stock_name in j):
          # print(j.index(i))
          stock_position=stock_data.index(i)
          # print(j)
          break
          
    # print(stock_position)

    freecash_list=[]
    for i in range(5):
      freecash_list.append(stock_data[stock_position][i])
    # print(freecash_list)

    count_freecash=0
    for i in range(1,len(freecash_list)):
      if(freecash_list[i]-freecash_list[i-1]>0):
        # print(freecash_list[i],"-",freecash_list[i-1],"=",freecash_list[i]-freecash_list[i-1])
        count_freecash+=20
        pepoints+=1
      else:
        # print(freecash_list[i],"-",freecash_list[i-1],"=",freecash_list[i]-freecash_list[i-1])
        count_freecash-=10
        pepoints-=1

    for i in range(0,len(freecash_list)):
      if(freecash_list[i]<0):
        count_freecash-=20
        pepoints-=1

    # print(count_freecash)

    ##Indicator 13: Pledged shares
    for i in stock_data:
      for j in i:
        j=str(j)
        if(stock_name in j):
          # print(j.index(i))
          stock_position=stock_data.index(i)
          # print(j)
          break

    pledged_shares=stock_data[stock_position][15]
    # print(pledged_shares)

    count_pshares=1
    if(pledged_shares>0):
      pepoints-=1
      count_pshares=count_pshares*-10
    else:
      count_pshares=count_pshares*10
      pepoints+=1

    ##Entities: Alpha & Beta
    alpha=round(stock_data[stock_position][9],2)
    # print("Alpha",alpha)
    beta=round(stock_data[stock_position][10],2)
    # print("Beta",beta)
    divy=data['Dividend Yield']
    # print("Dividend Yield",divy)

    cagr=stock_data[stock_position][8]
    # print("CAGR:", cagr)

    ##Indicator 14: PE Ratio
    st_pe=data['TTM PE']
    se_pe=data['Sector PE']
    # print("Stock PE", st_pe)
    # print("Sector PE",se_pe)
    count_pe=1
    if(data['TTM PE']=="--"):
        count_pe=pepoints*10
    elif(data['TTM PE']<data['Sector PE']):
      count_pe=pepoints*15
    else:
      count_pe=pepoints*10

    # print(count_pe)



    points=count_profitloss+count_reserves+count_pe+count_freecash+count_pshares+count_interest+count_adpa+count_adv+count_casa+count_dep+count_gnpa+count_npa+count_pro+count_spend+casa_ind*10
    # print(points)

    final_list=[]
    positives=[]
    if(beta>0 and beta<1.5):
      positives.append(" {} is {} times volatile than the market, low risk stock".format(stock_name,beta))
    if(count_reserves>60):
      positives.append(" Reserves And Surplus for {} are significantly increasing.".format(stock_name))
    if(casa_ind>45):
      positives.append(" Good Current to Savings Account Ratio for {}.".format(stock_name))
    if(npa_ind<2):
      positives.append(" Low Non Performing Assets for {}.".format(stock_name))
    if(st_pe!= "--"):
      if(st_pe<se_pe and pepoints >24):
        positives.append(" {} has PE ratio less than the industry PE, can be a steal deal".format(stock_name))
    


    

    negatives=[]
    if(pledged_shares>5):
      negatives.append(" {} has pledged shares.".format(stock_name))
    if(count_reserves<0):
      negatives.append(" Reserves and Surplus are continously decreasing for {}.".format(stock_name))
    if(npa_ind>3):
      negatives.append("{} has high Non Performing Assets.".format(stock_name))
    if(beta>1.5):
      negatives.append(" {} is {} times volatile than the market, high risk stock".format(stock_name,beta))
    if(casa_ind<30):
      negatives.append(" {} has low CASA performance".format(stock_name))
    
    final_list.append(stock_name) 
    final_list.append(divy)
    final_list.append(cagr) 
    final_list.append(cap)

    final_list.append(casa_ind)

    final_list.append(points)
    final_list.append(positives)
    final_list.append(negatives)


    return final_list
  table=[]
  url_list=[]
        
  url_list=[[["HDFCBANK"],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/hdfcbank/HDF01'],["https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01#HDF01","https://www.moneycontrol.com/financials/hdfcbank/profit-lossVI/HDF01#HDF01","https://www.moneycontrol.com/financials/hdfcbank/results/quarterly-results/HDF01#HDF01","https://www.moneycontrol.com/financials/hdfcbank/cash-flowVI/HDF01#HDF01","https://www.moneycontrol.com/financials/hdfcbank/ratiosVI/HDF01#HDF01"]],
          [["ICICIBANK"],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/icicibank/ICI02'],['https://www.moneycontrol.com/financials/icicibank/balance-sheetVI/ICI02#ICI02','https://www.moneycontrol.com/financials/icicibank/profit-lossVI/ICI02#ICI02','https://www.moneycontrol.com/financials/icicibank/results/quarterly-results/ICI02#ICI02','https://www.moneycontrol.com/financials/icicibank/cash-flowVI/ICI02#ICI02','https://www.moneycontrol.com/financials/icicibank/ratiosVI/ICI02#ICI02']],
          [['KOTAKBANK'],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/kotakmahindrabank/KMB'],['https://www.moneycontrol.com/financials/kotakmahindrabank/ratiosVI/KMB#KMB','https://www.moneycontrol.com/financials/kotakmahindrabank/cash-flowVI/KMB#KMB','https://www.moneycontrol.com/financials/kotakmahindrabank/results/quarterly-results/KMB#KMB','https://www.moneycontrol.com/financials/kotakmahindrabank/profit-lossVI/KMB#KMB','https://www.moneycontrol.com/financials/kotakmahindrabank/balance-sheetVI/KMB#KMB']],
          [['SBIN'],['https://www.moneycontrol.com/india/stockpricequote/bankspublicsector/statebankindia/SBI'],['https://www.moneycontrol.com/financials/statebankindia/balance-sheetVI/SBI#SBI','https://www.moneycontrol.com/financials/statebankindia/profit-lossVI/SBI#SBI','https://www.moneycontrol.com/financials/statebankindia/results/quarterly-results/SBI#SBI','https://www.moneycontrol.com/financials/statebankindia/cash-flowVI/SBI#SBI','https://www.moneycontrol.com/financials/statebankindia/ratiosVI/SBI#SBI']],
          [['AXISBANK'],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/axisbank/AB16'],['https://www.moneycontrol.com/financials/axisbank/balance-sheetVI/AB16#AB16','https://www.moneycontrol.com/financials/axisbank/profit-lossVI/AB16#AB16','https://www.moneycontrol.com/financials/axisbank/results/quarterly-results/AB16#AB16','https://www.moneycontrol.com/financials/axisbank/cash-flowVI/AB16#AB16','https://www.moneycontrol.com/financials/axisbank/ratiosVI/AB16#AB16']],
          [['INDUSINDBK'],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/indusindbank/IIB'],['https://www.moneycontrol.com/financials/indusindbank/balance-sheetVI/IIB#IIB','https://www.moneycontrol.com/financials/indusindbank/profit-lossVI/IIB#IIB','https://www.moneycontrol.com/financials/indusindbank/results/quarterly-results/IIB#IIB','https://www.moneycontrol.com/financials/indusindbank/cash-flowVI/IIB#IIB','https://www.moneycontrol.com/financials/indusindbank/ratiosVI/IIB#IIB']],
          [['BANDHANBNK'],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/bandhanbank/BB09'],['https://www.moneycontrol.com/financials/bandhanbank/balance-sheetVI/BB09#BB09','https://www.moneycontrol.com/financials/bandhanbank/profit-lossVI/BB09#BB09','https://www.moneycontrol.com/financials/bandhanbank/results/quarterly-results/BB09#BB09','https://www.moneycontrol.com/financials/bandhanbank/cash-flowVI/BB09#BB09','https://www.moneycontrol.com/financials/bandhanbank/ratiosVI/BB09#BB09']],

          [['YESBANK'],['https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/yesbank/YB'],['https://www.moneycontrol.com/financials/yesbank/balance-sheetVI/YB#YB','https://www.moneycontrol.com/financials/yesbank/profit-lossVI/YB#YB','https://www.moneycontrol.com/financials/yesbank/results/quarterly-results/YB#YB','https://www.moneycontrol.com/financials/yesbank/cash-flowVI/YB#YB','https://www.moneycontrol.com/financials/yesbank/ratiosVI/YB#YB']]]
        
            

            

  for i in range(len(url_list)):
    list_input=[]
    for j in url_list[i]:
      list_input.append(j)
    stockname=list_input[0][0]
    url1=list_input[1][0]
    url2=list_input[2]
    print(stockname,url1,url2)
    final_list=itcon(stockname,url1,url2)
    table.append(final_list)
  df=pd.DataFrame(table,columns=['stock_name','divy','cagr','cap','casa_ind','points','positives','negatives'])
  df.sort_values(by='points', ascending=False,inplace=True)
  stock=[]
  stock=df.values.tolist()
  with open("banks_stock.txt","w") as fmcgdata:
    stock_json=json.dumps(stock)
    fmcgdata.write(stock_json)
 
  return stock


import datetime
from datetime import datetime


def function_banks():
  currentDay = datetime.now().day
  currentMonth = datetime.now().month

  if(currentMonth in [11,2,5,8] and currentDay==20):
    result=banks()
    return result
  else:
    try:
      data_file = open("banks_stock.txt","r")
      list_stock = data_file.read()
      list_stock = json.loads(list_stock)

    except FileNotFoundError:
      
      list_stock = banks()
    return list_stock

