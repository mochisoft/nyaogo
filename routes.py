from flask import request, render_template,jsonify
# app = Flask(__name__)
from data_model import studies_dict, options_dict, site_dict


def register_routes(app, db):
  
  
  
  def save_study(study):
    studies_dict.append(study)
    
  
  @app.route('/')
  def hello_world():
  
    return render_template('home.html', studies=studies_dict)
  
  
  @app.route('/study/study', methods=['GET'])
  def add_new_study():
  
    return render_template('new_study.html', options_dict=options_dict)
  
  
  @app.route('/study/add', methods=['POST'])
  def view_new_study():
    study = request.form.to_dict()
    study['study_sites'] = []
    study['data_col_method'] = {}
    study['team_members'] = []
    study['study_timeline'] = {}
    study['other_details'] = {}
    save_study(study)
  
    return render_template('view_study.html', study=study, view='new', options_dict=options_dict)
  
  @app.route('/study/<string:study_id>/view')
  def view_study(study_id):
    # Find the study by ID (simple example)
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
  
    if study:
        # Pass study object to template
        return render_template("view_study.html", study=study, view='view', options_dict=options_dict)
    else:
        return f"Study with ID {study_id} not found", 404
  
  
  @app.route('/study/<string:study_id>/add_site', methods=['POST'])
  def add_site_to_study(study_id):
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
    
    site_data = request.form.to_dict()
    # study = study.to_dict()
    study["study_sites"].append(site_data)
    print(site_data)
  
    # return render_template('view_study.html', study=study, view='view', options_dict=options_dict)
    return jsonify({
        "status": "success",
        "site": site_data
    })
  
  @app.route('/study/<string:study_id>/add_team_member', methods=['POST'])
  def add_team_member(study_id):
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
  
    team_member_data = request.form.to_dict()
    # study = study.to_dict()
    study["team_members"].append(team_member_data)
    print(team_member_data)
  
    # return render_template('view_study.html', study=study, view='view', options_dict=options_dict)
    return jsonify({
        "status": "success",
        "member": team_member_data
    })
  
  
  
  @app.route('/study/<string:study_id>/add_data_collection_method', methods=['POST'])
  def add_data_collection_method(study_id):
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
  
    data_col_method = request.form.to_dict()
    # study = study.to_dict()
    study["data_col_method"]=data_col_method
    print(study)
  
    return render_template('view_study.html', study=study, view='view', options_dict=options_dict)
  
  @app.route('/study/<string:study_id>/add_timeline', methods=['POST'])
  def add_study_timeline(study_id):
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
  
    # time_line_data = request.form.to_dict()
    form_data = request.form.to_dict()
    active_years = request.form.getlist("active_years")
    print(active_years)
  
    form_data["active_years"] = active_years
    # study = study.to_dict()
    study["study_timeline"]=form_data
    print(form_data)
  
    return render_template('view_study.html', study=study, view='view', options_dict=options_dict)
  
  @app.route('/study/<string:study_id>/add_other_details', methods=['POST'])
  def add_other_study_details(study_id):
    study = next((s for s in studies_dict if s['study_id'] == study_id), None)
  
    # time_line_data = request.form.to_dict()
    form_data = request.form.to_dict()
  
    study["other_details"]=form_data
  
    return render_template('view_study.html', study=study, view='view', options_dict=options_dict)


#if __name__ == '__main__':
#  app.run(host='0.0.0.0', port=8080, debug=True)