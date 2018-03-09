from app import db


class User(db.Model):
    # 表的名字:
    __tablename__ = 'oa_system_user'

    # 表的结构:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

    def change_email(self, new_email):
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        db.session.commit()
        return True

    def get_one(self, name):
        return self.query.filter_by(name=name).first()
