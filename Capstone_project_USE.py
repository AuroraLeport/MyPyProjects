
# coding: utf-8

#Converting csv into pandas and extracting target columns from 2014 dataset:
import pandas as pd
geocorr_full14 = pd.read_csv('./geocorr14_use.csv', header=True, index_col=None)
len(geocorr_full14)
geocorr_full14.head()

pd.options.display.max_rows = 15
geocorr_min_new = geocorr_full14[['puma12','puma2k','PUMA12 Name','ZIP Census Tabulation Area',
                                 'Pop 2014 estimate fr county level ests',
                                 'puma2k to zcta5 alloc factor']]
geocorr_min_new.columns = ['puma12','pumaold','pumaname','zipcode','TotalPop14','AF']


#geting rid of non-zipcode rows from 2014 datset:
geocorr_min_new = geocorr_min_new[geocorr_min_new.zipcode !=99999]
print len(geocorr_min_new)
geocorr_min_new = geocorr_min_new[geocorr_min_new.zipcode !=99999]


#Converting csv into pandas and extracting target columns from 2010 dataset:
import pandas as pd
geocorr_full10 = pd.read_csv('./geocorr10_use.csv', header=True, index_col=None)
geocorr_min_med = geocorr_full10[['puma12','puma2k','PUMA12 Name','ZIP Census Tabulation Area',
                                 'Total Pop, 2010 census','puma2k to zcta5 alloc factor']]
geocorr_min_med.columns = ['puma12','pumaold','pumaname','zipcode','TotalPop10','AF']

#geting rid of non-zipcode rows from 2010 dataset:
geocorr_min_new_med = geocorr_min_med[geocorr_min_med.zipcode !=99999]
print len(geocorr_min_new_med)
geocorr_min_med = geocorr_min_med[geocorr_min_med.zipcode !=99999]


#Converting csv into pandas and extracting target columns from 2000 dataset:
import pandas as pd
geocorr_full00 = pd.read_csv('./geocorr00_use.csv', header=True, index_col=None)

pd.options.display.max_rows = 15
geocorr_min_old = geocorr_full00[['puma12','puma2k','PUMA12 Name','ZIP Census Tabulation Area',
                                 'Est Pop 2k Census','puma2k to zcta5 alloc factor']]
geocorr_min_old.columns = ['puma12','pumaold','pumaname','zipcode','TotalPop00','AF']

#geting rid of non-zipcode rows from 2000 dataset:
#print geocorr_full00[geocorr_full00['ZIP Census Tabulation Area']==99999].count()
geocorr_min_old = geocorr_min_old[geocorr_min_old.zipcode !=99999]


#converting raw csv data into pd dataframe:
#CA2014 = pd.read_csv('ss14pca.csv.gz')
#CA2013 = pd.read_csv('ss13pca.csv')
#CA2012 = pd.read_csv('ss12pca.csv')
#CA2011 = pd.read_csv('ss11pca.csv')
#CA2010 = pd.read_csv('ss10pca.csv.gz')
#CA2009 = pd.read_csv('ss09pca.csv')
#CA2008 = pd.read_csv('ss08pca.csv')
#CA2007 = pd.read_csv('ss07pca.csv')
#CA2006 = pd.read_csv('ss06pca.csv.gz')
#CA2005 = pd.read_csv('ss05pca.csv')


#Columns related to seniors useful towards ride-share companies: 
#SERIALNO, SPORDER, PUMA, REGION, ST, AGEP, DDRS, DEAR, DEYE, DOUT, DPHY, DRAT, DREM, 
#HINS4, JWMNP, JWTR, MAR, MARHW, OIP, PAP, RETP, SEX, SSP, WAGP, DIS, DRIVESP, HICOV 



#Extracting target columns from datasets:
CA2014_min = CA2014[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]
CA2013_min = CA2013[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]
CA2012_min = CA2012[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]
#CA2011_min = CA2011[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]
#CA2010_min = CA2010[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]
#CA2006_min = CA2006[['SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]


print geocorr_min_new.puma12.nunique()
print CA2014_min['PUMA'].nunique()
print len(CA2014_min)
print '-----------------------------'
print geocorr_min_med.pumaold.nunique()
print CA2010_min['PUMA'].nunique()
print '-----------------------------'
print geocorr_min_old.pumaold.nunique()
print CA2006_min['PUMA'].nunique()


pd.options.display.max_rows = 15
CA2014_min = CA2014_min.sort(['PUMA'], ascending = True)
CA2013_min = CA2013_min.sort(['PUMA'], ascending = True)
CA2012_min = CA2012_min.sort(['PUMA'], ascending = True)
#CA2011_min = CA2011_min.sort(['PUMA'], ascending = True)
#CA2010_min = CA2010_min.sort(['PUMA'], ascending = True)
#CA2006_min = CA2006_min.sort(['PUMA'], ascending = True)

#Count of population in CA:
PopS = geocorr_full14[['Pop 2014 estimate fr county level ests']].sum() # 38,802,499.994
Pop_newS = geocorr_min_new[['TotalPop14']].sum() #38798319.239

#Count of sample size from 2014 CA dataset:
SampS = len(CA2014_min) # 372553
SampS/PopS 

#Count of older adults from 2014 CA sample dataset:
SampOA = len(CA2014_min[CA2014_min['AGEP'] > 73])
SampR = (SampOA*1.0/SampS*1.0) # 0.0679
SampR*Pop_newS # 2,632,807.43 (2,102,746.00 is reported numb +75 CA 2013)

##Connecting SQL

dfs = [CA2014_min, CA2013_min, CA2012_min, CA2011_min, CA2010_min, CA2006_min, geocorr_min_new, geocorr_min_med, geocorr_min_old]
names = ['CA2014_min', 'CA2013_min', 'CA2012_min', 'CA2011_min','CA2010_min','CA2006_min','geocorr_min_new','geocorr_min_med','geocorr_min_old']


#combining geocorr_min w/ rest of csv files using SQLite:
import sqlite3 as sql
import sys

for name,df in zip(names,dfs):
    with sql.connect('SQLcapstone.db') as conn:
        conn.text_factory = str
        df.to_sql(name, conn, flavor='sqlite',if_exists='replace',index=False)

c = conn.cursor()

### 
#import sqlite3 as sql
import sys
#import pandas as pd
#conn = sql.connect('SQLcapstone.db')
#conn.text_factory = str
#c = conn.cursor()


## Puma to Zipcode
#Which zipcodes map to which puma geoloc?
c.execute("""SELECT DISTINCT(zipcode), puma12, pumaold 
                    FROM geocorr_min_med
                    ORDER BY puma12 ASC""")
names = [description[0] for description in c.description]
print names
data = c.fetchall()
zipcode_df = pd.DataFrame(data)
zipcode_df.to_csv('zipcode.csv')
zipcode_df

## maping puma12 to pumaold: Observing puma to zip relationship. These steps are not necessary for results.
PUMA12toZip_dict = {}
for x in range(len(zipcode_df)):
    PUMA = zipcode_df.iloc[x,1]
    zipcode = zipcode_df.iloc[x,0]
    PUMA12toZip_dict.setdefault(PUMA, [])
    PUMA12toZip_dict[PUMA].append(zipcode)
#PUMA12toZip_dictPUMAoldtoZip_dict = {}

for x in range(len(zipcode_df)):
    PUMA = zipcode_df.iloc[x,2]
    zipcode = zipcode_df.iloc[x,0]
    PUMAoldtoZip_dict.setdefault(PUMA, [])
    PUMAoldtoZip_dict[PUMA].append(zipcode)
data = c.fetchall()
#pd.DataFrame(data)

