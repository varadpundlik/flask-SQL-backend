from flask import Blueprint
from database import EventSchema

router=Blueprint('event', __name__)

@router.route('/',methods=['GET'])
def getAll():
    events_data = Event.query.order_by(Event.id).all()
    
    return "Hello World"