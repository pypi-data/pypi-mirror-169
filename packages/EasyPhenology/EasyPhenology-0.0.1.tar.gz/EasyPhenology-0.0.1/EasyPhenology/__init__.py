def integral_smoothing(df):
    Year = []
    Var_smooth=[]
    Var_Years=np.unique(df['year'])  #number of years in the site
    df_smooth=pd.DataFrame()
    for j in range(len(Var_Years)):  #looping for years
        df_jyear=df.loc[df['year'] ==Var_Years[j]] #the dataframe for year j

        if df_jyear['Var'].isnull().sum()<100:
        #For smoothing add 10 days before and after the year from the same year
            df_jyear_b= df_jyear.head(10)
            df_jyear_a= df_jyear.tail(10)
            df_jyear=pd.concat([df_jyear_b, df_jyear, df_jyear_a ])

            #interpolate if there is a nan
            df_jyear['Var']=df_jyear['Var'].interpolate(method='linear')
            
            # Cumulative of Variable from raw values
            Var_cum = df_jyear['Var'].cumsum()

            #Smooth the cumulative signal
            x = np.linspace(1, len(Var_cum), len(Var_cum))
            p = np.poly1d(np.polyfit(x, Var_cum, 7)) #the method of smoothing can be changed, since its a simple curve it does not matter
            Var_cum_smooth=p(x)
            Var_smooth=np.gradient(Var_cum_smooth,1)
            df_jyear['Var']=Var_smooth
            df_jyear=df_jyear.iloc[10:375,:]
            #df_smooth.append(df_jyear)
            df_smooth = pd.concat([df_smooth, df_jyear])

        else:
            df_jyear['Var']=np.nan
            #df_smooth.append(df_jyear)
            df_smooth = pd.concat([df_smooth, df_jyear])
    return df_smooth






def EasyPhenology(df, Threshold_value):


    # Define rows in the output dataframe
    rows = []
    Var_Years=np.unique(df['year'])  #number of years 
        
    #smooth the data first
    df=integral_smoothing(df)

    for j in range(len(Var_Years)): #looping for years

        df_jyear=df.loc[df['year'] ==Var_Years[j]] #the dataframe for year j


        if df_jyear['Var'].isnull().sum()<100:


            # peak of season, POS
            pos=df.iloc[df_jyear.Var.argmax(), 2]

            #SOS, EOS, GSL from threshold method
            Var_n=(df_jyear[0:pos+1].Var -min(df_jyear[0:pos+1].Var ))/(max(df_jyear[0:pos+1].Var )-min(df_jyear[0:pos+1].Var )  ) #normalized value of Var from 1jan to POS
            sos_p=np.argwhere(np.diff(np.sign(Var_n - Threshold_value))).flatten()
            sos=sos_p[-1] +1

            #if multiple points have this threshold then eos is in begning of season
            if len(sos_p)>1:
                eos=sos_p[-2] +1

            else:
                Var_n=(df_jyear[pos+1:-1].Var -min(df_jyear[pos+1:-1].Var ))/(max(df_jyear[pos+1:-1].Var )-min(df_jyear[pos+1:-1].Var )  ) #normalized value of Var from 1jan to POS
                eos_p=np.argwhere(np.diff(np.sign(Var_n - Threshold_value))).flatten()
                eos=eos_p[-1] + pos +1

            gsl=eos-sos

            if gsl<0:
                gsl=gsl+365

            #SOS, EOS, GSL from derivative method
            Var_1der=np.gradient(df_jyear.Var,1)

            pos_p=np.argwhere(np.diff(np.sign(Var_1der - 0))).flatten() #positions when derivative is 0, possible pos
            pos_der=pos_p[abs(pos_p-pos).argmin()]  # pos_p closest to the peak of season doy
            sos_p=argrelextrema(Var_1der, np.greater)[0] #doy of local max derivative positions
            eos_p=argrelextrema(Var_1der, np.less)[0] #doy of local min derivative positions
            sos_der=sos_p[abs(sos_p-sos).argmin()] +1 #local max closest to pos is sos
            eos_der=eos_p[abs(eos_p-eos).argmin()] +1 #local min closest to pos is eos
            gsl_der=eos_der -sos_der

            if gsl_der<0:
                gsl_der=gsl_der+365


            rows.append([Var_Years[j], sos, pos, eos, gsl, sos_der, eos_der, gsl_der])

        else:
            rows.append([Var_Years[j], np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])

        df_pheno = pd.DataFrame(rows, columns=["Year", "SOS", "POS", "EOS", "GSL", "SOS_der", "EOS_der","GSL_der"])

    return Pheno_out, df

