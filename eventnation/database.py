from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from eventnation import db

class EventSchema(db.model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(200), nullable=False)

    tickets = db.relationship('Ticket', backref='event', lazy=True)

class TicketSchema(db.model):
    __tablename__='tickets'
    id = db.Column(db.Integer,primary_key=True)
    fk_event=db.Column(db.Integer,ForeignKey('events.id'),nullable=Fasle)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price=db.Column(db.Integer,nullable=False)
    
    event = db.relationship('Event', backref='tickets')
    user = db.relationship('User', backref='tickets')