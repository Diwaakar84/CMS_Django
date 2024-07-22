class ShardRouter:
    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'Mockapp':
            user_id = hints.get('user_id')
            if user_id is not None:
                if user_id % 3 == 0:
                    return 'shard1'
                elif user_id % 3 == 1:
                    return 'shard2'
                else:
                    return 'shard3'
        return 'default'

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Mockapp':
            user_id = hints.get('user_id')
            if user_id is not None:
                if user_id % 3 == 0:
                    return 'shard1'
                elif user_id % 3 == 1:
                    return 'shard2'
                else:
                    return 'shard3'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        db_obj1 = hints.get('database', None)
        db_obj2 = hints.get('database', None)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        return True
