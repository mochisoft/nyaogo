from app import db
from sqlalchemy import UniqueConstraint

class Study(db.Model):
  __tablename__ = 'study'
  
  id = db.Column(db.Integer, primary_key=True)
  study_code = db.Column(db.String(20), unique=True, nullable=False)
  __table_args__ = (
      UniqueConstraint('study_code', name='uq_study_study_code'),
  )
  health_program = db.Column(db.String(50), nullable=False)
  protocol_num = db.Column(db.String(50), unique=True, nullable=False)
  protocol_desc = db.Column(db.String(200), nullable=False)
  project_num = db.Column(db.String(20), nullable=False)
  ctgov_num = db.Column(db.String(20), nullable=True)
  research_type = db.Column(db.String(50), nullable=True)
  study_design = db.Column(db.String(50), nullable=True)
  # data_col_method = db.Column(db.PickleType, nullable=True)
  # team_members = db.Column(db.PickleType, nullable=True)
  # study_timeline = db.Column(db.PickleType, nullable=True)
  # other_details = db.Column(db.PickleType, nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  study_sites = db.relationship(
      "StudySite", back_populates="study", cascade="all, delete-orphan"
  )
  data_col_method = db.relationship(
    "DataColMethod", back_populates="study", cascade=  "all, delete-orphan", uselist= False
    
  )
  team_members = db.relationship(
    "TeamMember", back_populates="study", cascade="all, delete-orphan"
  )
  study_timeline = db.relationship(
    "StudyTimeline", back_populates="study", cascade="all, delete-orphan", uselist= False
  )  
  other_details = db.relationship(
    "OtherDetails", back_populates="study", cascade="all, delete-orphan", uselist= False
  )    

  
  
  def __repr__(self):
    return f'<Study {self.study_code}>'

  def to_dict(self):
    #s = Study.query.filter_by(study_code=study_code).first()
    #sites_list = [site.to_dict() for site in s.study_sites]
    return {
        "id": self.id,
        "study_code": self.study_code,
        "health_program": self.health_program,
        "protocol_num": self.protocol_num,
        "protocol_desc": self.protocol_desc,
        "project_num": self.project_num,
        "ctgov_num": self.ctgov_num,
        "research_type": self.research_type,
        "study_design": self.study_design,
        "created_at": self.created_at,
        "updated_at": self.updated_at,
        "study_sites": [site.to_dict() for site in self.study_sites]  if self.study_sites else [] ,
        "data_col_method": self.data_col_method.to_dict() if self.data_col_method else {},
        "team_members": [member.to_dict() for member in  self.team_members ] if self.team_members else [],
        "study_timeline": self.study_timeline.to_dict() if self.study_timeline else {},
        "other_details": self.other_details.to_dict() if self.other_details else {}
      

      #study_data['study_sites'] = []
      #study_data['data_col_method'] = {}
      #study_data['team_members'] = []
      #study_data['study_timeline'] = {}
      #study_data['other_details'] = {}


    }

class StudySite(db.Model):
  __tablename__ = 'study_site'

  id = db.Column(db.Integer, primary_key=True)
  site_code = db.Column(db.String(20), unique=True, nullable=False)
  study_id = db.Column(db.String, db.ForeignKey("study.id"), nullable=False)
  study = db.relationship("Study", back_populates="study_sites")
  site_name = db.Column(db.String(50), nullable=False)
  site_country_id = db.Column(db.String(50), unique=False, nullable=True)
  site_city = db.Column(db.String(200), nullable=True)
  site_sample_size = db.Column(db.Integer, nullable=True)
  site_pi_name = db.Column(db.String(20), nullable=True)
  site_pi_gender = db.Column(db.String(50), nullable=True)
  pi_location = db.Column(db.String(50), nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())



  def __repr__(self):
    return f'<StudySite {self.site_code}>'

  def to_dict(self):
    return {
        "id": self.id,
        "site_code": self.site_code,
        "study_id": self.study_id,
        "site_name": self.site_name,
        "site_country_id": self.site_country_id,
        "site_city": self.site_city,
        "site_sample_size": self.site_sample_size,
        "site_pi_name": self.site_pi_name,
        "site_pi_gender": self.site_pi_gender,
        "pi_location": self.pi_location,
        "created_at": self.created_at,
        "updated_at": self.updated_at
    }

