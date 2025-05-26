#!/usr/bin/env python3
from models import session, Company, Dev, Freebie
from config import Base, engine

# Create tables
Base.metadata.create_all(engine)

# Optional: seed check
alice = session.query(Dev).filter_by(name="Alice").first()
print(alice.companies)

import ipdb; ipdb.set_trace()


alice = session.query(Dev).filter_by(name="Alice").first()
print(alice.companies)          # Should return Google & Microsoft
print(alice.received_one("T-shirt"))  # True
alice.freebies[0].print_details()     # "Alice owns a T-shirt from Google"

bob = session.query(Dev).filter_by(name="Bob").first()
alice.give_away(bob, alice.freebies[0])
session.commit()


