from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import (User, UserProfile, HealthMetric, FitnessActivity, 
                    NutritionLog, SleepRecord, WellnessGoal, 
                    CommunityPost, Appointment, Professional)
from app import appbuilder, db


class UserProfileView(ModelView):
    datamodel = SQLAInterface(UserProfile)
    list_columns = ['user', 'fitness_level', 'dietary_preferences']
    show_template = 'appbuilder/general/model/show_custom.html'
    
class UserView(ModelView):
    datamodel = SQLAInterface(User)
    list_columns = ['username', 'email', 'active']
    add_columns = ['username', 'email', 'active']
    edit_columns = ['username', 'email', 'active']
    related_views = [UserProfileView]

class HealthMetricView(ModelView):
    datamodel = SQLAInterface(HealthMetric)
    list_columns = ['user', 'metric_type', 'value', 'recorded_at']
    add_columns = ['user', 'metric_type', 'value']

class FitnessActivityView(ModelView):
    datamodel = SQLAInterface(FitnessActivity)
    list_columns = ['user', 'activity_type', 'duration', 'calories_burned']
    show_fieldsets = [
        ('Summary', {'fields': ['user', 'activity_type']}),
        ('Details', {'fields': ['duration', 'calories_burned', 'activity_date']})
    ]

class NutritionLogView(ModelView):
    datamodel = SQLAInterface(NutritionLog)
    list_columns = ['user', 'meal_type', 'calories', 'logged_at']
    search_columns = ['meal_type', 'logged_at']

class SleepRecordView(ModelView):
    datamodel = SQLAInterface(SleepRecord)
    list_columns = ['user', 'sleep_quality', 'duration', 'bedtime']
    add_columns = ['user', 'sleep_quality', 'duration', 'bedtime', 'wake_time']

class WellnessGoalView(ModelView):
    datamodel = SQLAInterface(WellnessGoal)
    list_columns = ['user', 'goal_type', 'target_value', 'current_value', 'completed']
    edit_columns = ['goal_type', 'target_value', 'current_value', 'deadline', 'completed']

class CommunityPostView(ModelView):
    datamodel = SQLAInterface(CommunityPost)
    list_columns = ['user', 'content', 'post_date', 'likes']
    add_columns = ['user', 'content']

class AppointmentView(ModelView):
    datamodel = SQLAInterface(Appointment)
    list_columns = ['user', 'professional', 'appointment_type', 'scheduled_time', 'status']
    add_columns = ['user', 'professional', 'appointment_type', 'scheduled_time', 'duration']

class ProfessionalView(ModelView):
    datamodel = SQLAInterface(Professional)
    list_columns = ['name', 'specialty', 'contact']

appbuilder.add_view(UserProfileView, 'UserProfile', category="User")
appbuilder.add_view(UserView, 'User', category="User")
appbuilder.add_view(HealthMetricView, 'HealthMetric', category="User")
appbuilder.add_view(FitnessActivityView, 'FitnessActivity', category="FitnessActivity")
appbuilder.add_view(NutritionLogView, 'NutritionLog', category="NutritionLog")
appbuilder.add_view(SleepRecordView, 'SleepRecord', category="SleepRecord")
appbuilder.add_view(WellnessGoalView, 'WellnessGoal', category="Goal")
appbuilder.add_view(CommunityPostView, 'Post', category="community")
appbuilder.add_view(AppointmentView, 'Appointment', category="Appointment")
appbuilder.add_view(ProfessionalView, "Professional", category="Professional")

db.create_all()
