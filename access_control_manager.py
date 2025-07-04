# access_control_manager.py

class AccessControlManager:
    def __init__(self):
        self.roles = {}  # role -> set of permissions
        self.user_roles = {}  # user -> role

    def define_role(self, role, permissions):
        self.roles[role] = set(permissions)

    def assign_role(self, user, role):
        if role in self.roles:
            self.user_roles[user] = role
        else:
            raise ValueError(f"Role {role} not defined")

    def check_permission(self, user, permission):
        role = self.user_roles.get(user)
        if not role:
            return False
        return permission in self.roles.get(role, set())

    def revoke_role(self, user):
        if user in self.user_roles:
            del self.user_roles[user]