## Creating 2014 table

geocorr_14_df = pd.DataFrame(data, columns=['puma12','pumaold','pumaname','TotalPop14','AF'])
geocorr_14_df.head()#TEST#

c.execute("""SELECT * 
                    FROM geocorr_min_new
                    WHERE puma12 = 3721""")
data = c.fetchall()
#pd.DataFrame(data)
pd.options.display.max_rows = 999
pd.DataFrame(data, columns=['puma12','pumaname','zipcode','zipname','TotalPop14','AF'])
#pd.DataFrame(data)#TEST#

pd.options.display.max_rows = 999
GEO_CA2014_df
GEO_CA2014_df[GEO_CA2014_df['zipcode']].count()
GEO_CA2014_df[GEO_CA2014_df['puma12']== 3721].count()
GEO_CA2014_df[GEO_CA2014_df['zipcode']== 91606].count()

print len(GEO_CA2014_df[(GEO_CA2014_df['puma12'] == 3721) & (GEO_CA2014_df['zipcode']==91606 )])
print len(GEO_CA2014_df[(GEO_CA2014_df['puma12'] == 3721)])
print len(GEO_CA2014_df[(GEO_CA2014_df['zipcode']==91606 )])pd.options.display.max_rows = 15

c.execute("""SELECT * 
                    FROM CA2014_min
                    ORDER BY PUMA ASC""")
