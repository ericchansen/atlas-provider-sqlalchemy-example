from atlas_provider_sqlalchemy.ddl import print_ddl

from example.one.models import Simple

print_ddl("postgresql", [Simple])
