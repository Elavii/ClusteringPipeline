class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}
        self.items = []

    def get_description(self):
        return self.description

    def link_room(self, room, direction):
        self.exits[direction] = room

    def set_item(self, item):
        self.items.append(item)

    def get_details(self):
        print(f"You're in: {self.get_description()}")
        for direction in self.exits:
            room = self.exits[direction]
            print(f"The {room.get_description()} is {direction}")
    
    def has_item(self, item_name):
        return any(item.get_name().lower() == item_name.lower() for item in self.items)

    def use_item(self, item, player):
        if self.description == "Library":  # Ensure we are in the Library
            if item.get_name().lower() in [x.get_name().lower() for x in required_items]:
                player.inventory.remove(item)  # Remove the item from player's inventory
                player.used_items.append(item)  # Add the item to the used list
                print(f"You place the {item.get_name()} in the ancient chest.")
                # Check if all required items have been used
                if len(player.used_items) == len(required_items):
                    print("The ancient chest glows brightly, and a spell recipe appears!")
                    print("Congratulations, you have mastered the Grand Spell and won the game!")
                    return True
                else:
                    # If not all items have been used yet
                    print("You placed the item, but more components are needed to complete the spell.")
                return False
            else:
                print(f"The {item.get_name()} cannot be used here.")
        else:
            print("There is nothing to use here.")
        return False


    def move(self, direction):
        return self.exits.get(direction, None)

class Item:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
class Player:
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.used_items = []

    def move(self, direction):
        new_room = self.current_room.move(direction)
        if new_room:
            self.current_room = new_room
            self.current_room.get_details()
        else:
            print("You can't go that way.")

    def use_item(self, item_name):
        item = next((item for item in self.inventory if item.get_name().lower() == item_name.lower()), None)
        if item:
            result = self.current_room.use_item(item, self)
            return result
        else:
            print(f"You don't have {item_name}.")
        return False

    def take_item(self, item_name):
        item_name = item_name.lower()
        item = next((item for item in self.current_room.items if item.get_name().lower() == item_name), None)
        if item:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You took the {item_name}.")
        else:
            print(f"There is no {item_name} here.")

    def read_map(self):
        print("You look at your map. It shows the following locations of the magical components:")
        for room in room_list:  # Now using the global room_list
            items_in_room = ", ".join(item.get_name() for item in room.items if not item in self.inventory)
            if items_in_room:
                print(f"{room.get_description()}: {items_in_room}")
            else:
                print(f"{room.get_description()}: No items left here.")

    def has_all_items(self, required_items, used=False):
        if used:
            return not self.inventory  # If used is True, inventory should be empty
        return all(item.get_name().lower() in (inventory_item.get_name().lower() for inventory_item in self.inventory) for item in required_items)
    
def print_intro():
    print("Welcome to the Wizard's Quest.")
    print("As a new student at the mystical Academy of Arcane Arts, you face your first major challenge.")
    print("Your quest is to collect four magical components scattered throughout the academy:")
    print("- Phoenix Feather")
    print("- Unicorn Horn")
    print("- Mermaid's Tear")
    print("- Dragon's Breath")
    print("These components are needed to cast the Grand Spell, which will prove your skills as a master wizard.")
    print("\nCommands you can use:")
    print("- 'go [direction]' or 'move [direction]' to move between rooms (e.g., 'go east')")
    print("- 'take [item]' to pick up an item (e.g., 'take Phoenix Feather')")
    print("- 'inventory' or 'items' to check what you are carrying")
    print("- 'map' or 'read' to see where all the items are located")
    print("- 'look' or 'examine' to get details about your current location")
    print("- 'quit' or 'exit' to leave the game")
    print("\nWould you like to start your adventure? (yes/no)")

def start_game():
    # ... (rest of your setup code here) ...
    # Setting up rooms
    library = Room("Library")
    garden = Room("Botanical Garden")
    alchemy_class = Room("Alchemy Classroom")
    forbidden_tower = Room("Forbidden Tower")

    # Linking rooms
    library.link_room(garden, "east")
    garden.link_room(library, "west")
    library.link_room(alchemy_class, "north")
    alchemy_class.link_room(library, "south")
    alchemy_class.link_room(forbidden_tower, "up")
    forbidden_tower.link_room(alchemy_class, "down")

    # Adding items to rooms
    garden.set_item(Item("Phoenix Feather"))
    alchemy_class.set_item(Item("Unicorn Horn"))
    forbidden_tower.set_item(Item("Mermaid's Tear"))
    forbidden_tower.set_item(Item("Dragon's Breath"))

    # Initializing player
    player = Player()
    player.current_room = library

    global required_items
    required_items = [Item("Phoenix Feather"), Item("Unicorn Horn"), Item("Mermaid's Tear"), Item("Dragon's Breath")]
    global room_list
    room_list = [library, garden, alchemy_class, forbidden_tower]
    # Print the game intro
    player = Player()
    player.current_room = library

    print_intro()
    if input("> ").strip().lower() in ['yes', 'y']:
        player.current_room.get_details()
    else:
        print("Maybe next time. Goodbye!")

    while True:
        command = input("> ").strip().lower().split()  # Normalize the input to handle case sensitivity
        action = command[0] if command else ""
        
        if action in ["go", "move"]:
            if len(command) > 1:
                player.move(command[1])
            else:
                print("Go where?")
        elif action == "use":
            if len(command) > 1:
                game_over = player.use_item(" ".join(command[1:]))  # Use the item
                if game_over:
                    break  # End the game loop if all required items have been successfully used
            else:
                print("Use what?")
        elif action in ["take", "get"]:
            if len(command) > 1:
                player.take_item(" ".join(command[1:]))  # Allow multi-word items
            else:
                print("Take what?")
        elif action in ["inventory", "items"]:
            if player.inventory:
                for item in player.inventory:
                    print(item.get_name())
            else:
                print("Your inventory is empty.")
        elif action in ["look", "examine"]:
            player.current_room.get_details()
        elif action in ["map", "read"]:
            player.read_map()
        elif action in ["quit", "exit"]:
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

        # Check if the player has all required items after each command
        if player.has_all_items(required_items):
            print("Congratulations, you have collected all the magical components and completed the grand spell!")
            break


# Game loop
start_game()