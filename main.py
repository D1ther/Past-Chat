from app import (
    main
)

from pyngrok import (
    ngrok
)

from app.backend.db.db_tests import (
    start_db_tests
)

from app.backend.db.models import *
 
if __name__ == '__main__':
    # start_db_tests()
    # ngrok.kill()
    # ngrok.set_auth_token('2wMlBkUMRZPP2xwFHCvTLwHVAPx_CPvmqbEJDtGMu2P3WxDW')
    # print(f'NGROK URL: {ngrok.connect(5000)}')
    main()