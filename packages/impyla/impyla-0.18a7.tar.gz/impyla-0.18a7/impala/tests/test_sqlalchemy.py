# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from sqlalchemy.engine import create_engine
from sqlalchemy import Table, Column
from sqlalchemy.schema import MetaData, CreateTable

from impala.sqlalchemy import STRING, INT, DOUBLE, TINYINT, DATE, VARCHAR
from impala.tests.util import ImpylaTestEnv

TEST_ENV = ImpylaTestEnv()


def test_sqlalchemy_impala_compilation():
    def create_test_engine():
        return create_engine('impala://{0}:{1}'.format(TEST_ENV.host, TEST_ENV.port))

    engine = create_test_engine()
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    mytable = Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE),
                    Column('col5', DATE),
                    Column('col6', VARCHAR(10)),
                    impala_partitioned_by='(part_col STRING)',
                    impala_stored_as='PARQUET',
                    impala_table_properties={
                        'transactional': 'true',
                        'transactional_properties': 'insert_only'
                    })
    observed = str(CreateTable(mytable, bind=engine))
    # The DATE column type of 'col5' will be replaced with TIMESTAMP.
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE, \n\tcol5 TIMESTAMP, \n\tcol6 VARCHAR(10)\n)'
                '\nPARTITIONED BY (part_col STRING)\nSTORED AS PARQUET\n'
                "TBLPROPERTIES ('transactional' = 'true', "
                "'transactional_properties' = 'insert_only')\n\n")
    assert expected == observed

def test_sqlalchemy_impala4_compilation():
    def create_test_engine():
        return create_engine('impala4://{0}:{1}'.format(TEST_ENV.host, TEST_ENV.port))

    engine = create_test_engine()
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    mytable = Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE),
                    Column('col5', DATE),
                    Column('col6', VARCHAR(10)),
                    impala_partitioned_by='(part_col STRING)',
                    impala_stored_as='PARQUET',
                    impala_table_properties={
                        'transactional': 'true',
                        'transactional_properties': 'insert_only'
                    })
    observed = str(CreateTable(mytable, bind=engine))
    # The DATE column type of 'col5' will be left as is.
    expected = ('\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, '
                '\n\tcol3 INT, \n\tcol4 DOUBLE, \n\tcol5 DATE, \n\tcol6 VARCHAR(10)\n)'
                '\nPARTITIONED BY (part_col STRING)\nSTORED AS PARQUET\n'
                "TBLPROPERTIES ('transactional' = 'true', "
                "'transactional_properties' = 'insert_only')\n\n")
    assert expected == observed
