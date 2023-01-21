##### #!/usr/bin/env python3: we will not need this anymore because we won't be executing our models.py as a script


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()