from kv_store import KeyValueStore

def main():
    store = KeyValueStore("test_store.json")
    print("[KV] Başlangıç keys:", store.keys())
    store.set("foo", {"status": "active", "data": 123})
    store.set("bar", [1, 2, 3])
    print("[KV] foo:", store.get("foo"))
    print("[KV] bar:", store.get("bar"))
    store.delete("foo")
    print("[KV] After delete foo, keys:", store.keys())

if __name__ == "__main__":
    main()
