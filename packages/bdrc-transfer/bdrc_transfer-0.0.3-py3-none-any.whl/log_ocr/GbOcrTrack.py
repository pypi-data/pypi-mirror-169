"""
SqlAlchemy ORM for tracking OCR

See ao-google-books/README.md for requirements explanation

Initially, this creates a standalone DB which imports work_ids from the DRS database
We would like to get to declaring the data classes using Reflection, but we need to try
the actual import and creation from logs first.
"""
import argparse
import configparser
import datetime
import os
from collections import namedtuple
from pathlib import Path

import sqlalchemy
from config.config import DBConfig
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

# Code Location of correct LOG_HOME variable


# drs_engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
# Use the qa section, which resolves to a user which has authority to create and drop tables
# - only if you want to create things
# for reading, use 'prod'
drs_cnf: DBConfig = DBConfig('prodcli', '~/.config/bdrc/db_apps.config')

# We need to reach through the DBApps config into the underlying [mysql] config
# parser
engine_cnf = configparser.ConfigParser()
engine_cnf.read(os.path.expanduser(drs_cnf.db_cnf))

drs_conn_str = "mysql+pymysql://%s:%s@%s:%d/%s" % (
    engine_cnf.get(drs_cnf.db_host, "user"),
    engine_cnf.get(drs_cnf.db_host, "password"),
    engine_cnf.get(drs_cnf.db_host, "host"),
    engine_cnf.getint(drs_cnf.db_host, "port", fallback=3306),
    engine_cnf.get(drs_cnf.db_host, "database"))

drs_engine = create_engine(drs_conn_str, echo=False, future=True)

Base.metadata.create_all(drs_engine)

class Works(Base):
    __table__ = Table('Works', Base.metadata, autoload_with=drs_engine)


class Volumes(Base):
    __table__ = Table('Volumes', Base.metadata, autoload_with=drs_engine)


class GbMetadataTrack(Base):
    """
    xxx = GbMetaDataTrack(work_id = workId,upload_time = some_time)
    Record the upload of a work's metadata to GB: columns
    `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time` timestamp NULL DEFAULT NULL,
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `work_id` int(11) DEFAULT NULL,
    `upload_time` datetime NOT NULL,
    `upload_result` int(11) DEFAULT NULL,


    """
    __table__ = Table('GB_Metadata_Track', Base.metadata, autoload_with=drs_engine)

    def __init__(self, *args, **kwargs):
        """
        Use only kwargs
        :param kwargs:
        """
        # Don't need this?-->        super(Base, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)


class GbContentTrack(Base):
    """
    Records the steps in an **image group's** upload status
    """
    __table__ = Table('GB_Content_Track', Base.metadata, autoload_with=drs_engine)

    #
    # id
    # volume_id
    # job_step
    # step_start
    # step_end
    # step_rc

    def __init__(self, *args, **kwargs):
        """
        Use only kwargs
        :param kwargs:
        """
        super().__init__(*args, **kwargs)


class GbOcrTracker():

    drs_session: Session

    def __init__(self):
        """
        Set up the connection
        """
        self.drs_session = Session(drs_engine,autoflush=True, autocommit=True)


    # Not sure if I need a cross db for this, but heck
    # ocr_track_conn_str = f"sqlyte+pysqlite://{os.getenv(GB_LOG_HOME_ENV_KEY)}/GBActivities.db"
    # ocr_track_engine: Engine = create_engine(ocr_track_conn_str, echo=True, future=True)
    # ocr_track_session: Session = Session(ocr_track_engine)


    def add_metadata_upload(self, work_name: str, metadata_upload_date: datetime.datetime, upload_result: int):
        """
        Adds a metadata upload record
        :type work_name: str
        :param work_name: the BDRC work name
        :type metadata_upload_date: datetime
        :param metadata_upload_date:
        :return: the ID of the newly created tracking item
        """

        _ = get_work_id(work_name)
        self.drs_session.add(
            GbMetadataTrack(work_id=_, upload_time=metadata_upload_date,
                            upload_result=upload_result))
        self.drs_session.flush()

    def add_content_activity(self, work_rid: str, image_group_label: str, activity: str, upload_start: datetime.datetime, upload_rc: int) -> int:
        """
        Log a content upload
        :param work_rid: Work containing image group
        :param image_group_label: entity to track
        :param activity: activity type (freeform)
        :param upload_start:
        :return:
        """
        _v = get_volume_id(work_rid, image_group_label)
        self.drs_session.add(
            GbContentTrack(volume_id=_v, step_time=upload_start, job_step=activity,step_rc=upload_rc))
        self.drs_session.flush()


def get_work_id(work_name: str) -> int:
    """
    Return the DRS db work Id for this work. Create it if needed
    :param work_name:
    :return: int primary key in Works
    """

    with drs_engine.begin() as conn:
        work_id_result = conn.execute(sqlalchemy.text("CALL AddWork2  (:p1 , :p2) "), {'p1' : work_name, 'p2': None})
        return work_id_result.first()['workId']

def get_volume_id(work_name: str, image_group_label: str) -> int:
    """
    Return the DRS db work Id for this work. Create it if needed
    :param work_name: work name
    :param image_group_label: image group name
    :return: int primary key in Volumes
    """

    with drs_engine.begin() as conn:
        volume_id_result = conn.execute(sqlalchemy.text("CALL AddVolume2  (:p1 , :p2) "), {'p1' : work_name, 'p2': image_group_label})
        return volume_id_result.first()['volumeId']


def import_track_from_activity_log(log: Path, activity: str):
    """
    Creates records for
    :param log: Path to input log file
    :param activity:
    :return:
    """
    pass


if __name__ == '__main__':
    """
    This is a stub test
    To run, enter the VPN and mount RS2://processing. Or use the default (See ~/.bashrc ) 
    """

    ap = argparse.ArgumentParser()
    ap.add_argument("log_file", help="tracking log to read", type=argparse.FileType('r'))

    args = ap.parse_args(['/Volumes/Processing/logs/google-books-logs/transfer-activity.log'])

    gb_t: GbOcrTracker = GbOcrTracker()

    # each line is
    # log_entry_date:result:operation:operand:operation_type{content|metadata}
    Row = namedtuple('GbLogRow', ('entry_dtm',  'operation', 'result', 'operand', 'op_class'))

    for line in args.log_file.readlines():
        fields = line.strip().split(':')
        _row = Row._make(fields)
        start_time: datetime.datetime = datetime.datetime.strptime(_row.entry_dtm, '%m-%d-%Y %H-%M-%S')
        result: int = 0 if _row.result == 'success' else 1
        if (_row.op_class == 'metadata'):
            gb_t.add_metadata_upload(_row.operand,
                                     start_time,
                                     result)