data2014 = c.fetchall()
CA2014_min_df = pd.DataFrame(data2014, columns = ['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
#CA2014_min_dfc.execute("""SELECT * 
                    FROM geoCA2014""")
geo2014 = c.fetchall()
names = [description[0] for description in c.description]
print names
GEO_CA2014_df = pd.DataFrame(geo2014, columns = ['puma12','pumaname','zipcode','zipname','TotalPop14','AF','DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
print GEO_CA2014_df['zipcode'].nunique()
print GEO_CA2014_df['puma12'].nunique()


pd.options.display.max_rows = 15
#c.execute("""DROP TABLE geocorr_min_new_sql""")
c.execute("""CREATE TABLE geocorr_min_new_sql AS
                    SELECT puma12, pumaold, pumaname, SUM(TotalPop14) AS TotalPop14, SUM(AF) AS AF  
                    FROM geocorr_min_new
                    GROUP BY puma12
                    ORDER BY puma12 ASC""")
data = c.fetchall()
pd.DataFrame(data)


#c.execute("""DROP table geoCA2014""")
c.execute("""create table geoCA2014 as
                SELECT * FROM geocorr_min_new_sql AS G
                JOIN CA2014_min AS C
                WHERE G.puma12 = C.PUMA
                ORDER BY PUMA ASC""")


#c.execute("""DROP table OA_CA14""")
c.execute("""create table OA_CA14 as 
        SELECT *
        FROM geoCA2014 
        WHERE AGEP >= 64""")

CA2014_min = CA2014[['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P']]


c.execute("""SELECT SERIALNO, PUMA, DIS, DEAR, AGEP, DDRS, DEYE, DOUT, DPHY, DREM
            FROM OA_CA14""")
data=c.fetchall()
names = [description[0] for description in c.description]
print names
OA_CA14_lite = pd.DataFrame(data, columns = ['SERIALNO', 'PUMA', 'DIS', 'DEAR', 'AGEP', 'DDRS', 'DEYE', 'DOUT', 'DPHY', 'DREM'])
OA_CA14_lite.head()



c.execute("""SELECT A.puma,(DEAR_total*1.0/total_count*1.0)*100,(DDRS_total*1.0/total_count*1.0)*100,(DEYE_total*1.0/total_count*1.0)*100,(DOUT_total*1.0/total_count*1.0)*100,(DPHY_total*1.0/total_count*1.0)*100,(DREM_total*1.0/total_count*1.0)*100
             FROM
             (SELECT puma, COUNT(SERIALNO) as total_count FROM OA_CA14 GROUP BY puma) AS X
             JOIN
             (SELECT puma, COUNT(DEAR) as DEAR_total FROM OA_CA14 WHERE DEAR = 1
              GROUP BY puma) AS A
              JOIN
              (SELECT puma, COUNT(DDRS) as DDRS_total FROM OA_CA14 WHERE DDRS = 1
              GROUP BY puma) AS B
              JOIN
              (SELECT puma, COUNT(DEYE) as DEYE_total FROM OA_CA14 WHERE DEYE = 1
              GROUP BY puma) AS C
              JOIN
              (SELECT puma, COUNT(DOUT) as DOUT_total FROM OA_CA14 WHERE DOUT = 1
              GROUP BY puma) AS D
              JOIN
              (SELECT puma, COUNT(DPHY) as DPHY_total FROM OA_CA14 WHERE DPHY = 1
              GROUP BY puma) AS E
              JOIN
              (SELECT puma, COUNT(DREM) as DREM_total FROM OA_CA14 WHERE DREM = 1
              GROUP BY puma) AS F
              ON
              X.puma = A.puma
              AND
              A.puma = B.puma
              AND
              B.puma = C.puma
              AND 
              C.puma = D.puma
              AND 
              D.puma = E.puma
              AND
              E.puma = F.puma""")

data=c.fetchall()
names = [description[0] for description in c.description]
print names
Dis_ratio_Puma = pd.DataFrame(data, columns = ['PUMA', 'DEAR_total', 'DDRS_total', 'DEYE_total', 'DOUT_total', 'DPHY_total', 'DREM_total'])
Dis_ratio_Puma.head()
#len(OA_CA14_lite)


# # Cal total OA Pop 14

# In[55]:

#finding total population per PUMA:
c.execute("""SELECT puma12, pumaold, TotalPop14 as PopTot
                    FROM geocorr_min_new_sql""")
data = c.fetchall()
PopTot14perPuma = pd.DataFrame(data, columns=['PUMA','pumaold', 'PopTotal'])
PopTot14perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampTot
                    FROM geoCA2014
                    GROUP BY puma12""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
SampTot14 = pd.DataFrame(data, columns=['PUMA', 'SampTot'])
SampTot14.head()

# In[46]:

c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampOA, AVG(AGEP)
                    FROM OA_CA14 
                    GROUP BY puma12""")
data = c.fetchall()
TotSampOA14 = pd.DataFrame(data, columns=['PUMA', 'SampOA','AGEP'])
TotSampOA14.head()


# In[27]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb55Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 55 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_55_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_55_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb56Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 56 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_56_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_56_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb57Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 57 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_57_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_57_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb58Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 58 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_58_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_58_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb59Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 59 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_59_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_59_perPuma.head()

# In[28]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb60Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 60 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_60_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_60_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb61Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 61 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_61_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_61_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb62Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 62 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_62_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_62_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb63Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 63 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_63_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_63_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb64Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 64 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_64_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_64_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb65Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 65 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_65_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_65_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb66Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 66 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_66_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_66_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb67Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 67 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_67_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_67_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb68Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 68 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_68_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_68_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb69Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 69 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_69_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_69_perPuma.head()


# In[30]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 70
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_70_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_70_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 71
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_71_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_71_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb72Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 72
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_72_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_72_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb73Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 73
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_73_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_73_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb74Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 74
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_74_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_74_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb75Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 75
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_75_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_75_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb76Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 76
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_76_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_76_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb77Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 77
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_77_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_77_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb78Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 78
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_78_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_78_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb79Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 79
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_79_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_79_perPuma.head()

# In[31]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb80Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 80 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_80_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_80_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb81Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 81 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_81_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_81_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb82Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 82 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_82_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_82_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb83Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 83 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_83_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_83_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb84Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 84 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_84_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_84_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb85Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 85 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_85_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_85_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb86Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 86 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_86_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_86_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb87Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 87 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_87_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_87_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb88Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 88 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_88_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_88_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb89Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 89 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_89_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_89_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb90Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 90 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_90_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_90_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb94Samp, AGEP
                    FROM OA_CA14
                    WHERE AGEP = 94 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA14_94_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA14_94_perPuma.head()


#Defining OA as +74:
frames14 = [SampPopOA14_74_perPuma,
    SampPopOA14_75_perPuma,SampPopOA14_76_perPuma,SampPopOA14_77_perPuma,SampPopOA14_78_perPuma,
    SampPopOA14_79_perPuma,SampPopOA14_80_perPuma,SampPopOA14_81_perPuma,SampPopOA14_82_perPuma,
    SampPopOA14_83_perPuma,SampPopOA14_84_perPuma,SampPopOA14_85_perPuma,SampPopOA14_86_perPuma,
    SampPopOA14_87_perPuma,SampPopOA14_88_perPuma,SampPopOA14_89_perPuma,
    SampPopOA14_90_perPuma,SampPopOA14_94_perPuma]
CountOA14 = pd.concat(frames14)

#keeping OA from 55 on for later analyses:
frames14 = [SampPopOA14_55_perPuma,SampPopOA14_56_perPuma,SampPopOA14_57_perPuma,SampPopOA14_58_perPuma,
    SampPopOA14_59_perPuma,SampPopOA14_60_perPuma,SampPopOA14_61_perPuma,SampPopOA14_62_perPuma,
    SampPopOA14_63_perPuma,SampPopOA14_64_perPuma,SampPopOA14_65_perPuma,SampPopOA14_66_perPuma,
    SampPopOA14_67_perPuma,SampPopOA14_68_perPuma,SampPopOA14_69_perPuma,SampPopOA14_70_perPuma,
    SampPopOA14_71_perPuma,SampPopOA14_72_perPuma,SampPopOA14_73_perPuma,SampPopOA14_74_perPuma,
    SampPopOA14_75_perPuma,SampPopOA14_76_perPuma,SampPopOA14_77_perPuma,SampPopOA14_78_perPuma,
    SampPopOA14_79_perPuma,SampPopOA14_80_perPuma,SampPopOA14_81_perPuma,SampPopOA14_82_perPuma,
    SampPopOA14_83_perPuma,SampPopOA14_84_perPuma,SampPopOA14_85_perPuma,SampPopOA14_86_perPuma,
    SampPopOA14_87_perPuma,SampPopOA14_88_perPuma,SampPopOA14_89_perPuma,
    SampPopOA14_90_perPuma,SampPopOA14_94_perPuma]
CountOA14 = pd.concat(frames14)

print len(CountOA14)
print len(SampPopOA14_89_perPuma)
# In[63]:

import numpy as np
#Merging Totals datasets:
PopSampTot14 = pd.merge(PopTot14perPuma,SampTot14, on=['PUMA'])

#renaming dataset for congruency:
CountOA14 = CountOA14.rename(index=None, columns = {'PUMA':'PUMA','SampPop':'SampOA','AGEP':'AGEP'})

#Adding year and merging to dataset:
year = [2014] * 9654
year_df = pd.DataFrame(year, columns = ['year'])
Counts_14 = CountOA14.join(year_df)    #SampOA count = 27556, check 

#Merging OA dataset with Totals datasets:
Counts_14_PopSampOA = pd.merge(Counts_14,PopSampTot14,how='left',on=['PUMA'])

#Making full table:
#sum OAtot = 2,856,634.13... checkish (2,869,729)
OAtot = (Counts_14_PopSampOA.SampOA/Counts_14_PopSampOA.SampTot)*Counts_14_PopSampOA.PopTotal
OAtot_df = pd.DataFrame(OAtot, columns = ['OAtot'])
Table14 = Counts_14_PopSampOA.join(OAtot_df)
Table14_final = Table14[['PUMA','pumaold','AGEP','year','OAtot']] #OAtot = 2,856,634.13, checkish
Table14_final



ZipCalc_all[ZipCalc_all['PUMA']==102] #PopTotal looks good
ZipCalc_all2
wOAtot_df[['OAtot']].sum() # 2,856,634.13, looks good
OATotpuma_df
#wOAtot_df[wOAtot_df['PUMA']==300] #20384.717598, check
OAPopzip_df[['OAPopzip']].sum() #2,856,627 check
OAPopzip_df
ZipCalc_all3[['OAPopzip']].sum() #2856627, check


#ZipCalc_all = pd.merge(ZipCalc_new,PopSampTot14_new,how='left',on=['PUMA'])

#creating df w/ Pop total per zip and pop total per puma:
Zip_Pop_df = geocorr_min_new[['zipcode','TotalPop14','puma12']] 
Zip_Pop_df = Zip_Pop_df.rename(index=None, columns={'puma12':'PUMA','TotalPop14':'PopTotzip','zipcode':'zipcode'})
Zip_Pop_df = Zip_Pop_df.groupby(['zipcode','PUMA']).agg({'PopTotzip': np.sum}).reset_index()
# PopTotzip = 38,798,319.239, check
ZipCalc_all = pd.merge(Zip_Pop_df,PopSampTot14,on=['PUMA'])
ZipCalc_all.head()

ratio_df = pd.DataFrame(ZipCalc_all.PopTotzip/ZipCalc_all.PopTotal,columns=['ratio'])
ZipCalc_all2 = ZipCalc_all.join(ratio_df)
ZipCalc_all2

#computing numb OA per zip:
wOAtot_df = Table14_final.groupby('PUMA').agg({'OAtot': np.sum}).reset_index()

OATotpuma_df = pd.merge(ZipCalc_all2, wOAtot_df, on = ['PUMA'])
OATotpuma_df

OAPopzip_df = np.round(pd.DataFrame(OATotpuma_df.ratio*OATotpuma_df.OAtot, columns=['OAPopzip']))
OAPopzip_df
ZipCalc_all3 = ZipCalc_all2.join(OAPopzip_df)
ZipCalc_all3.head() #looks good, OAPopzip.sum() = 2856627



Dis_2ratio = pd.merge(ZipCalc_all3,Dis_ratio_Puma, on=['PUMA'])
Dis_2ratio_lite = Dis_2ratio[['zipcode','PUMA','ratio','DEAR_total','DDRS_total','DEYE_total','DOUT_total','DPHY_total','DREM_total']]
Dis_2ratio_lite



Dis_zip = []
#new_df = Dis_2ratio_lite[['zipcode','PUMA']]
for col in Dis_2ratio_lite:
    if(col != 'zipcode' and col != 'PUMA' and col != 'ratio'):
        dfx = pd.DataFrame(Dis_2ratio_lite[col] * Dis_2ratio_lite.ratio, columns=[col])
        Dis_zip.append(dfx)
Dis_zip.append(pd.DataFrame(Dis_2ratio_lite['zipcode']))
Dis_zip.append(pd.DataFrame(Dis_2ratio_lite['PUMA']))
Dis_zip
Dis_zip_df = Dis_zip[0].join(Dis_zip[1:])

#List comprehension method (not complete): 
#cols = [pd.DataFrame(Dis_2ratio_lite[col] * Dis_2ratio_lite.ratio, columns=[col]) for col in Dis_2ratio_lite]



dfs3 = [Dis_zip_df]
names3 = ['Dis_zip_df']

import sqlite3 as sql
import sys

for name,df in zip(names3,dfs3):
    with sql.connect('Dis_zip_df.db') as conn:
        conn.text_factory = str
        df.to_sql(name, conn, flavor='sqlite',if_exists='replace',index=False)

c = conn.cursor()
conn.text_factory = str



c.execute("""SELECT zipcode, SUM(DEAR_total),SUM(DDRS_total),SUM(DEYE_total),
            SUM(DOUT_total),SUM(DPHY_total),SUM(DREM_total) FROM Dis_zip_df
            GROUP BY zipcode""")
names = [description[0] for description in c.description]
print names
data = c.fetchall()
#pd.DataFrame(data)
Dis_zip_final_df = pd.DataFrame(data, columns = ['zipcode', 'SUM(DEAR_total)', 'SUM(DDRS_total)', 'SUM(DEYE_total)', 'SUM(DOUT_total)', 'SUM(DPHY_total)', 'SUM(DREM_total)'])
Dis_zip_final_df
#Dis_zip_final_df.to_csv("OAxZip_final.csv")



#creating a df that signifies typical disability per zipcode:
disability_ar = []
zipcode_ar = []
max_col_ar = []
for i,row in Dis_zip_final_df.iterrows():
    max_col = row[1]
    diability = 'Hearing'
    #print max_col
    if(max_col < row[2]):
        max_col = row[2]
        disability = 'Self-care'
    if(max_col < row[3]):
        max_col = row[3]
        disability = 'Vision'
    if(max_col < row[4]):
        max_col = row[4]
        disability = 'Indep. living'
    if(max_col < row[5]):
        max_col = row[5]
        disability = 'Ambulatory'
    if(max_col < row[6]):
        max_col = row[6]
        disability = 'Cognitive'
    zipcode_ar.append(row[0])
    disability_ar.append(disability)
    max_col_ar.append(max_col)

dftest = pd.DataFrame({'zipcode':zipcode_ar,'disability':disability_ar,'max':max_col_ar})
dftest.to_csv('disability.csv')



PopTot14perPuma[['PopTotal']].sum() # looks good
SampTot14[['SampTot']].sum() # looks good: 372,553
CountOA14[['SampOA']].sum() # looks good: 27556



OA_agg_T14 = Table14_final.groupby('PUMA').agg({'OAtot': np.sum})
#check OAall = PopOA 2,856,634.13
OA_agg_T14 = OA_agg_T14.rename(index = None, columns={'OAtot':'OAall'}).reset_index()

OAagePuma = pd.merge(OA_agg_T14,Table14_final, how='left', on=['PUMA'])

ratio_OAxOAtot_df = pd.DataFrame(OAagePuma.OAtot/OAagePuma.OAall, columns=['ratio_OAxOAtot_PUMA'])
#check OAtot.sum() = 2856634.131185
OAagePuma = OAagePuma.join(ratio_OAxOAtot_df)

#pd.options.display.max_rows = 30
OAagePuma.head()
#OAagePuma[OAagePuma['PUMA']==101]


Map14 = ZipCalc_all3[['zipcode','OAPopzip','PUMA']]
Map14test = Map14.groupby(['zipcode'],as_index=False).agg({'OAPopzip':np.sum})
Map14test2 = Map14.groupby(['zipcode','PUMA']).agg({'OAPopzip':np.sum}).reset_index()
Map14test2.head() #check OAPopzip = 2856627.0


#need to remove duplicate rows from below table:
Map14test3 = pd.merge(Map14test,Map14test2, on=['zipcode'])
Map14test4 = Map14test3[['zipcode','OAPopzip_x','PUMA']]
#Map14test4 = Map14test4.groupby(['zipcode'])
Map14test4[['OAPopzip_x']] #(inflated)

#Tried using SQlite but did not support outer join: 
dfs2 = [ZipCalc_all3, OAagePuma]
names2 = ['ZipCalc_all3','OAagePuma']

import sqlite3 as sql
import sys

for name,df in zip(names2,dfs2):
    with sql.connect('OA_zipPuma.db') as conn:
        conn.text_factory = str
        df.to_sql(name, conn, flavor='sqlite',if_exists='replace',index=False)

c = conn.cursor()

c.execute("""SELECT AGEP, zipcode, ZCA3.PUMA, (ratio_OAxOAtot_PUMA*OAPopzip) AS OAbyZipcode   
             FROM ZipCalc_all3 AS ZCA3
             OUTER JOIN OAagePuma AS OAxP
             ON ZCA3.PUMA = OAxP.PUMA""")


OAagePuma.head()
OAagePum_lite = OAagePuma[['PUMA','AGEP','ratio_OAxOAtot_PUMA']]
OAagePum_lite #len =4620


pd.options.display.max_rows = 10
testx = pd.merge(Map14test4,OAagePum_lite,on=['PUMA'])
OAx_Zip_df = pd.DataFrame((1.0*testx.OAPopzip_x)*testx.ratio_OAxOAtot_PUMA, columns=['OAx_Zip'])
Final = testx.join(np.round(OAx_Zip_df))
Final[['OAx_Zip']].sum()  #inflated: 5,535,165 (but this is ok, bc some are doubled up)
pd.options.display.max_rows = 55
OA_zip_Count14 = Final.groupby(['zipcode','AGEP','PUMA','OAPopzip_x']).agg({'OAx_Zip':np.sum}).reset_index()



pd.options.display.max_rows = 55
OA_zip_Count14 = Final.groupby(['zipcode','AGEP','PUMA','OAPopzip_x']).agg({'OAx_Zip':np.sum}).reset_index()



dfs2 = [OA_zip_Count14]
names2 = ['OA_zip_Count14']

import sqlite3 as sql
import sys

for name,df in zip(names2,dfs2):
    with sql.connect('OA_zipFinal_use1.db') as conn:
        conn.text_factory = str
        df.to_sql(name, conn, flavor='sqlite',if_exists='replace',index=False)

c = conn.cursor()
conn.text_factory = str


c.execute("""SELECT zipcode, AGEP, max(OAx_Zip), OAPopzip_x
             FROM OA_zip_Count14
             GROUP by zipcode""")

names = [description[0] for description in c.description]
print names
data = c.fetchall()
FF = pd.DataFrame(data, columns = ['zipcode', 'AGEP', 'max(OAx_Zip)', 'OAPopzip_x'])
FF[['OAPopzip_x']].sum() #2,856,627: numb we want!


Count_OAx_dis = pd.merge(FF,dftest,on=['zipcode'])
sorted(Count_OAx_dis['AGEP'].unique())
#Count_OAx_dis.to_csv("Count_OAx_dis.csv")

#Finished. Above code will create the 3 maps I need. 1. Density per zip 2. Typical age 3. Typical disability



## Creating 2013 table:

# In[136]:

#c.execute("""DROP table geoCA2013""")
c.execute("""create table geoCA2013 as
                SELECT * FROM geocorr_min_new_sql AS G
                JOIN CA2013_min AS C
                WHERE G.puma12 = C.PUMA
                ORDER BY PUMA ASC""")


# In[359]:

c.execute("""DROP table OA_CA13""")
c.execute("""create table OA_CA13 as 
        SELECT *
        FROM geoCA2013 
        WHERE AGEP >= 55""")


# In[35]:

#finding total population per PUMA:
c.execute("""SELECT puma12, pumaold, TotalPop14 as PopTot
                    FROM geocorr_min_new_sql
                    GROUP BY puma12""")
data = c.fetchall()
PopTot13perPuma = pd.DataFrame(data, columns=['PUMA','pumaold', 'PopTotal'])
PopTot13perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampTot
                    FROM geoCA2013
                    GROUP BY puma12""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
SampTot13 = pd.DataFrame(data, columns=['PUMA', 'SampTot'])
SampTot13.head()

# In[46]:

c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampOA, AVG(AGEP)
                    FROM OA_CA13 
                    GROUP BY puma12""")
data = c.fetchall()
TotSampOA13 = pd.DataFrame(data, columns=['PUMA', 'SampOA','AGEP'])
TotSampOA13.head()


# In[27]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb55Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 55 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_55_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_55_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb56Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 56 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_56_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_56_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb57Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 57 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_57_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_57_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb58Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 58 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_58_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_58_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb59Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 59 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_59_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_59_perPuma.head()

# In[28]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb60Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 60 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_60_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_60_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb61Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 61 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_61_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_61_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb62Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 62 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_62_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_62_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb63Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 63 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_63_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_63_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb64Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 64 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_64_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_64_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb65Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 65 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_65_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_65_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb66Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 66 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_66_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_66_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb67Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 67 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_67_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_67_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb68Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 68 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_68_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_68_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb69Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 69 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_69_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_69_perPuma.head()


# In[30]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 70
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_70_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_70_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 71
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_71_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_71_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb72Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 72
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_72_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_72_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb73Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 73
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_73_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_73_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb74Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 74
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_74_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_74_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb75Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 75
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_75_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_75_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb76Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 76
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_76_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_76_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb77Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 77
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_77_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_77_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb78Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 78
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_78_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_78_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb79Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 79
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_79_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_79_perPuma.head()

# In[31]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb80Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 80 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_80_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_80_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb81Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 81 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_81_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_81_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb82Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 82 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_82_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_82_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb83Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 83 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_83_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_83_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb84Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 84 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_84_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_84_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb85Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 85 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_85_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_85_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb86Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 86 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_86_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_86_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb87Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 87 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_87_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_87_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb88Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 88 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_88_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_88_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb89Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 89 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_89_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_89_perPuma.head()

# In[33]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb90Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 90 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_90_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_90_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb94Samp, AGEP
                    FROM OA_CA13
                    WHERE AGEP = 94 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA13_94_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA13_94_perPuma.head()


# In[361]:

print sorted(CA2013_min['AGEP'].unique())


# In[36]:

frames13 = [SampPopOA13_64_perPuma,SampPopOA13_65_perPuma,SampPopOA13_66_perPuma,
    SampPopOA13_67_perPuma,SampPopOA13_68_perPuma,SampPopOA13_69_perPuma,SampPopOA13_70_perPuma,
    SampPopOA13_71_perPuma,SampPopOA13_72_perPuma,SampPopOA13_73_perPuma,SampPopOA13_74_perPuma,
    SampPopOA13_75_perPuma,SampPopOA13_76_perPuma,SampPopOA13_77_perPuma,SampPopOA13_78_perPuma,
    SampPopOA13_79_perPuma,SampPopOA13_80_perPuma,SampPopOA13_81_perPuma,SampPopOA13_82_perPuma,
    SampPopOA13_83_perPuma,SampPopOA13_84_perPuma,SampPopOA13_85_perPuma,SampPopOA13_86_perPuma,
    SampPopOA13_87_perPuma,SampPopOA13_88_perPuma,SampPopOA13_89_perPuma,
    SampPopOA13_90_perPuma,SampPopOA13_94_perPuma]
CountOA13 = pd.concat(frames13)

print len(CountOA13)
print len(SampPopOA13_89_perPuma)

frames13 = [SampPopOA13_55_perPuma,SampPopOA13_56_perPuma,SampPopOA13_57_perPuma,SampPopOA13_58_perPuma,
    SampPopOA13_59_perPuma,SampPopOA13_60_perPuma,SampPopOA13_61_perPuma,SampPopOA13_62_perPuma,
    SampPopOA13_63_perPuma,SampPopOA13_64_perPuma,SampPopOA13_65_perPuma,SampPopOA13_66_perPuma,
    SampPopOA13_67_perPuma,SampPopOA13_68_perPuma,SampPopOA13_69_perPuma,SampPopOA13_70_perPuma,
    SampPopOA13_71_perPuma,SampPopOA13_72_perPuma,SampPopOA13_73_perPuma,SampPopOA13_74_perPuma,
    SampPopOA13_75_perPuma,SampPopOA13_76_perPuma,SampPopOA13_77_perPuma,SampPopOA13_78_perPuma,
    SampPopOA13_79_perPuma,SampPopOA13_80_perPuma,SampPopOA13_81_perPuma,SampPopOA13_82_perPuma,
    SampPopOA13_83_perPuma,SampPopOA13_84_perPuma,SampPopOA13_85_perPuma,SampPopOA13_86_perPuma,
    SampPopOA13_87_perPuma,SampPopOA13_88_perPuma,SampPopOA13_89_perPuma,
    SampPopOA13_90_perPuma,SampPopOA13_94_perPuma]
CountOA13 = pd.concat(frames13)

print len(CountOA13)
print len(SampPopOA13_89_perPuma)
# In[37]:

#Merging Totals datasets:
PopSampTot13 = pd.merge(PopTot13perPuma,SampTot13, on=['PUMA'])

#renaming dataset for congruency:
CountOA13 = CountOA13.rename(index=None, columns = {'PUMA':'PUMA','SampPop':'SampOA','AGEP':'AGEP'})

#Adding year and merging to dataset:
year = [2013] * 9654
year_df = pd.DataFrame(year, columns = ['year'])
Counts_13 = CountOA13.join(year_df)

#Merging OA dataset with Totals datasets:
Counts_13_PopSampOA = pd.merge(Counts_13,PopSampTot13,how='left',on=['PUMA'])

#Making full table:
OAtot = (Counts_13_PopSampOA.SampOA/Counts_13_PopSampOA.SampTot)*Counts_13_PopSampOA.PopTotal
OAtot_df = pd.DataFrame(OAtot, columns = ['OAtot'])
Table13 = Counts_13_PopSampOA.join(OAtot_df)
Table13


# In[ ]:




# # Creating 2012 table:

# In[38]:

c.execute("""DROP table geoCA2012""")
c.execute("""create table geoCA2012 as
                SELECT * FROM geocorr_min_new_sql AS G
                JOIN CA2012_min AS C
                WHERE G.puma12 = C.PUMA
                ORDER BY PUMA ASC""")

c.execute("""DROP table OA_CA12""")
c.execute("""create table OA_CA12 as 
        SELECT *
        FROM geoCA2012 
        WHERE AGEP >= 55""")


# In[39]:

#finding total population per PUMA:
c.execute("""SELECT puma12, pumaold, TotalPop14 as PopTot
                    FROM geocorr_min_new_sql
                    GROUP BY puma12""")
data = c.fetchall()
PopTot12perPuma = pd.DataFrame(data, columns=['PUMA','pumaold', 'PopTotal'])
PopTot12perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampTot
                    FROM geoCA2012
                    GROUP BY puma12""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
SampTot12 = pd.DataFrame(data, columns=['PUMA', 'SampTot'])
SampTot12.head()

# In[46]:

c.execute("""SELECT puma12, COUNT(SERIALNO) AS SampOA, AVG(AGEP)
                    FROM OA_CA12 
                    GROUP BY puma12""")
data = c.fetchall()
TotSampOA12 = pd.DataFrame(data, columns=['PUMA', 'SampOA','AGEP'])
TotSampOA12.head()


# In[27]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb55Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 55 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_55_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_55_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb56Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 56 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_56_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_56_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb57Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 57 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_57_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_57_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb58Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 58 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_58_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_58_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb59Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 59 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_59_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_59_perPuma.head()

# In[28]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb60Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 60 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_60_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_60_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb61Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 61 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_61_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_61_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb62Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 62 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_62_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_62_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb63Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 63 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_63_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_63_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb64Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 64 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_64_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_64_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb65Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 65 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_65_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_65_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb66Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 66 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_66_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_66_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb67Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 67 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_67_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_67_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb68Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 68 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_68_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_68_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb69Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 69 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_69_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_69_perPuma.head()


# In[30]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 70
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_70_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_70_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 71
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_71_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_71_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb72Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 72
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_72_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_72_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb73Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 73
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_73_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_73_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb74Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 74
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_74_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_74_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb75Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 75
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_75_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_75_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb76Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 76
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_76_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_76_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb77Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 77
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_77_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_77_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb78Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 78
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_78_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_78_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb79Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 79
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_79_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_79_perPuma.head()

# In[31]:

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb80Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 80 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_80_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_80_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb81Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 81 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_81_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_81_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb82Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 82 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_82_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_82_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb83Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 83 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_83_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_83_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb84Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 84 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_84_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_84_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb85Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 85 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_85_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_85_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb86Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 86 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_86_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_86_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb87Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 87 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_87_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_87_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb88Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 88 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_88_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_88_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb89Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 89 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_89_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_89_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT puma12, COUNT(SERIALNO) AS Numb94Samp, AGEP
                    FROM OA_CA12
                    WHERE AGEP = 93 
                    GROUP BY puma12""")
