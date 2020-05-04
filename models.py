from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model) :
    _tablename_ = "results"

    id = db.column(db.Integer, primary_key = True)
    url = db.column(db.String())
    result_all = db.column(JSON)
    result_no_stop_words = db.column(JSON)


    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
