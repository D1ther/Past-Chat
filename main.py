from app import (
    main
)

from app.backend.db.base import (
    creat_db,
    drop_db
)

from app.backend.db.models import *

if __name__ == '__main__':
    drop_db()
    creat_db()
    main()