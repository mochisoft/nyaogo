from app import db

class Study(db.Model):
  __tablename__ = 'study'
  
  id = db.Column(db.Integer, primary_key=True)
  study_id = db.Column(db.String(20), unique=True, nullable=False)
  protocol_num = db.Column(db.String(20), unique=True, nullable=False)
  protocol_desc = db.Column(db.String(200), nullable=False)
  project_num = db.Column(db.String(20), nullable=False)
  ctgov_num = db.Column(db.String(20), nullable=False)
  research_type = db.Column(db.String(50), nullable=False)
  study_design = db.Column(db.String(50), nullable=False)
  study_sites = db.Column(db.PickleType, nullable=True)
  data_col_method = db.Column(db.PickleType, nullable=True)
  team_members = db.Column(db.PickleType, nullable=True)
  study_timeline = db.Column(db.PickleType, nullable=True)
  other_details = db.Column(db.PickleType, nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
  
  def __repr__(self):
    return f'<Study {self.study_id}>'

        
