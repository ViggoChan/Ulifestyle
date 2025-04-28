from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128))
    registered_on = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean(), default=True)
    
    # Relationships
    profile = relationship("app.models.UserProfile", back_populates="user", uselist=False)
    health_metrics = relationship("app.models.HealthMetric", back_populates="user")
    activities = relationship("app.models.FitnessActivity", back_populates="user")
    nutrition_logs = relationship("app.models.NutritionLog", back_populates="user")
    sleep_records = relationship("SleepRecord", back_populates="user")
    goals = relationship("app.models.WellnessGoal", back_populates="user")
    posts = relationship("app.models.CommunityPost", back_populates="user")
    appointments = relationship("app.models.Appointment", back_populates="user")

class UserProfile(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    full_name = Column(String(100))
    bio = Column(Text)
    avatar = Column(String(255))
    fitness_level = Column(String(50))
    dietary_preferences = Column(String(100))
    
    user = relationship("app.models.User", back_populates="profile")

class HealthMetric(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    metric_type = Column(String(50))
    value = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("app.models.User", back_populates="health_metrics")

class FitnessActivity(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    activity_type = Column(String(50))
    duration = Column(Integer)
    calories_burned = Column(Integer)
    activity_date = Column(Date)
    
    user = relationship("app.models.User", back_populates="activities")

class NutritionLog(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    meal_type = Column(String(50))
    calories = Column(Integer)
    protein = Column(Integer)
    carbs = Column(Integer)
    fats = Column(Integer)
    logged_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("app.models.User", back_populates="nutrition_logs")

class SleepRecord(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    sleep_quality = Column(Integer)
    duration = Column(Float)
    bedtime = Column(DateTime)
    wake_time = Column(DateTime)
    
    user = relationship("app.models.User", back_populates="sleep_records")

class WellnessGoal(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    goal_type = Column(String(50))
    target_value = Column(Float)
    current_value = Column(Float)
    deadline = Column(Date)
    completed = Column(Boolean, default=False)
    
    user = relationship("app.models.User", back_populates="goals")

class CommunityPost(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    post_date = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0)
    
    user = relationship("app.models.User", back_populates="posts")

class Appointment(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    professional_id = Column(Integer, ForeignKey('professional.id'))
    appointment_type = Column(String(100))
    scheduled_time = Column(DateTime)
    duration = Column(Integer)
    status = Column(String(20))
    
    user = relationship("app.models.User", back_populates="appointments")
    professional = relationship("app.models.Professional")

class Professional(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    specialty = Column(String(100))
    contact = Column(String(100))
    
    appointments = relationship("app.models.Appointment", back_populates="professional")