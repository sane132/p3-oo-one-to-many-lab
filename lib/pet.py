class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {self.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
        
    @property
    def owner(self):
        return self._owner
        
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner) and owner is not None:
            raise Exception("The owner must be an instance of Owner class")
        self._owner = owner