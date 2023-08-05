from wedeliver_core import WeDeliverCore


class Transactions(object):
    savepoint = None
    db = None

    def __init__(self, savepoint):
        app = WeDeliverCore.getApp()

        self.db = app.extensions['sqlalchemy'].db
        self.savepoint = savepoint

    @staticmethod
    def atomic(session):
        savepoint = session.begin_nested()
        return Transactions(savepoint)

    def __enter__(self):
        return self

    def __exit__(self, a, error, traceback):
        if error:
            if self.savepoint.is_active:
                self.savepoint.rollback()

            self.db.session.rollback()
            raise error

        self.db.session.commit()

    def commit(self, instance):
        self.db.session.add(instance)
        if not self.savepoint.is_active:
            self.savepoint = self.db.session.begin_nested()

        self.savepoint.commit()
