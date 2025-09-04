data_col_method ={
  'data_collection_tool':'OpenClinica','data_collection_tool_other':'randomization','Yes':'','use_tablets':'No'
}
years_list = [str(year) for year in range(2000, 2031)]

studies_dict = [{
   'study_id':'TB001',
   'protocol_num':'TB001',
   'protocol_desc':'TB Reference Materials (TBRM) - Collection, Storage & Distribution',
   'project_num':'1111',
   'ctgov_num':'2222',
   'research_type':'Specimen collection',
   'study_design':'N/A',
  'study_sites':[],
  'data_col_method':data_col_method,
  'team_members':[],
  'study_timeline':{},
  'other_details':{}


},{
  'study_id':'TB002',
  'protocol_num':'TB002',
  'protocol_desc':'TB Reference Materials (TBRM) - Collection, Storage & Distribution',
  'project_num':'1111',
  'ctgov_num':'2222',
  'research_type':'Specimen collection',
  'study_design':'N/A',
  'study_sites':[],
  'data_col_method':data_col_method,
  'team_members':[],
  'study_timeline':{},
  'other_details':{}

},{
  'study_id':'TB003',
  'protocol_num':'TB003',
  'protocol_desc':'TB Reference Materials (TBRM) - Collection, Storage & Distribution',
  'project_num':'4444',
  'ctgov_num':'22255',
  'research_type':'Specimen collection',
  'study_design':'N/A',
  'study_sites':[],
  'data_col_method':data_col_method,
  'team_members':[],
  'study_timeline':{},
  'other_details':{}

},{
  'study_id':'TB004',
  'protocol_num':'TB004',
  'protocol_desc':'TB Reference Materials (TBRM) - Collection, Storage & Distribution',
  'project_num':'1111',
  'ctgov_num':'2222',
  'research_type':'Specimen collection',
  'study_design':'N/A',
  'study_sites':[],
  'data_col_method':data_col_method,
  'team_members':[],
  'study_timeline':{},
  'other_details':{}

}]

site_dict = [{'site_id':'KEMRI','site_name':'KEMRI CDC','site_country_id':'KE','site_city':'Kisumu','site_sample_size':'100','site_pi_name':'John Doe','site_pi_gender':'M','pi_location':'KE'}]

options_dict ={
  'health_program':['AMR','COVID-19','Digital Health','Fever','HCV','Malaria','NCD','NTD','Pandemic Threats','TB','WH','Tech and Dev'],
  'research_type':['Clinical Performance Study','Feasibility Study','Flex and Human factor study','Implementation Research','Operation Research','Specimen Collection'],
  'study_design':['Interventional','Observational','N/A'],
  'data_col_tool':['OpenClinica','RedCAP','Other'],
  'yes_no': ['Yes','No'],
  'team_member_role':['CRA','Data Manager','Project Manager','Statistician','Trial Manager','Other'],
  'years_list':years_list,
  'find_role':['Sponsor','Co-Sponsor','Funding','Other'],
  'study_population':['Adults','Children','Mixed','Other' ],
  'inv_prod':['Early Prototype','Optimized Prototype (All its iterations)','Design Lock','Post Approval','Other'],
  'oir_team':['Yes','No']
}

