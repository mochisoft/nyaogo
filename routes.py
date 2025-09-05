from flask import request, render_template,jsonify
# app = Flask(__name__)
from data_model import studies_dict, options_dict, site_dict
from models import Study, StudySite, TeamMember, DataColMethod, StudyTimeline, OtherDetails
from datetime import datetime


def register_routes(app, db):
  
  
  @app.route('/')
  def hello_world():
    
    studies=Study.query.all()
  
    #return render_template('home.html', studies=studies_dict)
    return render_template('home.html', studies=studies)

  
  
  @app.route('/study/study', methods=['GET'])
  def add_new_study():
  
    return render_template('new_study.html', options_dict=options_dict)
    
  @app.route('/study/<string:study_code>/download', methods=['GET'])
  def download_study_data(study_code):
    study = Study.query.filter_by(study_code=study_code).first()


    return jsonify({
        "study_data": study.to_dict()
    })

  
  @app.route('/study/add', methods=['POST'])
  def view_new_study():
    study_data = request.form.to_dict()
   
    
    #study_data['study_sites'] = []
    #study_data['data_col_method'] = {}
    #study_data['team_members'] = []
    #study_data['study_timeline'] = {}
    #study_data['other_details'] = {}

    study = Study( study_code=study_data['study_code'], health_program=study_data['health_program'], 
                  protocol_num=study_data['protocol_num'],protocol_desc=study_data['protocol_desc'],  
                  project_num=study_data['project_num'], ctgov_num=study_data['ctgov_num'], 
                  research_type=study_data['research_type'],study_design=study_data['study_design'])
    
    db.session.add(study)
    db.session.commit()
    # print(study)
    # Create a new study object and save it to the database but then redirect to the view page with study_data dict with initialized empty lists and dicts.
  
    return render_template('view_study.html', study=study.to_dict(), view='new', options_dict=options_dict)
  
  @app.route('/study/<string:study_code>/view')
  def view_study(study_code):
    # Find the study by ID (simple example)
    # study = next((s for s in studies_dict if s['study_code'] == study_code), None)
    study = Study.query.filter_by(study_code=study_code).first()
    print(study.to_dict())

  
    if study:
        # Pass study object to template
        return render_template("view_study.html", study=study.to_dict(), view='view', options_dict=options_dict)
    else:
        return f"Study with ID {study_code} not found", 404
  
  
  @app.route('/study/<string:study_code>/add_site', methods=['POST'])
  def add_site_to_study(study_code):
    # study = next((s for s in studies_dict if s['study_code'] == study_code), None)
    study = Study.query.filter_by(study_code=study_code).first()
    site_data = request.form.to_dict()

    new_site = StudySite(**site_data, study_id=study.id)
    db.session.add(new_site)
    db.session.commit()

    s = Study.query.filter_by(study_code=study_code).first()
  
    # return render_template('view_study.html', study=study, view='view', options_dict=options_dict)
    sites_list = [site.to_dict() for site in s.study_sites]
    print(sites_list)

    return jsonify({
        "status": "success",
        "site": sites_list
    })
  
  @app.route('/study/<string:study_code>/add_team_member', methods=['POST'])
  def add_team_member(study_code):
    try:
      # Parse form data
      full_name = request.form.get("full_name")
      study_role = request.form.get("study_role")
      start_date_str = request.form.get("start_date")
      end_date_str = request.form.get("end_date")

      # Convert string to date (if provided)
      start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
      end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None

      # Find the study
      study = Study.query.filter_by(study_code=study_code).first_or_404()

      # Create new team member
      new_member = TeamMember(
          full_name=full_name,
          study_role=study_role,
          start_date=start_date,
          end_date=end_date,
          study=study
      )
      db.session.add(new_member)
      db.session.commit()

      # Return full updated members list
      members_list = [m.to_dict() for m in study.team_members]
      return jsonify({
          "status": "success",
          "members": members_list
      })

    except Exception as e:
      return jsonify({
          "status": "error",
          "message": str(e)
      }), 400
  
  
  
  @app.route('/study/<string:study_code>/add_data_collection_method', methods=['POST'])
  def add_data_collection_method(study_code):
    # study = next((s for s in studies_dict if s['study_code'] == study_code), None)
    study = Study.query.filter_by(study_code=study_code).first()
    data = request.form.to_dict()

    new_data_col = DataColMethod(**data, study_id=study.id)
    db.session.add(new_data_col)
    db.session.commit()
  
    #data_col_method = request.form.to_dict()
    # study = study.to_dict()
    #study["data_col_method"]=data_col_method
    #print(study)
  
    return render_template('view_study.html', study=study.to_dict(), view='view', options_dict=options_dict)
  
  @app.route('/study/<string:study_code>/add_timeline', methods=['POST'])
  def add_study_timeline(study_code):
    study = Study.query.filter_by(study_code=study_code).first()

    # Parse form data
    estimated_fpfv_str = request.form.get("estimated_fpfv")
    estimated_lplv_str = request.form.get("estimated_lplv")
    actual_fpfv_str = request.form.get("actual_fpfv")
    actual_lplv_str = request.form.get("actual_lplv")
    active_years = request.form.getlist("active_years")
    active_years_str = ",".join(active_years)

    # Convert string to date (if provided)
    estimated_fpfv = datetime.strptime(estimated_fpfv_str, "%Y-%m-%d").date() if estimated_fpfv_str else None
    estimated_lplv = datetime.strptime(estimated_lplv_str, "%Y-%m-%d").date() if estimated_lplv_str else None
    actual_fpfv = datetime.strptime(actual_fpfv_str, "%Y-%m-%d").date() if actual_fpfv_str else None
    actual_lplv = datetime.strptime(actual_lplv_str, "%Y-%m-%d").date() if actual_lplv_str else None


    new_timeline= StudyTimeline(estimated_fpfv=estimated_fpfv,
                                estimated_lplv=estimated_lplv,
                                actual_fpfv=actual_fpfv,
                                actual_lplv=actual_lplv,
                                active_years=active_years_str,
                                study=study)
    db.session.add(new_timeline)
    db.session.commit()

   
    #form_data = request.form.to_dict()
    #active_years = request.form.getlist("active_years")
    #print(active_years)
     
    # study = study.to_dict()
    #study["study_timeline"]=form_data
    #print(form_data)
  
    return render_template('view_study.html', study=study.to_dict(), view='view', options_dict=options_dict)
  
  @app.route('/study/<string:study_code>/add_other_details', methods=['POST'])
  def add_other_study_details(study_code):
    #study = next((s for s in studies_dict if s['study_code'] == study_code), None)
    # time_line_data = request.form.to_dict()
    #form_data = request.form.to_dict()  
    #study["other_details"]=form_data
    #
    study = Study.query.filter_by(study_code=study_code).first()
    form_data = request.form.to_dict()

    other_details = OtherDetails(**form_data, study_id=study.id)
    db.session.add(other_details)
    db.session.commit()
  
    return render_template('view_study.html', study=study.to_dict(), view='view', options_dict=options_dict)


#if __name__ == '__main__':
#  app.run(host='0.0.0.0', port=8080, debug=True)