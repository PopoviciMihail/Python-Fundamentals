# _var -> protected -> accessible from within the class and are also available to its sub-classes
# __var -> private -> gives a strong suggestion not to touch it from outside the class

# --- Custom containers & Private members ---
class TagCloud:
    _internal_state = 'Valid'  # protected

    def __init__(self, x="default"):
        self.__tags = {}  # private
        self.x = x

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
print(cloud._internal_state)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags) # cannot do this
print(cloud.__dict__)
print(cloud._TagCloud__tags)
