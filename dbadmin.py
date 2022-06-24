#data.db administration Frode
import streamlit as st
import pandas as pd
import sqlite3
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder, JsCode

conn = sqlite3.connect('./data.db', check_same_thread=False)
c=conn.cursor()

st.set_page_config(page_title="FPV DB Admin", layout="wide")


def get_data(tablename):
    df=pd.read_sql_query("SELECT * FROM {}".format(tablename), conn)
    return df

option = st.sidebar.radio("What to show",('Projects', 'Resources', 'Actions','Companies','Customer Contact','Customers','Disciplines','Functions','Locations','Managers','Resources Hours','Rigs'))

if option=='Projects':
    tablename = 'tbl_Projects'
    data = get_data(tablename)
    rigname = get_data('tbl_Rigs') 
    
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_column('KO_Date', header_name=("KO_Date"), editable= True)
    gb.configure_column('Tracker_No', header_name=("Tracker_No"), editable= True)
    gb.configure_column('KO_Promised_Date', header_name=("KO_Promised_Date"), editable= True)
    gb.configure_columns(['Sales_Prospect_No','Comments','Q_Amount','PO_Amount','Closed'], hide=True)
    gb.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=20)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
    
    with st.form("New Project", clear_on_submit=True):
        Tracker_no=st.text_input("Tracker No")
        Rigname=st.selectbox("Rigname",rigname.iloc[:,1])
        SO_Description=st.text_input("Description")
        Received_date=st.date_input("Received Date")
        button_check = st.form_submit_button("Add to list")
        if button_check:
            data_to_df={'Tracker_No':Tracker_no,'Rigname':Rigname,'SO_Description':SO_Description,'Received_Date':Received_date}
            data=data.append(data_to_df, ignore_index = True)
            data.to_sql(tablename, conn, if_exists='replace', index=False)
            st.legacy_caching.clear_cache()
            st.experimental_rerun()
elif option == 'Resources':

    tablename = 'tbl_Resources'
    data = get_data(tablename)
    
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_column('Terminated', header_name=("Terminated"), editable= True, filter=("TRUE"))
    gb.configure_column('Producer', header_name=("Producer"), editable= True)
    gb.configure_column('Last_Name', header_name=("Last_Name"), editable= True)
    gb.configure_column('First_Name', header_name=("First_Name"), editable= True)
    gb.configure_columns(['Resource_Email', 'Discipline_ID', 'Manager_ID', 'Location_ID'], hide=True)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Actions':
    tablename = 'tbl_Actions'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Companies':
    tablename = 'tbl_Companies'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Customer Contact':
    tablename = 'tbl_Customer_Contacts'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Customers':
    tablename = 'tbl_Customers'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Disciplines':
    tablename = 'tbl_Disciplines'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Functions':
    tablename = 'tbl_Functions'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Locations':
    tablename = 'tbl_Locations'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
elif option=='Resources Hours':
    tablename = 'tbl_Resources_Hours'
    data = get_data(tablename)
    names = pd.read_sql_query("SELECT Resource_ID, Last_Name, First_Name FROM tbl_Resources WHERE Producer = 'TRUE'", conn)
    names["Full_name"]=names["Last_Name"]+' '+names["First_Name"]

    projectlist=pd.read_sql_query("SELECT * FROM tbl_Projects", conn)
    projectlist['full_project']=projectlist['Tracker_No']+' --- '+projectlist['Rigname']+' --- '+projectlist['SO_Description']
    project=st.selectbox("Projects ready for kickoff",projectlist.iloc[:,25])
    discipline=pd.read_sql_query("SELECT * FROM tbl_disciplines",conn)
    #gb = GridOptionsBuilder.from_dataframe(data)
    #gridOptions = gb.build()
    #dta = AgGrid(data,
    #gridOptions=gridOptions,
    #width='100%',
    #reload_data=False,
    #height=800,
    #editable=True,
    #theme='streamlit',
    #data_return_mode=DataReturnMode.AS_INPUT,
    #update_mode=GridUpdateMode.MODEL_CHANGED)

    with st.form("New Project", clear_on_submit=True):
        #Tracker_no=st.text_input("Tracker No")
        Discipline=st.selectbox("Dicsipline", discipline.iloc[:,1])
        Resource_Name=st.selectbox("Name",names.iloc[:,3])
        Planned_Hours=st.text_input("Planned Hours")

        button_check = st.form_submit_button("Add to list")


            #if button_check:
            #data_to_df={'Tracker_No':Tracker_no,'Rigname':Rigname,'SO_Description':SO_Description,'Received_Date':Received_date}
            #data=data.append(data_to_df, ignore_index = True)
            #data.to_sql(tablename, conn, if_exists='replace', index=False)
            #st.legacy_caching.clear_cache()
            #st.experimental_rerun()

        if button_check:
            selected_tracker_no=(project.split(' ',1)[0])
            discipline_id=int(discipline[discipline['Discipline'].str.contains(Discipline)].iloc[:,0])
            resource_id=int(names[names["Full_name"]==Resource_Name].iloc[:,0])
            planned_hours = int(Planned_Hours)
            sql = '''INSERT INTO tbl_Resources_hours(Tracker_No,Disiplin_ID,Resource_ID,Resource_Function_ID,Planned_Hours,Actual_Hours,Progress_Percentage)
                 VALUES (?,?,?,?,?,?,?);'''
            data_tuple=(selected_tracker_no,discipline_id,resource_id,'',planned_hours,'','')
            c.execute(sql,data_tuple)
            conn.commit()



elif option=='Managers':
    tablename = 'tbl_Managers'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)
else:
    option=='Rigs'
    tablename = 'tbl_Rigs'
    data = get_data(tablename)

    gb = GridOptionsBuilder.from_dataframe(data)
    gridOptions = gb.build()
    dta = AgGrid(data,
    gridOptions=gridOptions,
    width='100%',
    reload_data=False,
    height=800,
    editable=True,
    theme='streamlit',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED)



if st.button("Save changes to database"):
    data=dta['data']
    data.to_sql(tablename, conn, if_exists='replace', index=False)
    st.legacy_caching.clear_cache()
    st.experimental_rerun()
    
