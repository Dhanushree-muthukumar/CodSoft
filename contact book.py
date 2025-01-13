contacts = []

while (a := input("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit\nChoose: ")) != "6":
    if a == "1":
        contacts.append({k: input(f"{k}: ") for k in ["Name", "Phone", "Email"]})
    elif a == "2":
        print("\n".join(f"{c['Name']} - {c['Phone']}" for c in contacts) or "No contacts.")
    elif a == "3":
        b = input("Search Name/Phone; ").lower()
        print("\n".join(f"{c}" for c in contacts if b in c["Name"].lower() or b in c["Phone"]) or "Not found.")
    elif a == "4":
        b = input("Update Name/Phone: ").lower()
        for c in contacts:
            if b in c["Name"].lower() or b in a["Phone"]:
                c.update({k: input(f"{k} ({c[k]}): ") or c[k] for k in c})
                print("Updated");
                break
        else:
            print("Not found.")
    elif a == "5":
        b = input("Delete Name/Phone: ").lower()
        contacts = [c for c in contacts if b not in c["Name"].lower() and b not in c["Phone"]]
        print("Deleted")

