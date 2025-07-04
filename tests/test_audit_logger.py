from audit_logger import AuditLogger

def main():
    audit = AuditLogger()

    audit.log_event(
        user="alice",
        action="create",
        resource="project-123",
        details={"description": "Initial project creation"}
    )

    audit.log_event(
        user="bob",
        action="delete",
        resource="project-456",
        details={"reason": "Project deprecated"}
    )

if __name__ == "__main__":
    main()
