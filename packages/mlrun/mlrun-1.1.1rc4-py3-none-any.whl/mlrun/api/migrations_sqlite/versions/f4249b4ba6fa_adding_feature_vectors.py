# Copyright 2018 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Adding feature vectors

Revision ID: f4249b4ba6fa
Revises: 863114f0c659
Create Date: 2020-11-24 14:43:08.789873

"""
import sqlalchemy as sa
from alembic import op

from mlrun.api.utils.db.sql_collation import SQLCollationUtil

# revision identifiers, used by Alembic.
revision = "f4249b4ba6fa"
down_revision = "863114f0c659"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "feature_vectors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column(
            "project",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("updated", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "state",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column(
            "uid", sa.String(255, collation=SQLCollationUtil.collation()), nullable=True
        ),
        sa.Column("object", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project", "uid", name="_feature_vectors_uc"),
    )
    op.create_table(
        "feature_vectors_labels",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column(
            "value",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column("parent", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["feature_vectors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "parent", name="_feature_vectors_labels_uc"),
    )
    op.create_table(
        "feature_vectors_tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "project",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column(
            "name",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.Column("obj_id", sa.Integer(), nullable=True),
        sa.Column(
            "obj_name",
            sa.String(255, collation=SQLCollationUtil.collation()),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["obj_id"],
            ["feature_vectors.id"],
        ),
        sa.ForeignKeyConstraint(
            ["obj_name"],
            ["feature_vectors.name"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "project", "name", "obj_name", name="_feature_vectors_tags_uc"
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("feature_vectors_tags")
    op.drop_table("feature_vectors_labels")
    op.drop_table("feature_vectors")
    # ### end Alembic commands ###