data = c.fetchall()
SampPopOA12_93_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA12_93_perPuma.head()


# In[40]:

print sorted(CA2012_min['AGEP'].unique())


# In[43]:

frames12 = [SampPopOA12_64_perPuma,SampPopOA12_65_perPuma,SampPopOA12_66_perPuma,
    SampPopOA12_67_perPuma,SampPopOA12_68_perPuma,SampPopOA12_69_perPuma,SampPopOA12_70_perPuma,
    SampPopOA12_71_perPuma,SampPopOA12_72_perPuma,SampPopOA12_73_perPuma,SampPopOA12_74_perPuma,
    SampPopOA12_75_perPuma,SampPopOA12_76_perPuma,SampPopOA12_77_perPuma,SampPopOA12_78_perPuma,
    SampPopOA12_79_perPuma,SampPopOA12_80_perPuma,SampPopOA12_81_perPuma,SampPopOA12_82_perPuma,
    SampPopOA12_83_perPuma,SampPopOA12_84_perPuma,SampPopOA12_85_perPuma,SampPopOA12_86_perPuma,
    SampPopOA12_87_perPuma,SampPopOA12_88_perPuma,SampPopOA12_89_perPuma,SampPopOA12_93_perPuma]
CountOA12 = pd.concat(frames12)

