import tutorial_pb2 as pb

AddressBook = pb.AddressBook()
person = AddressBook.people.add()
person.name = "first_name"
person.id = 66
person.email = "email@gamil.com"
phone = person.phones.add()
phone.number = "18808080808"
phone.type = 2

print(AddressBook)
data = AddressBook.SerializeToString()
print(data)

AddressBook = pb.AddressBook()
AddressBook.ParseFromString(data)
print(AddressBook)
