from character import Character

dave = Character("Dave", "A smelly zombie")
dave.describe()
# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude?")
# Trigger a conversation with Dave
dave.talk()