print len(CountOA12)
SampPopOA12_89_perPuma

frames12 = [SampPopOA12_55_perPuma,SampPopOA12_56_perPuma,SampPopOA12_57_perPuma,SampPopOA12_58_perPuma,
    SampPopOA12_59_perPuma,SampPopOA12_60_perPuma,SampPopOA12_61_perPuma,SampPopOA12_62_perPuma,
    SampPopOA12_63_perPuma,SampPopOA12_64_perPuma,SampPopOA12_65_perPuma,SampPopOA12_66_perPuma,
    SampPopOA12_67_perPuma,SampPopOA12_68_perPuma,SampPopOA12_69_perPuma,SampPopOA12_70_perPuma,
    SampPopOA12_71_perPuma,SampPopOA12_72_perPuma,SampPopOA12_73_perPuma,SampPopOA12_74_perPuma,
    SampPopOA12_75_perPuma,SampPopOA12_76_perPuma,SampPopOA12_77_perPuma,SampPopOA12_78_perPuma,
    SampPopOA12_79_perPuma,SampPopOA12_80_perPuma,SampPopOA12_81_perPuma,SampPopOA12_82_perPuma,
    SampPopOA12_83_perPuma,SampPopOA12_84_perPuma,SampPopOA12_85_perPuma,SampPopOA12_86_perPuma,
    SampPopOA12_87_perPuma,SampPopOA12_88_perPuma,SampPopOA12_89_perPuma,SampPopOA12_93_perPuma]
