bus = {1:{'name':'olio','breed':'german shepherd','pickup_time':'2pm','dropoff_time':'3pm'}, 2:{'name':'oreo','breed':'golden retriever','pickup_time':'3pm','dropoff_time':'4pm'}, 3:{'name':'sally','breed':'pamelian','pickup_time':'3pm','dropoff_time':'4pm'}}
for seat, pet in bus.items():
  print(seat,pet['name'],pet['pickup_time'])
MAX_SEATS = 4
if len(bus)<MAX_SEATS:
  fields = ['name','breed','pickup_time','dropoff_time']
  new_pet = {}
  for field in fields:
    new_pet[field] = input(f"Enter {field}: ")
  next_seat = len(bus) + 1
  bus[next_seat] = new_pet
for seat, pet in bus.items():
  print(seat,pet['name'],pet['pickup_time'])
leaves_early = input('Enter the name of pet who leaves early: ')
for seat, pet in bus.items():
  if pet['name'] == leaves_early:
    del bus[seat]
    break
bus = {i+1: pet for i, pet in enumerate(bus.values())}
for seat, pet in bus.items():
  print(seat, pet['name'], pet['dropoff_time'])