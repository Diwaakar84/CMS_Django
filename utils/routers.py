class ShardRouter:
    def db_for_read(self, model, **hints):
        user_location = hints.get('user_location')
        return self.get_db_for_location(user_location)

    def db_for_write(self, model, **hints):
        user_location = hints.get('user_location')
        return self.get_db_for_location(user_location)

    def get_db_for_location(self, user_location):
        if user_location == 'North America':
            return 'north_america'
        elif user_location == 'Europe':
            return 'europe'
        elif user_location == 'Asia':
            return 'asia'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = hints.get('database', None)
        db_obj2 = hints.get('database', None)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
