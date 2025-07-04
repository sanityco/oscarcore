from resource_manager import ResourceManager

if __name__ == "__main__":
    rm = ResourceManager(10)

    assert rm.allocate(3) is True
    assert rm.allocate(8) is False

    rm.release(2)
    assert rm.allocate(5) is True

    status = rm.status()
    print(f"[Test] Resource status: {status}")