CountOA12 = pd.concat(frames12)

print len(CountOA12)
print len(SampPopOA12_89_perPuma)
# In[44]:

#Merging Totals datasets:
PopSampTot12 = pd.merge(PopTot12perPuma,SampTot12, on=['PUMA'])

#renaming dataset for congruency:
CountOA12 = CountOA12.rename(index=None, columns = {'PUMA':'PUMA','SampPop':'SampOA','AGEP':'AGEP'})

#Adding year and merging to dataset:
year = [2012] * 9654
year_df = pd.DataFrame(year, columns = ['year'])
Counts_12 = CountOA12.join(year_df)

#Merging OA dataset with Totals datasets:
Counts_12_PopSampOA = pd.merge(Counts_12,PopSampTot12,how='left',on=['PUMA'])

#Making full table:
OAtot = (Counts_12_PopSampOA.SampOA/Counts_12_PopSampOA.SampTot)*Counts_12_PopSampOA.PopTotal
OAtot_df = pd.DataFrame(OAtot, columns = ['OAtot'])
Table12 = Counts_12_PopSampOA.join(OAtot_df)
Table12.head()


# # Running linear regression:

# In[45]:

#Concat tables together on PUMA:
Full_frames = [Table14,Table13,Table12]
Full_table_df = pd.concat(Full_frames)
Full_table_df.head() #Where y is OAtot Do not need PopT, SampT, SampOA

Final_test_df = Full_table_df[['PUMA','AGEP','year','OAtot']]
Final_test_df.head()


# In[46]:

X = Final_test_df[['PUMA','AGEP','year']]
y = Final_test_df[['OAtot']]


# In[47]:

import numpy as np
import scipy as sp
import sklearn as sk
from sklearn.linear_model import LinearRegression 
from sklearn.cross_validation import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linreg = LinearRegression(fit_intercept=True)
model = linreg.fit(X_train, y_train)
y_pred = model.predict(X_test)
print model.score(X_test, y_test)


print('Coefficients: \n', linreg.coef_)
print("Residual sum of squares: %.2f" % np.mean((linreg.predict(X_test) - y_test) ** 2))
print('Variance score: %.2f' % linreg.score(X_test, y_test))

print y.var()
#print compute_error(linreg, X, y)


# # Creating 2010 table:

# In[46]:

pd.options.display.max_rows = 15

c.execute("""SELECT * 
                    FROM geocorr_min_med
                    ORDER BY puma12 ASC""")
data = c.fetchall()
#pd.DataFrame(data)
geocorr_10_df = pd.DataFrame(data, columns=['puma12','pumaold','pumaname','zipcode','zipname','TotalPop10','AF'])
geocorr_10_df.head()
print geocorr_10_df['zipcode'].nunique()
print geocorr_10_df['pumaold'].nunique()


# In[75]:

