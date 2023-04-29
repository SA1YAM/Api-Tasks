import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
#print(current)

parentt = os.path.dirname(current)
sys.path.append(parentt)
#print("parentt",parentt)

parent = os.path.dirname(parentt)
sys.path.append(parent)
#print("parent",parent)
 

from flask_restful import Api, Resource, abort, reqparse, marshal_with, fields, request
from application.data.models import db, Event
from datetime import datetime

# instantiating the api object and binding it with our app
api = Api(prefix = "/api/v3/app")

  
#formatting of date        
class ChangeDateFormat(fields.Raw):
    def format(self, value):
        return value.strftime('%d/%m/%Y %H:%M')
        
class ChangeUserFormat(fields.Raw):
    def format(self, value):
        return value.user_id
        

#output fields of user        
event_fields = {
    "id": fields.Integer,
    "type": fields.String,
    "uid": fields.Integer,
    "name": fields.String,
    "tagline": fields.String,
    "schedule": ChangeDateFormat,
    "description" : fields.String,
    "moderator" : fields.String,
    "category" : fields.String,
    "sub_category" : fields.String,
    "rigor_rank" : fields.Integer,
    "attendees": fields.List(ChangeUserFormat),
    "image": fields.String,
    "errors": fields.List(fields.String)
}

event_fields2 = {
    "id": fields.Integer,
     "errors": fields.List(fields.String),
}


#Events api class for CRUD operations

class Events(Resource):

    @marshal_with(event_fields)
    def get(self):
        event_id = request.args.get('id', type = int)
        print(event_id)
        error_list = []
        
        if event_id:
            event = Event.query.get(int(event_id))
            if(event):
                print(event.id)
                return event, 200
            
            else:
                error_list.append("Event not found, please provise a valid event id")
             
        limit = request.args.get('limit', type = int)
        page_no = request.args.get('page', type = int)
        print(limit, page_no)
        
        if (not event_id) and (not limit) and (not page_no) and (not request.args.get('type')):
            error_list.append("please provide valid query parameters")
        
        if len(error_list) > 0:
            error = {}
            error["errors"] = error_list
            return error, 400
            
          
            
        if limit and page_no:
            events = Event.query.order_by(Event.id.desc()).paginate(page = page_no, per_page = limit)
            print("pagignation", len(events.items))
            return events.items[0], 200
        
        return {}, 400
   
                
    @marshal_with(event_fields2)
    def post(self):
    
        error_list = []
            
        file = request.files['image']

        if(not file):
            error_list.append("image file is not present")
            
        if (not request.form.get("name")):
            error_list.append("name is not present")
            
        if (not request.form.get("tagline")):
            error_list.append("tagline is not present")
            
        if (not request.form.get("schedule")):
            error_list.append("schedule is not present")
        
        if (not request.form.get("description")):
            error_list.append("description is not present")
            
        if (not request.form.get("moderator")):
            error_list.append("moderator is not present")
            
        if (not request.form.get("category")):
            error_list.append("category is not present")
            
        if (not request.form.get("category")):
            error_list.append("category is not present")
            
        if (not request.form.get("sub_category")):
            error_list.append("sub_category is not present")
            
        if (not request.form.get("rigor_rank")):
            error_list.append("rigor_rank is not present")
            
            
        if len(error_list) > 0:
            error = {}
            error["errors"] = error_list
            return error, 400

            
        e1 = Event(
                type = "event", 
                uid = 18, 
                name = request.form.get("name"), 
                tagline = request.form.get("tagline"), 
                schedule = datetime.strptime(request.form.get("schedule"), '%Y-%m-%d %H:%M'), 
                description = request.form.get("description"), 
                image = file.read(),
                moderator = request.form.get("moderator"), 
                category = request.form.get("category"),
                sub_category = request.form.get("sub_category"),
                rigor_rank = request.form.get("rigor_rank"),
                )
                
        db.session.add(e1)
        db.session.commit()
        
        
        return e1,  201
                                
                
                
    @marshal_with(event_fields)
    def put(self, event_id):
    
        error_list = []
            
        file = request.files['image']

        if(not file):
            error_list.append("image file is not present")
            
        if (not request.form.get("name")):
            error_list.append("name is not present")
            
        if (not request.form.get("tagline")):
            error_list.append("tagline is not present")
            
        if (not request.form.get("schedule")):
            error_list.append("schedule is not present")
        
        if (not request.form.get("description")):
            error_list.append("description is not present")
            
        if (not request.form.get("moderator")):
            error_list.append("moderator is not present")
            
        if (not request.form.get("category")):
            error_list.append("category is not present")
            
        if (not request.form.get("category")):
            error_list.append("category is not present")
            
        if (not request.form.get("sub_category")):
            error_list.append("sub_category is not present")
            
        if (not request.form.get("rigor_rank")):
            error_list.append("rigor_rank is not present")
            
            
        if len(error_list) > 0:
            error = {}
            error["errors"] = error_list
            return error, 400
        
        
        event = Event.query.get(event_id)       

        event.image = file.read()          
        event.name = request.form.get("name")
        event.tagline = request.form.get("tagline")
        event.schedule = datetime.strptime(request.form.get("schedule"), '%Y-%m-%d %H:%M')
        event.description = request.form.get("description")
        event.moderator = request.form.get("moderator")
        event.category = request.form.get("category")
        event.sub_category = request.form.get("sub_category")
        event.rigor_rank = request.form.get("rigor_rank")
                
        db.session.commit()
                
        return event,  200

                
                
    
    def delete(self, event_id):
    
        error_list = []
        event = Event.query.get(event_id)
        
        if event:
            db.session.delete(event)
            db.session.commit()
            
            return 200 
            
        else:
            error_list.append("Event not found")
            
        if len(error_list) > 0:
            error = {}
            error["errors"] = error_list
            return error, 400
               
api.add_resource(Events, "/events", "/events/<int:event_id>")
        

