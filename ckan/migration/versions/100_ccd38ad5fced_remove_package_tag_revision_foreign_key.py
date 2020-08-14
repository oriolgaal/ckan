"""Remove package_tag_revision foreign key

Revision ID: ccd38ad5fced
Revises: 3ae4b17ed66d
Create Date: 2020-08-13 20:39:03.031606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd38ad5fced'
down_revision = '3ae4b17ed66d'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(u'package_tag_revision_continuity_id_fkey', u'package_tag_revision',
                       type_=u'foreignkey')
    op.drop_constraint(u'package_tag_revision_package_id_fkey', u'package_tag_revision',
                       type_=u'foreignkey')
    op.drop_constraint(u'package_extra_revision_package_id_fkey', u'package_extra_revision',
                       type_=u'foreignkey')


def downgrade():
    op.create_foreign_key(u'package_tag_revision_continuity_id_fkey', u'package_tag_revision',
                          u'package_tag', [u'continuity_id'], ['id'])
    op.create_foreign_key(u'package_tag_revision_package_id_fkey', u'package_tag_revision',
                          u'package', [u'package_id'], ['id'])
    op.create_foreign_key(u'package_extra_revision_package_id_fkey', u'package_extra_revision',
                          u'package', [u'package_id'], ['id'])