#finding total population per PUMA:
c.execute("""SELECT puma12, pumaold, SUM(TotalPop10) as PopTot10
                    FROM geocorr_min_med
                    GROUP BY pumaold""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
PopTot10perPuma = pd.DataFrame(data, columns=['PUMAnew','PUMA', 'PopTotal'])
PopTot10perPuma.head()


# In[47]:

pd.options.display.max_rows = 15

c.execute("""SELECT * 
                    FROM CA2010_min
                    ORDER BY PUMA ASC""")
data2010 = c.fetchall()
CA2010_min_df = pd.DataFrame(data2010, columns = ['DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
print CA2010_min_df['PUMA'].nunique()


# In[ ]:

c.execute("""DROP table geoCA2010""")
c.execute("""create table geoCA2010 as
                SELECT * FROM geocorr_min_med AS G
                JOIN CA2010_min AS C
                WHERE G.pumaold = C.PUMA""")


# In[ ]:

c.execute("""SELECT * 
                    FROM geoCA2010""")
geo2010 = c.fetchall()
names = [description[0] for description in c.description]
print names
GEO_CA2010_df = pd.DataFrame(geo2010, columns = ['puma12','pumaold','pumaname','zipcode','zipname','TotalPop10','AF','DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
print GEO_CA2010_df['zipcode'].nunique()
print GEO_CA2010_df['pumaold'].nunique()


# In[58]:

c.execute("""DROP table OA_CA10""") 
c.execute("""create table OA_CA10 as 
        SELECT *
        FROM geoCA2010 
        WHERE AGEP >= 55""")


# # Cal total OA Pop 10

# In[258]:

#finding total population per PUMA:
c.execute("""SELECT pumaold, SUM(TotalPop10) as PopTot
                    FROM geocorr_min_med
                    GROUP BY pumaold""")
data = c.fetchall()
PopTot10perPuma = pd.DataFrame(data, columns=['PUMA', 'PopTotal'])
PopTot10perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS SampTot, AVG(AGEP)
                    FROM geoCA2010
                    GROUP BY pumaold""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
SampTot10 = pd.DataFrame(data, columns=['PUMA', 'SampTot','AGEP'])
SampTot10.head()

# In[46]:

c.execute("""SELECT pumaold, COUNT(SERIALNO) AS SampOA, AVG(AGEP)
                    FROM OA_CA10 
                    GROUP BY pumaold""")
data = c.fetchall()
TotSampOA10 = pd.DataFrame(data, columns=['PUMA', 'SampOA','AGEP'])
TotSampOA10.head()


# In[27]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb55Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 55 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_55_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_55_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb56Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 56 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_56_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_56_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb57Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 57 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_57_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_57_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb58Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 58 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_58_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_58_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb59Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 59 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_59_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_59_perPuma.head()

# In[28]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb60Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 60 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_60_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_60_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb61Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 61 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_61_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_61_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb62Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 62 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_62_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_62_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb63Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 63 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_63_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_63_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb64Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 64 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_64_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_64_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb65Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 65 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_65_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_65_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb66Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 66 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_66_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_66_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb67Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 67 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_67_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_67_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb68Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 68 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_68_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_68_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb69Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 69 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_69_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_69_perPuma.head()


# In[30]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 70
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_70_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_70_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 71
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_71_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_71_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb72Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 72
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_72_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_72_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb73Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 73
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_73_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_73_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb74Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 74
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_74_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_74_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb75Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 75
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_75_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_75_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb76Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 76
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_76_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_76_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb77Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 77
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_77_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_77_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb78Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 78
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_78_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_78_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb79Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 79
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_79_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_79_perPuma.head()

# In[31]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb80Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 80 
                    GROUP BY pumaold""")
SampPopOA10_80_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_80_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb81Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 81 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_81_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_81_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb82Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 82 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_82_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_82_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb83Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 83 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_83_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_83_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb84Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 84 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_84_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_84_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb85Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 85 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_85_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_85_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb86Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 86 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_86_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_86_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb87Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 87 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_87_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_87_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb88Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 88 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_88_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_88_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb89Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 89 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_89_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_89_perPuma.head()

# In[33]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb90Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 90 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_90_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_90_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb91Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 91 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_91_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_91_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb92Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 92 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_92_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_92_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb93Samp, AGEP
                    FROM OA_CA10
                    WHERE AGEP = 93 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA10_93_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA10_93_perPuma.head()


# In[263]:

print sorted(CA2010_min['AGEP'].unique())


# In[264]:

frames10 = [SampPopOA10_55_perPuma,SampPopOA10_56_perPuma,SampPopOA10_57_perPuma,SampPopOA10_58_perPuma,
    SampPopOA10_59_perPuma,SampPopOA10_60_perPuma,SampPopOA10_61_perPuma,SampPopOA10_62_perPuma,
    SampPopOA10_63_perPuma,SampPopOA10_64_perPuma,SampPopOA10_65_perPuma,SampPopOA10_66_perPuma,
    SampPopOA10_67_perPuma,SampPopOA10_68_perPuma,SampPopOA10_69_perPuma,SampPopOA10_70_perPuma,
    SampPopOA10_71_perPuma,SampPopOA10_72_perPuma,SampPopOA10_73_perPuma,SampPopOA10_74_perPuma,
    SampPopOA10_75_perPuma,SampPopOA10_76_perPuma,SampPopOA10_77_perPuma,SampPopOA10_78_perPuma,
    SampPopOA10_79_perPuma,SampPopOA10_80_perPuma,SampPopOA10_81_perPuma,SampPopOA10_82_perPuma,
    SampPopOA10_83_perPuma,SampPopOA10_84_perPuma,SampPopOA10_85_perPuma,SampPopOA10_86_perPuma,
    SampPopOA10_87_perPuma,SampPopOA10_88_perPuma,SampPopOA10_89_perPuma,
    SampPopOA10_93_perPuma]
CountOA10 = pd.concat(frames10)


# In[265]:

CountOA10

#Merged Samp datasets 2014:
result0 = pd.merge(SampPopOA10_85to90_perPuma,SampPopOA10_90to95_perPuma, 
                   on=['PUMA'])
result1=pd.merge(SampPopOA10_80to85_perPuma,result0,on=['PUMA'])
result2=pd.merge(SampPopOA10_75to80_perPuma,result1,on=['PUMA'])
result3=pd.merge(SampPopOA10_70to75_perPuma,result2,on=['PUMA'])
result4=pd.merge(SampPopOA10_65to70_perPuma,result3,on=['PUMA'])
result5=pd.merge(SampPopOA10_60to65_perPuma,result4,on=['PUMA'])
result6=pd.merge(SampPopOA10_55to60_perPuma,result5,on=['PUMA'])
result7=pd.merge(TotSampOA10,result6,on=['PUMA'])
result8=pd.merge(SampTot10,result7,on=['PUMA'])
CountsPUMA10=pd.merge(PopTot10perPuma,result8,on=['PUMA'])

CountsPUMA10.head()
CountsPUMA10_final = CountsPUMA10.rename(index=None, columns={'PUMA':'PUMA', 'PopTotal':'PopTotal_10', 'SampTot':'SampTot_10', 'SampOA':'SampOA_10', 'SampPop55_60':'SampPop55_60_10', 'SampPop60_65':'SampPop60_65_10', 'SampPop65_70':'SampPop65_70_10', 'SampPop70_75':'SampPop70_75_10', 'SampPop75_80':'SampPop75_80_10', 'SampPop80_85':'SampPop80_85_10', 'SampPop85_90':'SampPop85_90_10', 'SampPop90_95':'SampPop90_95_10'})
# # Creating 2006 table:

# In[79]:

pd.options.display.max_rows = 15

c.execute("""SELECT * 
                    FROM geocorr_min_old
                    ORDER BY pumaold ASC""")
data = c.fetchall()
#pd.DataFrame(data)
geocorr_00_df = pd.DataFrame(data, columns=['pumaold','pumaname','zipcode','zipname','TotalPop00','AF'])
geocorr_00_df.head()


# In[80]:

pd.options.display.max_rows = 15

c.execute("""SELECT * 
                    FROM CA2006_min
                    ORDER BY PUMA ASC""")
