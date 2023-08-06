#!/usr/bin/env python
# coding: utf-8

# ## Main Toolbox
# 
# Edit the following notebook to update the <b>Toolbox</b> module in hcar-py</br>
# * Don't forget to hit <u>save</u> before running</b>
# 
# ### Imports

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime as dt
from threading import Timer
import re
import requests
import sqlparse
import pyodbc
import os
import logging
import random
from ipywidgets import widgets
from IPython.display import HTML,Javascript, display

pd.options.mode.chained_assignment = None
from deshaw.djs import TidyReport


# ### Data Cleaning

# In[2]:


def colsSnakeCase(dfs,chars=[':','(',')','?','.','*','-',','],rm_unnamed = True):
    """
    Converts all column names to lower case, removes multiple spaces between words,
    and replaces spaces with underscores.

    Args:
        dfs (list or pd.DataFrame): Dataframe(s) with non-standardised column naming convention
        chars (list): string characters to be removed from all column names

    Return:
        None
    """
    if type(dfs) is not list:
        dfs = [dfs]
    for df in dfs:
        ## for camel case headers, add a space inbetween words
        df.columns = [re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', x) for x in df.columns]
        
        ## lowercase
        df.columns = [x.lower() for x in df.columns]
        for char in chars:
            df.columns = df.columns.str.replace(char,'', regex = True)
        df.columns = [re.sub(' +', ' ', x) for x in df.columns]
        df.columns = df.columns.str.replace(' ','_', regex = True)
        if [x for x in df.columns if 'unnamed' in x] and rm_unnamed:
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            logging.warning("Unnamed columns were removed. Set rm_unnamed = False to stop this.") 
            # print("Unnamed columns were removed. Set rm_unnamed = False to stop this.")

#----------------- WIDE TO LONG -----------------#        

def getStubNames(key):
    stub_names_dict = {
        'professional_experience':['start_date_professional_experience',
                                   'end_date_professional_experience',
                                   'company_professional_experience',
                                   'company_location_city_professional_experience',
                                   'country_professional_experience',
                                   'position_title_professional_experience',
                                   'position_type_professional_experience',
                                   'is_current_employer_professional_experience'],
        'education_data':[
                                     'education_data_cum_gpa',
                                     'education_data_cum_gpa_max_scale',
                                     'degree_name',
                                     'degree_level_name',
                                     'university_name',
                                     'school_name',
                                     'major_1_name',
                                     'major_2_name',
                                     'education_start_date',
                                     'date_of_grad_education_data'],
        'des_interview_feedback':['des_interview_feedback_schedule_id',
                                   'des_interview_feedback_interview_status',
                                   'des_interview_feedback_interviewer_role',
                                   'des_interview_feedback_interview_type',
                                   'des_interview_feedback_interview_date',
                                   'des_interview_feedback_comments_date',
                                   'des_interview_feedback_bottom_line'],
        'reference':['references_full_name_reference', 
                     'superstar_reference']
        
    }
    if key in stub_names_dict.keys():
        return stub_names_dict[key]
    else:
        raise Exception(f"{key} is not a preset wide-to-long grouping. Please add in stub_names in list format to the function.")
def getWideToLongDict(key):
    dicts = {'educ':{'degree_name': 'degree_name_1', 
                    'degree_level_name': 'degree_level_name_1', 
                    'university_name': 'university_name_1',
                    'school_name': 'school_name_1',
                    'major_1_name': 'major_1_name_1', 
                    'major_2_name': 'major_2_name_1',
                    'degree_name1': 'degree_name_2', 
                    'degree_level_name1': 'degree_level_name_2', 
                    'university_name1': 'university_name_2',
                    'school_name1': 'school_name_2', 
                    'major_1_name1': 'major_1_name_2', 
                    'major_2_name1': 'major_2_name_2',
                    'degree_name2': 'degree_name_3', 
                    'degree_level_name2': 'degree_level_name_3',
                    'university_name2': 'university_name_3', 
                    'school_name2': 'school_name_3', 
                    'major_1_name2': 'major_1_name_3', 
                    'major_2_name2': 'major_2_name_3',
                    'degree_name3': 'degree_name_4',
                    'degree_level_name3': 'degree_level_name_4', 
                    'university_name3': 'university_name_4', 
                    'school_name3': 'school_name_4',
                    'major_1_name3': 'major_1_name_4', 
                    'major_2_name3': 'major_2_name_4', 
                    'degree_name4': 'degree_name_5',
                    'degree_level_name4': 'degree_level_name_5', 
                    'university_name4': 'university_name_5', 
                    'school_name4': 'school_name_5',
                    'major_1_name4': 'major_1_name_5', 
                    'major_2_name4': 'major_2_name_5', 
                    'degree_name5': 'degree_name_6',
                    'degree_level_name5': 'degree_level_name_6', 
                    'university_name5': 'university_name_6', 
                    'school_name5': 'school_name_6',
                    'major_1_name5': 'major_1_name_6', 
                    'major_2_name5': 'major_2_name_6', 
                     'education_data_1_date_of_grad_':'date_of_grad_education_data_1',
                     'education_data_2_date_of_grad_':'date_of_grad_education_data_2',
                     'education_data_3_date_of_grad_':'date_of_grad_education_data_3',
                     'education_data_4_date_of_grad_':'date_of_grad_education_data_4',
                     'education_data_5_date_of_grad_':'date_of_grad_education_data_5',
                     'education_data_6_date_of_grad_':'date_of_grad_education_data_6',
                     'education_data_1_cum_gpa_':'education_data_cum_gpa_1',
                     'education_data_2_cum_gpa_':'education_data_cum_gpa_2',
                     'education_data_3_cum_gpa_':'education_data_cum_gpa_3',
                     'education_data_4_cum_gpa_':'education_data_cum_gpa_4',
                     'education_data_5_cum_gpa_':'education_data_cum_gpa_5',
                     'education_data_6_cum_gpa_':'education_data_cum_gpa_6',
                     'education_data_1_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_1',
                     'education_data_2_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_2',
                     'education_data_3_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_3',
                     'education_data_4_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_4',
                     'education_data_5_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_5',
                     'education_data_6_cum_gpa_max_scale_':'education_data_cum_gpa_max_scale_6',
                     
                     'education_data_1_start_date_':'education_start_date_1',
                     'education_data_2_start_date_':'education_start_date_2',
                     'education_data_3_start_date_':'education_start_date_3',
                     'education_data_4_start_date_':'education_start_date_4',
                     'education_data_5_start_date_':'education_start_date_5',
                     'education_data_6_start_date_':'education_start_date_6',
                },
            'scores':{'position_internal_position_name':'score_pos_name_1',
                      'position_internal_position_name1':'score_pos_name_2',
                      'position_internal_position_name2':'score_pos_name_3',
                     'position_internal_position_name3':'score_pos_name_4',
                      'scores_1_score_date':'score_date_1',
                     'scores_2_score_date':'score_date_2',
                     'scores_3_score_date':'score_date_3',
                     'scores_4_score_date':'score_date_4',
                     'scores_1_score':'score_1',
                     'scores_2_score':'score_2',
                     'scores_3_score':'score_3',
                     'scores_4_score':'score_4'}}
    return dicts[key]
def wideToLongDF(df,
                 icims_group_str,
                 stub_names = None,
                 id_cols = ['primary_record_system_id'],
                 dedupe_col = 'application_date_final',
                 dedupe_last = False,
                 is_educ = False,
                 is_scores = False,
                 drop_dupes = True,
                 rerun = False):
    """
    Converts iCIMS data from wide-to-long
    
    Args:
        df (pd.DataFrame):          Wide DF from iCIMS
        icims_group_str (str):      String that iCIMS uses to denote the series of wide data e.g. education_data
        stub_names (list):          Column names of wide data, without the number
        id_col (list):              ID column for when converting rows to long data
        dedupe_col (str or list):   Column to sort DF on before deduplicating 
        dedupe_last (bool or list): True if want to remove the last ordered value (e.g. latest date) else False
    """
    if is_educ:
        col_dict = getWideToLongDict('educ')
        
        df.rename(columns=col_dict, inplace=True,errors = 'ignore')
    elif is_scores:
        col_dict = getWideToLongDict('scores')
        df.rename(columns=col_dict, inplace=True,errors = 'ignore')
        stub_names = ['score_pos_name',
                        'score_date',
                        'score']
        rerun=True
        
    else:
        pattern = fr'({icims_group_str}_\d_)(.*)'

        ## End every column name with _
        df.columns = [x.rstrip("_")+"_" for x in df.columns]

        ## move the numbered string to the end of the column name
        df.columns = [re.search(pattern,x).group(2)+re.search(pattern,x).group(1) if re.search(pattern,x) else x for x in df.columns]

        ## remove _ from end of all column names
        df.columns = [x.strip('_') for x in df.columns]
        
    if not stub_names:
        stub_names = getStubNames(icims_group_str)

    if drop_dupes:
        ## Keep only latest application info for each candidate
        df = df.sort_values(dedupe_col, ascending=dedupe_last)
        df = df.drop_duplicates(id_cols)

    ## Dropping candidates without primary ID
    df = df.dropna(subset=id_cols,how='all')
    
    ## Wide to Long format
    long_df = pd.wide_to_long(df,
                               stubnames=stub_names,
                               i = id_cols,
                               j = "No.",
                               sep = '_')
    ## Formatting
    long_df.reset_index(inplace=True)
    long_df.drop(['No.'],inplace=True,axis=1)
    long_df.reset_index(drop=True,inplace=True)
    
    return long_df     
#----------------- END WIDE TO LONG -----------------#   

#----------------- DATA TYPE FORMATTING -----------------# 

def colsToDatetime(df, cols, dt_format = '%m/%d/%Y',time = False):
    for col in cols:
        df[col] = pd.to_datetime(df[col],
                                 format = dt_format,
                                 errors = "coerce")
        if not time:
            df[col] = df[col].apply(lambda x: x.date())
    return df


def dateToAY(date):
    year = date.year
    mth = date.month
    if 1<= mth <= 5:
        return year
    elif 6<= mth <=12:
        return year+1
    else:
        raise Exception(f"AY {mth}, {year} not found")
#----------------- END DATA TYPE FORMATTING -----------------# 

def deduplicateByFurthestStage(df,
                               dedupe_cols,
                               stage_col = 'furthest_stage_numeric'):
    """
    Args:
        stage_col (str): Column name of the column containing the furthest 
                         stage by numerical values. If just stage name, then
                         must equal 'furthest_stage'
    
    """
    if (stage_col == 'furthest_stage'):
        df = addStageNumericCol(df)
        stage_col = 'furthest_stage_numeric'
    df = df.sort_values(dedupe_cols +['furthest_stage_numeric'])
    df = df.drop_duplicates(dedupe_cols,keep='last')
    return df


def getYTD(date,ytd = None):
    if ytd==None:
        ytd = dt.today().date()
    if pd.isnull(date):
        return 0
    month = date.month
    day = date.day
    if month<ytd.month:
        return 1
    elif month ==ytd.month:
        if day <ytd.day:
            return 1
    else:
        return 0


# ### Output Formatting

# In[3]:


def prettifyColumns(dfs):
    """
    Converts columns from snake case to title case
    """
    if type(dfs) is not list:
        dfs = list(dfs)
    for df in dfs:
        df.columns = [x.replace('_'," ").title() if not x.isupper() else x for x in df.columns ]
    return df

def overwriteFile(filename,
                  count,
                  file_ext = 'xlsx'):
    """
    Prompts the user to confirm whether file should be overwritten.
    Args:
        filename (str): Name of file that user is updating
        count (int):    Recursion stopper
        file_ext (str): File extension
    
    Return:
        filename (str): Updated filename
    """
    if os.path.exists(filename):
        prompt = 'This file already exists. Do you want to overwrite? (y/n)' 
        overwrite = input(prompt)
        if overwrite.lower()=="n":
            filename = filename.replace(f'.{file_ext}',f' - Copy.{file_ext}')
        elif overwrite.lower() == 'y':
            pass
        else:
            ## include count to not result in infinite recursion
            if count != 0:
                print("Incorrect command. Please Try Again")
                overwriteFile(filename,count-1)
            else:
                print("Too many errors! Filename unchanged")
    return filename

def exportToExcel(dfs, 
                  output_filepath,
                  sheetname_lst,
                  incl_date = True,
                  overwrite_alert = False,
                  prettify_cols = True,
                  adjust_cols = False):
    """
    Exports Dataframe(s) into one workbook, with multiple sheets where necessary.
    Args:
        dfs (list or pd.Dataframe):  List of Dataframes to export             
        output_filepath (str):       Full filepath of the intended destination, including file name (.xlsx extension)
        sheetname_lst (list or str): List of sheet names - must be in same order as dfs
        incl_date (bool):            True if today's date should be appended to the filename, before the extension
        overwrite_alert (bool):      True if user want's a warning before an existing file is overwritten

    Return:
        None
    """
    ## DFs need to be in list format
    if dfs is not list:
        dfs = list(dfs)
    if sheetname_lst is not list:
        sheetname_lst = list(sheetname_lst)
    
    ## Check filename extension
    if not output_filepath.endswith('.xlsx'):
        output_filepath = output_filepath + '.xlsx'
        print("Added .xlsx file extension.")
    
    ## Add date to name
    if incl_date:
        date_str = dt.today().strftime("%Y-%m-%d")
        output_filepath = output_filepath.replace(".xlsx",f" {date_str}.xlsx")
        filename = output_filepath.split("/")[-1]
    else:
        filename = output_filepath.split("/")[-1]
    
    if overwrite_alert:
        filename = overwriteFile(filename, 3)
    
    print(f"Saving file as {filename}")
        
    with pd.ExcelWriter(output_filepath,date_format='mm/dd/yyyy') as writer:
        for n, df in enumerate(dfs):
            sheetname = sheetname_lst[n]
            output = df.fillna('-')
            
            if prettify_cols:
                output = prettifyColumns([output])
                
            output.to_excel(writer,sheetname,index=False)
            worksheet = writer.sheets[sheetname]

            # Get the dimensions of the dataframe.
            (max_row, max_col) = df.shape

            # Make the columns wider for clarity.
            
            
            if adjust_cols:
                worksheet = writer.sheets[sheetname]  # pull worksheet object
                for idx, col in enumerate(df):  # loop through all columns
                    series = df[col]
                    max_len = max((
                        series.astype(str).map(len).max(),  # len of largest item
                        len(str(series.name))  # len of column name/header
                        )) + 1  # adding a little extra space
                    worksheet.set_column(idx, idx, max_len)  # set column width
            else:
                worksheet.set_column(0,  max_col - 1, 14)
                
            # Set the autofilter.
            worksheet.autofilter(0, 0, max_row, max_col - 1)
    print("Done!")
    
    
def checkDir(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
        print(f"Folder at {path} has been created")
        
def checkRuntime(start,end):
    runtime = round(end-start,2)
    val = "seconds"
    if runtime > 60:
        runtime = runtime/60
        val = "mins"
    print(f"Execution time: {runtime} {val}")


# ### Mappings

# In[4]:


def getJobType(job):
    
    """
    Takes name of a job and returns whether it is a fellowship, intern, 
    or perm position. 
    
    Note: This is a best guess based on words in the internal position name.
    """
    
    # Convert the name of the job to all lowercase letters
    job = job.lower()
    
    # If the name of the job is a None value (a nothing-nothing string),
    if job is None:
        # return a None value
        return None
    
    # If the job name is "TLC - Internal Only", a test job, or a temp job, exclude
    elif job == "tlc - internal only" or 'zzz' in job or 'yyy' in job or 'temp' in job or 'z_test' in job or '(Internal)' in job:
        return "Exclude"
    
    # If the word 'intern' is in the job name, and the word 'internal' 
    #  is not in the job name,
    elif "intern" in job and "internal" not in job and "intern recruit" not in job:
        # return that the job is an 'Intern' position
        return "Intern"
    
    # If the word 'fellowship' appears in the job name,
    elif "fellowship" in job:
        # it is a 'Fellowship' position
        return "Fellowship"
    
    # Otherwise, we presume the job name is referring to a permanent position
    else:
        return "Permanent"
    
#------------------------ STAGE MAP ------------------------#
def getStageMap(as_dict = False,
                clean_cols = True):
    map_df = pd.read_excel('/proj/hr/HCAR/Recurring Reports/Map Repository/Stage Map.xlsx')
    if as_dict:
        map_df.set_index('Furthest Stage',inplace=True)
        return map_df.to_dict('dict')['Furthest Stage Numeric']
    else:
        if clean_cols:
            colsSnakeCase(map_df)
        return map_df
stage_map = getStageMap(as_dict = True)

def addStageNumericCol(df,col = 'furthest_stage'):
    df[col].fillna('Screening', inplace=True)
    df[col] = df[col].apply(lambda x: 'Screening' if x=='-' else x)
    stage_map = getStageMap(as_dict=True)
    df['furthest_stage_numeric'] = df[col].apply(lambda x: stage_map[x] if x in stage_map.keys() else (1 if pd.isnull(x) else np.nan))
    return df

def getStageNumeric(stage):
    """
    row-level mapping
    """
    if stage in stage_map.keys():
        return stage_map[stage]
    return np.nan

def addHighestDegreeNumericCol(x):
    deg_map = {
        'Bachelors':0,
        'Undergraduate':0,
        'Masters':1,
        'Law':1,
        'PhD':2
    }
    if x in deg_map.keys():
        return deg_map[x]
    else:
        return np.nan

#------------------------ END STAGE MAP ------------------------#

#----------------- JOB REPORTING GROUP [SEGMENTS] -----------------#
def convertSegments(df, 
               seg_col = 'job_reporting_grouping',
               seg_map = None,
               new_col = None):
    if not new_col:
        new_col = seg_col
    key_segments = ['FO Tech',
                    'FONT',
                    'SBD',
                    'Exclude',
                    'Other Tech',
                    'Support Unit']
    if not seg_map:
        seg_map = {
            'Front-Office Technical':'FO Tech', 
            'Front-Office Non-Technical':'FONT', 
            'Support' : 'Support Unit',
            '-':'-',
            'Middle-Office': 'SBD', 
            'Exclude' : 'Exclude', 
            'Other Technical': 'Other Tech',
            'Admin, EA, and Facilities': 'Support Unit'
        }

    df[new_col] = df[seg_col].apply(lambda x: seg_map[x] if x in seg_map.keys() else x)

    unique_segments = df[new_col].unique().tolist()
    outliers = [x for x in unique_segments if x not in key_segments]
    if any(outliers):
        print(f"Found the following segments that are not recognised. Please check: {outliers}")
    return df
#----------------- END JOB REPORTING GROUP [SEGMENTS] -----------------#


# ### DWH

# In[5]:


def getDWHData(report,
               alterations = {},
               print_query = False,
               query_date = None,
               date_cols = ['Assignment Details Shown as Of'],
               clean_cols = True,
               updated_path = None,
               local_file = False
               ):
    #### DWH REPORT IN PYTHON ####    
    """
    Loads the employee roster (including temps) from DWH on a given date/dates
 
    Args:
        report (str):       File name of SQL query in git
        alterations (dict): Changes to be made in the SQL query, where k is original, and v is altered version
        print_query (bool): If TRUE, prints the SQL query
        clean_cols (bool):  If TRUE, changes column names of output to snake-case
        
    Returns:
        df (pd.dataframe): Data from DWH
    """
    ## Format Query Date
    if not query_date:
        query_date = dt.today()
    query_date = query_date.strftime('%Y%m%d')
    
    # pull report from gitHub repo
    if not local_file:
        if not os.path.isdir(".git"):
            os.system('git init')
            os.system(f'git remote add origin https://github.deshaw.com/hcar/DWH_Workday_Queries.git')
        os.system('git fetch')
        os.system(f'git checkout -m origin/main "{report}"')
        os.system(f'git add "{report}"')
        os.system(f'git commit -m "pulled roster"')
    
    
    # read query from report file
    if updated_path:
        report = updated_path + "/" + report
        
    with open(report) as f:
        lines = f.readlines()
        raw_query = ''.join(lines)
 
    ## format query
    query = sqlparse.format(raw_query, strip_comments=True).replace('use hcanalytics\ngo\n\n', '').replace("format(f.source_start_date,n'yyyymmdd')", 
                                                                                                           "format(f.source_start_date,N'yyyyMMdd')")

        
    ## Alter query
    for k,v in alterations.items():
        query = query.replace(k,v)
        
    ## Alter date
    if 'Declare @EffectiveDate datetime' not in query:
        query.replace('use hcanalytics',"""
                                        use hcanalytics\n
                                        go\n
                                        Declare @EffectiveDate datetime\n
                                        Set @EffectiveDate = GETDATE()\n
                                        """)
    query = query.replace("Set @EffectiveDate = GETDATE()",f"Set @EffectiveDate = \'{query_date}\'")

    ## print query
    if print_query:
        print(query)
        
    ## Get dataframe
    df = queryDWH(query,date_cols)
    
    print(f"{report} generated.")
    
    if clean_cols:
        ## convert columns to snake-case
        colsSnakeCase(df)
        
    idx_cols = [x for x in df.columns.tolist() if '_id' in x]
    for col in idx_cols:
        try:
            df[col] = df[col].astype(int)
        except:
            continue
    ## replace NA with np.nan
    df = df.replace("NA",np.nan)
    return df

def queryDWH(query,
             date_cols):
    """
    Queries the DWH based on some SQL input
    
    Args:
        query (str):       SQL text to query from DWH
        date_cols (list):  
        clean_cols (bool): If TRUE, changes column names of output to snake-case
    
    Returns:
        df (pd.dataframe): data from DWH
    """

    # connect to database
    connection_str = 'DRIVER={ODBC Driver 17 for SQL Server};Server=DBCLPROD1DS5;Database=hcanalytics;Trusted_connection=yes;'
    conn = pyodbc.connect(connection_str,charset='utf8')
    conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin-1')
    conn.setdecoding(pyodbc.SQL_WCHAR, encoding='latin-1')
    conn.setencoding(encoding='latin-1')

    # execute query and load as pandas df
    if date_cols:
        df = pd.read_sql(query, conn,parse_dates=date_cols)
    else:
        df = pd.read_sql(query,conn) 
        
    return df

def getQuery(report,query_date = dt.today()):
    ## Format Query Date
    query_date = query_date.strftime('%Y%m%d')
    # pull report from gitHub repo
    if not os.path.isdir(".git"):
        os.system('git init')
        os.system('git remote add origin https://github.deshaw.com/hcar/DWH_Workday_Queries.git')
    os.system('git fetch')
    os.system(f'git checkout -m origin/main "{report}"')
    os.system(f'git add "{report}"')
    os.system(f'git commit -m "pulled roster"')
     
    # read query from report file
    report_fp = os.path.join(path, report)
    with open(report_fp) as f:
        lines = f.readlines()
        raw_query = ''.join(lines)
 
    ## format query
    query = query.replace("Set @EffectiveDate = GETDATE()",f"Set @EffectiveDate = \'{query_date}\'")
    return query


# In[6]:


## Dummy Data Builder
def buildDummyDF(rows,columns,date_col = None):
    randomized_data = []
    header = [f'col{i}' for i in range(1,columns+1)]
    if date_col:
        date_range = pd.date_range(dt.today().date() - datetime.timedelta(rows-1),dt.today().date())
        randomized_data.append(date_range) 
        header.insert(0,'Date')
    for x in range(columns):
        randomized_data.append(random.sample(range(10, 100), rows))
    df = pd.DataFrame(randomized_data).T
    df.columns = header
    return df


# ### Recruitment Metrics

# In[7]:


def getConversionRate(df,id_col = 'funnel'):
    def calcOfferRate(df,outcome):
        declined = df.loc[df.furthest_stage=='Offer Declined',id_col].iloc[0]
        accepted = df.loc[df.furthest_stage=='Offer Accepted',id_col].iloc[0]
        if outcome == 'declined':
            return declined/(declined+accepted)
        if outcome == 'accepted':
            return accepted/(declined+accepted)
        else:
            raise Exception("Wrong command. Try 'declined' or 'accepted'")
        
    if 'furthest_stage_numeric' not in df.columns:
        addStageNumericCol(df)
    df = df.sort_values('furthest_stage_numeric')
    df = df.drop('furthest_stage_numeric',axis=1)
    df['conversion_rate'] = df[id_col].pct_change()
    

    ## format
    df['conversion_rate'] = df['conversion_rate'].apply(lambda x: (1+x)) ## decimal
    
    ## change for offer declined and accepted
    df.loc[df.furthest_stage=='Offer Declined','conversion_rate'] = calcOfferRate(df,'declined')
    df.loc[df.furthest_stage=='Offer Accepted','conversion_rate'] = calcOfferRate(df,'accepted')
    
    df.set_index('furthest_stage',inplace=True)
    
    # df.fillna("-",inplace=True) ## denotes no conversion rate
    # df.reset_index(drop = True,inplace=True)
    return df


def getRecruitmentFunnel(df,id_col = 'primary_record_system_id',cr = True):
    if 'furthest_stage_numeric' not in df.columns:
        addStageNumericCol(df)
        
    try: ## hacky way to work around an error until I can figure out what is wrong
        df = df.groupby(['furthest_stage','furthest_stage_numeric'],as_index=False)[id_col].count()
    except:
        df = df.groupby(['furthest_stage','furthest_stage_numeric'])[id_col].count().reset_index()
    
    ## Test to see if any row missing ##
    missing = [x for x in range(1,10) if x not in df.furthest_stage_numeric.unique()] 
    if any(missing):
        ## if there's any missing rows, add in a zero row 
        stage_map = getStageMap().drop_duplicates('furthest_stage_numeric')
        for stage in missing:
            stage_str = stage_map[stage_map.furthest_stage_numeric == stage].furthest_stage.iloc[0]
            df = df.append({'furthest_stage':stage_str,
                            'furthest_stage_numeric':stage,
                             id_col:0},
                          ignore_index = True)
    
    df.reset_index(drop=True,inplace=True)
        
    df = df.sort_values('furthest_stage_numeric',ascending=False)
    df['funnel'] = df[id_col].cumsum()
    df.loc[df.furthest_stage_numeric == 8,'funnel'] = df.loc[df.furthest_stage_numeric == 8,id_col]
    df = df.sort_values('furthest_stage_numeric')
    df = df.drop([id_col,'furthest_stage_numeric'],axis=1)
    # df.reset_index(drop = True,inplace=True)
    if cr:
        df = getConversionRate(df)
    return df

def compileTransposedFunnel(
    df,
    id_col,
    job_name_col,
    stage_col,
):
    """
    This function outputs two tables - one for funnel abs count, and one for
    conversion rates.
    """
    jobs_lst = sorted(df[job_name_col].unique().tolist())
    rec_dfs = []
    cr_dfs = []
    for job in jobs_lst:
        temp = df[df[job_name_col]==job]
        funnel = getRecruitmentFunnel(temp,id_col)
        rec_dfs.append(funnel[['funnel']].rename({'funnel':job},axis=1).T)
        cr_dfs.append(funnel[['conversion_rate']].rename({'conversion_rate':job},axis=1).T)

    rec_df = pd.concat(rec_dfs)
    cr_df = pd.concat(cr_dfs)

    # output.loc['Total', :] = output.sum().values ## not until they fix the problem
    return rec_df,cr_df


# ### Calculations

# In[8]:


# def addQuantileCol(
#     df,
#     id_col,
#     segment_col = "job_family_group",
#     segment=True,
#     percentile = True):
#     def _find_quantile(n,mapping):
#         if n in mapping.keys():
#             return mapping[n]
#         else:
#             for k,v in mapping.items():
#                 if n>k:
#                     return mapping[k]
#     quantile_map = df[id_col].quantile([x/20 for x in range(21)]).to_dict()
#     quantile_map = {v: k for k, v in sorted(quantile_map.items(),reverse=True)} ## reversing 
#     if segment:
#         for seg in df[segment_col].unique().tolist():
#             segment_map = df.loc[df[segment_col]==seg,id_col].quantile([x/20 for x in range(21)]).to_dict()
#             segment_map = {v: k for k, v in sorted(segment_map.items(),reverse=False)} ## reversing 
#             df.loc[df[segment_col]==seg,'percentile_in_group'] = df.loc[df[segment_col]==seg,id_col].apply(lambda x:_find_quantile(x,segment_map))
#         df['percentile_firmwide'] = df[id_col].apply(lambda x:_find_quantile(x,quantile_map))
#         # if percentile:
#         #     df['percentile_in_group'] = df['percentile_in_group'].map('{:.0%}'.format)
#         #     df['percentile_firmwide'] = df['percentile_firmwide'].map('{:.0%}'.format)
#     else:
#         df['percentile'] = df[id_col].apply(lambda x:_find_quantile(x,quantile_map))
# #         if percentile:
# #             df['percentile_in_group'] = df['percentile_in_group'].map('{:.0%}'.format)
# #             df['percentile_firmwide'] = df['percentile_firmwide'].map('{:.0%}'.format)
    
#     return df

def addQuantileCol(
    df,
    id_col
):
    """
    New and improved!
    """
    def _find_quantile(n,mapping):
        if n in mapping.keys():
            return mapping[n]
        else:
            for k,v in mapping.items():
                if n>k:
                    return mapping[k]
    quantile_map = df[id_col].quantile([x/20 for x in range(21)]).to_dict()
    quantile_map = {v: k for k, v in sorted(quantile_map.items(),reverse=True)} ## reversing 
    df['percentile'] = df[id_col].apply(lambda x:_find_quantile(x,quantile_map))
    # df['percentile'] = df['percentile']*100 ## use this for full %
    return df.sort_values(id_col,ascending=False)


# ## Errors

# In[9]:


def Notify(
        user,
        warning,
        filepath,
        message = None,
        title = "[djserror] DJS Python Error Report"):
    report = TidyReport([f"{warning} error at {filepath}",
                          f"{message}"])
    report.mail(
            to = user,
            subject = title,
            attach_html_report = False
        )
    
def popup(text):
    """
    Creates a Jupyter Notebook popup
    """
    display(HTML("<script>alert('{}');</script>".format(text)))
    
    
def checkFolderExists(path):
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(path)
        print("New file created!")
    else:
        print("Folder already exists")


# ### Exporting

# In[10]:


