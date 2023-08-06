from django.conf import settings

auth_db_tables = [
    'cleverstack_auth_user',
    'cleverstack_auth_user_user_permissions',
    'cleverstack_auth_profile',
    'cleverstack_auth_role',
    'cleverstack_auth_customgroup',
    'cleverstack_auth_customgroup_default_permissions',
    'cleverstack_auth_customgroup_permissions',
    'cleverstack_auth_generatetoken',
    'cleverstack_auth_user_groups',
    'cleverstack_auth_apisettings',
    'cleverstack_auth_billingdetail',
    'cleverstack_auth_branch',
    'cleverstack_auth_organisation',
    'cleverstack_auth_department',
    'cleverstack_auth_user_user_permissions'
]

class AuthRouter:

    def db_for_read(self, model, **hints):
        if model._meta.db_table in auth_db_tables:
            return settings.AUTH_DB
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in auth_db_tables:
            return False
        return True

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table in auth_db_tables or obj2._meta.db_table in auth_db_tables:
            return True
        return None