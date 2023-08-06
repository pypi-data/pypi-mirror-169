from sqlalchemy import Table, MetaData, Column, JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.attributes import flag_modified

Base = declarative_base()


class StateMachineRun(Base):
    def __init__(self, app) -> None:
        self.app = app
        metadata = MetaData(bind=app.db_engine)

        setattr(
            StateMachineRun,
            "__table__",
            Table(
                "pipeline_state_machine_runs",
                metadata,
                Column("result", MutableDict.as_mutable(JSON)),
                autoload=True,
            ),
        )

        pass

    def result_to_db(self, logical_step_name, state_machine_run_id, results):
        sm_run = self.app.db.query(StateMachineRun).get(state_machine_run_id)
        sm_run.result[logical_step_name] = results

        return self.app.db.commit()
