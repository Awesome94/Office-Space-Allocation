# Room Space Allocation
Space allocation system for amity Facility. 

Amity has rooms which can be offices or living Spaces. These rooms are allocated to people in the amity facility and these people can either be Staff or Fellows. Only a Fellow can be given a living Space on top of office space.  

## Installation.
clone the Repo into a folder of your choice
```
git clone https://github.com/Awesome94/Office-Space-Allocation.git
```
Create a virtual enviroment.
```
virtualenv amity_env
```
Navigate to the root folder.
```
cd office-space-allocation
```
Install the packages.
```
pip install -r requirements.txt
```
## Launching the Program.
```
python app.y
```
## Running.
Run ```Create_room <room_type> <room_name>``` to create a new room.

Run ```add_person<first_name> <last_name> <designation> <--wants_accomodation=N/Y>``` to add a person and assign them accommodation if they are of designation f(fellows).

Run ```save_state<db_name>``` to save the current state of the program to any database name of your choice.

Run ```load_state<file_name>``` to load data from any existing SQL database.

Run ```load_people<file_name>``` to load data from any ```.txt``` format file.

Run ```reallocate_person <person_id> <current_room_type> <new room name>``` to transfer a person from one room to another

Run ```print_room<room_name>``` to see the members in a given room.

Run ``` print_unallocated``` to print people that have not been allocated rooms.

Run ```print_allocations``` to print a list of people and the rooms they have been allocated to

## Testing.
```
nosetests
```
### Credits.
[Awesome](https://github.com/Awesome94)
