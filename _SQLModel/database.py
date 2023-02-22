from sqlmodel import SQLModel, create_engine

sqlite_file_name = "_SQLModel/database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)