#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        allowed_attributes = ('first_name')
        if name not in allowed_attributes:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