class DataColMethod(db.Model):
  __tablename__ = 'data_col_method'
  id = db.Column(db.Integer, primary_key=True)
  study_id = db.Column(db.String, db.ForeignKey("study.id"), nullable=False)
  study = db.relationship("Study", back_populates="data_col_method")
  data_collection_tool = db.Column(db.String(50), nullable=True)
  data_collection_tool_other = db.Column(db.String(50), nullable=True)
  randomization = db.Column(db.String(50), nullable=True)
  use_tablets = db.Column(db.String(50), nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
  
  def __repr__(self):
    return f'<DataColMethod {self.id}>'

  def to_dict(self):
    return  {
        "id": self.id,
        "study_id": self.study_id,
        "data_collection_tool": self.data_collection_tool,
        "data_collection_tool_other": self.data_collection_tool_other,
        "randomization": self.randomization,
        "use_tablets": self.use_tablets,
        "created_at": self.created_at,
        "updated_at":self.updated_at       
      
    }

class TeamMember(db.Model):
  
  __tablename__ = 'team_member'
  
  id = db.Column(db.Integer, primary_key=True)
  study_id = db.Column(db.String, db.ForeignKey("study.id"), nullable=False)
  study = db.relationship("Study", back_populates="team_members")
  full_name = db.Column(db.String(50), nullable=False)
  study_role = db.Column(db.String(50), nullable=True)
  start_date = db.Column(db.DateTime, nullable=True)
  end_date = db.Column(db.DateTime, nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

          
  def __repr__(self):
      return f'<TeamMember {self.full_name}>'

  def to_dict(self):
      return {
          "id": self.id,
          "study_id": self.study_id,
          "full_name": self.full_name,
          "study_role": self.study_role,
          "start_date": self.start_date,
          "end_date": self.end_date,
          "created_at": self.created_at,
          "updated_at":self.updated_at
      }

class StudyTimeline(db.Model):
  __tablename__ = 'study_timeline'
  id = db.Column(db.Integer, primary_key=True)
  study_id = db.Column(db.String, db.ForeignKey("study.id"), nullable=False)
  study = db.relationship("Study", back_populates="study_timeline")
  estimated_fpfv = db.Column(db.DateTime, nullable=True)
  estimated_lplv  = db.Column(db.DateTime, nullable=True)
  actual_fpfv = db.Column(db.DateTime, nullable=True)
  actual_lplv = db.Column(db.DateTime, nullable=True)
  active_years = db.Column(db.String(100), nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
  
  def __repr__(self):
    return f'<StudyTimeline {self.id}>'

  def to_dict(self):
    return {
        "id": self.id,
        "study_id": self.study_id,
        "estimated_fpfv": self.estimated_fpfv,
        "estimated_lplv": self.estimated_lplv,
        "actual_fpfv": self.actual_fpfv,
        "actual_lplv": self.actual_lplv,
        "active_years": self.active_years.split(",") if self.active_years else [],
        "created_at": self.created_at,
        "updated_at": self.updated_at
      
    }

class OtherDetails(db.Model):
  __tablename__ = 'other_details'
  
  id = db.Column(db.Integer, primary_key=True)
  study_id = db.Column(db.String, db.ForeignKey("study.id"), nullable=False)
  study = db.relationship("Study", back_populates="other_details")
  find_role = db.Column(db.String(50), nullable=True)
  study_population = db.Column(db.String(50), nullable=True)
  investigational_status = db.Column(db.String(50), nullable=True)
  oir_team = db.Column(db.String(50), nullable=True)
  additional_notes = db.Column(db.String(500), nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  
  def __repr__(self):
    return f'<OtherDetails {self.id}>'

  def to_dict(self):
    return {
        "id": self.id,
        "study_id": self.study_id,
        "find_role": self.find_role,
        "study_population": self.study_population,
        "investigational_status": self.investigational_status,
        "oir_team": self.oir_team,
        "additional_notes": self.additional_notes,
        "created_at": self.created_at,
        "updated_at":self.updated_at
      
    }





  
  
        