data2006 = c.fetchall()
CA2006_min_df = pd.DataFrame(data2006, columns = ['SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])


# In[ ]:

c.execute("""DROP table geoCA2006""")


# In[81]:

c.execute("""DROP table geoCA2006""")
c.execute("""create table geoCA2006 as
                SELECT * FROM geocorr_min_old AS G
                JOIN CA2006_min AS C
                WHERE G.pumaold = C.PUMA""")


# In[ ]:

c.execute("""SELECT * 
                    FROM geoCA2006""")
geo2006 = c.fetchall()
names = [description[0] for description in c.description]
print names
GEO_CA2006_df = pd.DataFrame(geo2006, columns = ['pumaold','pumaname','zipcode','zipname','TotalPop00','AF','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
print GEO_CA2006_df['zipcode'].nunique()
print GEO_CA2006_df['pumaold'].nunique()


# In[ ]:

GEO_CA2006_df.head()


# In[ ]:

c.execute("""DROP table OA_CA06""") 


# In[82]:

c.execute("""DROP table OA_CA06""") 
c.execute("""create table OA_CA06 as 
        SELECT *
        FROM geoCA2006 
        WHERE AGEP >= 55""")


# # Cal total OA Pop 06

# In[260]:

#finding total population per PUMA:
c.execute("""SELECT pumaold, SUM(TotalPop00) as PopTot
                    FROM geocorr_min_old
                    GROUP BY pumaold""")
data = c.fetchall()
PopTot06perPuma = pd.DataFrame(data, columns=['PUMA', 'PopTotal'])
PopTot06perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS SampTot, AVG(AGEP)
                    FROM geoCA2006
                    GROUP BY pumaold""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
SampTot06 = pd.DataFrame(data, columns=['PUMA', 'SampTot','AGEP'])
SampTot06.head()

# In[46]:

c.execute("""SELECT pumaold, COUNT(SERIALNO) AS SampOA, AVG(AGEP)
                    FROM OA_CA06 
                    GROUP BY pumaold""")
data = c.fetchall()
TotSampOA06 = pd.DataFrame(data, columns=['PUMA', 'SampOA','AGEP'])
TotSampOA06.head()


# In[27]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb55Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 55 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_55_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_55_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb56Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 56 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_56_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_56_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb57Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 57 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_57_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_57_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb58Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 58 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_58_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_58_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb59Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 59 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_59_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_59_perPuma.head()

# In[28]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb60Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 60 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_60_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_60_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb61Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 61 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_61_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_61_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb62Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 62 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_62_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_62_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb63Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 63 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_63_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_63_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb64Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 64 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_64_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_64_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb65Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 65 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_65_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_65_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb66Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 66 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_66_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_66_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb67Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 67 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_67_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_67_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb68Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 68 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_68_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_68_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb69Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 69 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_69_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_69_perPuma.head()


# In[30]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 70
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_70_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_70_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb70Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 71
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_71_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_71_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb72Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 72
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_72_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_72_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb73Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 73
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_73_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_73_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb74Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 74
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_74_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_74_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb75Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 75
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_75_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_75_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb76Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 76
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_76_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_76_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb77Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 77
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_77_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_77_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb78Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 78
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_78_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_78_perPuma.head()


#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb79Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 79
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_79_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_79_perPuma.head()

# In[31]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb80Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 80 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_80_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_80_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb81Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 81 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_81_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_81_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb82Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 82 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_82_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_82_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb83Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 83 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_83_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_83_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb84Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 84 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_84_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_84_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb85Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 85 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_85_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_85_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb86Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 86 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_86_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_86_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb87Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 87 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_87_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_87_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb88Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 88 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_88_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_88_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb89Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 89 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_89_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_89_perPuma.head()

# In[33]:

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb90Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 90 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_90_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_90_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb91Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 91 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_91_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_91_perPuma.head()

#finding total sample population per PUMA:
c.execute("""SELECT pumaold, COUNT(SERIALNO) AS Numb92Samp, AGEP
                    FROM OA_CA06
                    WHERE AGEP = 92 
                    GROUP BY pumaold""")
data = c.fetchall()
SampPopOA06_92_perPuma = pd.DataFrame(data, columns=['PUMA', 'SampPop','AGEP'])
SampPopOA06_92_perPuma.head()


# In[266]:

print sorted(CA2006_min['AGEP'].unique())


# In[267]:

frames06 = [SampPopOA06_55_perPuma,SampPopOA06_56_perPuma,SampPopOA06_57_perPuma,SampPopOA06_58_perPuma,
    SampPopOA06_59_perPuma,SampPopOA06_60_perPuma,SampPopOA06_61_perPuma,SampPopOA06_62_perPuma,
    SampPopOA06_63_perPuma,SampPopOA06_64_perPuma,SampPopOA06_65_perPuma,SampPopOA06_66_perPuma,
    SampPopOA06_67_perPuma,SampPopOA06_68_perPuma,SampPopOA06_69_perPuma,SampPopOA06_70_perPuma,
    SampPopOA06_71_perPuma,SampPopOA06_72_perPuma,SampPopOA06_73_perPuma,SampPopOA06_74_perPuma,
    SampPopOA06_75_perPuma,SampPopOA06_76_perPuma,SampPopOA06_77_perPuma,SampPopOA06_78_perPuma,
    SampPopOA06_79_perPuma,SampPopOA06_80_perPuma,SampPopOA06_81_perPuma,SampPopOA06_82_perPuma,
    SampPopOA06_83_perPuma,SampPopOA06_84_perPuma,SampPopOA06_85_perPuma,SampPopOA06_86_perPuma,
    SampPopOA06_87_perPuma,SampPopOA06_88_perPuma,SampPopOA06_92_perPuma]
CountOA06 = pd.concat(frames06)


# In[271]:

CountOA06[CountOA06['PUMA']==100]

#Merged Samp datasets 2014:
result0 = pd.merge(SampPopOA06_85to90_perPuma,SampPopOA06_90to95_perPuma, 
                   on=['PUMA'])
result1=pd.merge(SampPopOA06_80to85_perPuma,result0,on=['PUMA'])
result2=pd.merge(SampPopOA06_75to80_perPuma,result1,on=['PUMA'])
result3=pd.merge(SampPopOA06_70to75_perPuma,result2,on=['PUMA'])
result4=pd.merge(SampPopOA06_65to70_perPuma,result3,on=['PUMA'])
result5=pd.merge(SampPopOA06_60to65_perPuma,result4,on=['PUMA'])
result6=pd.merge(SampPopOA06_55to60_perPuma,result5,on=['PUMA'])
result7=pd.merge(TotSampOA06,result6,on=['PUMA'])
result8=pd.merge(SampTot06,result7,on=['PUMA'])
CountsPUMA06=pd.merge(PopTot06perPuma,result8,on=['PUMA'])

CountsPUMA06.head()

CountsPUMA06_final = CountsPUMA06.rename(index=None, columns={'PUMA':'PUMA', 'PopTotal':'PopTotal_06', 'SampTot':'SampTot_06', 'SampOA':'SampOA_06', 'SampPop55_60':'SampPop55_60_06', 'SampPop60_65':'SampPop60_65_06', 'SampPop65_70':'SampPop65_70_06', 'SampPop70_75':'SampPop70_75_06', 'SampPop75_80':'SampPop75_80_06', 'SampPop80_85':'SampPop80_85_06', 'SampPop85_90':'SampPop85_90_06', 'SampPop90_95':'SampPop90_95_06'})
# In[ ]:

#Can take tables from different years and subtract based on age count
#to see change in count age over time per zip.
c.execute("""SELECT * 
                FROM OA_CA14""")
data = c.fetchall()
names = [description[0] for description in c.description]
print names
OA_CA14_df = pd.DataFrame(data, columns = ['cntyname','CountySubName','zipcode','puma12','zipname','TotalPop','DIS','DEAR','SERIALNO','SPORDER','PUMA','AGEP','DDRS','DEYE','DOUT','DPHY','DREM','MIG','RETP','SCHL','SEX','WAGP','WKL','DRIVESP','LANP','RAC1P'])
print OA_CA14_df['zipcode'].nunique()
print OA_CA14_df['puma12'].nunique()
OA_CA14_df.head()


