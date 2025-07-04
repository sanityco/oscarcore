# test_access_control_manager.py

from access_control_manager import AccessControlManager

acm = AccessControlManager()
acm.define_role("admin", ["read", "write", "delete"])
acm.define_role("user", ["read"])

acm.assign_role("alice", "admin")
acm.assign_role("bob", "user")

print("[Test] Alice can delete:", acm.check_permission("alice", "delete"))
print("[Test] Bob can delete:", acm.check_permission("bob", "delete"))

acm.revoke_role("alice")
print("[Test] Alice after revoke:", acm.check_permission("alice", "read"))
