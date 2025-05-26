#!/usr/bin/env python3

# Script goes here!
from config import Base, engine, session
from models import Dev, Company, Freebie

Base.metadata.create_all(engine)

# Sample data
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

alice = Dev(name="Alice")
bob = Dev(name="Bob")

tshirt = Freebie(item_name="T-shirt", value=10, dev=alice, company=google)
mug = Freebie(item_name="Mug", value=15, dev=alice, company=microsoft)

session.add_all([google, microsoft, alice, bob, tshirt, mug])
session.commit()
