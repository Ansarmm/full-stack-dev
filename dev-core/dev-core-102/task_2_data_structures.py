participants_list = ["Ansar", "Bolat", "Alibek"]
Ansar_info = {"name": "Ansar", "age": "14", "email": "ansar1234@gmail.com"}
Bolat_info = {"name": "Bolat", "age": "20", "email": "bolatik5678@gmail.com"}
Alibek_info = {"name": "Alibek", "age": "27", "email": "bek000@gmail.com"}
coordinates = (43,76)

print(participants_list)
print("About Ansar: ", Ansar_info["name"], Ansar_info["age"], Ansar_info["email"])
print("About Bolat: ", Bolat_info["name"], Bolat_info["age"], Bolat_info["email"])
print("About Alibek: ", Alibek_info["name"], Alibek_info["age"], Alibek_info["email"])

new_participant = input("Add new participant if you want: ")
participants_list.append(new_participant)
removed_participant = input("Remove participant if you want: ")
participants_list.remove(removed_participant)
new_participant_info = {}
new_participant_info["name"] = input("Enter new partcipant`s name: ")
new_participant_info["age"] = int(input("Enter new partcipant`s age: "))
new_participant_info['email'] = input("Enter new participant`s email: ")
print("new participants list: ", participants_list)
print("About new participant: ", new_participant_info["name"], new_participant_info["age"], new_participant_info["email"])
print("coordinates of conferation", coordinates, "(Almaty)")