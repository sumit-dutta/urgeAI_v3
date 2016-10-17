from tester import app

import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)

app.run(debug=True, host='0.0.0.0', port=8000)