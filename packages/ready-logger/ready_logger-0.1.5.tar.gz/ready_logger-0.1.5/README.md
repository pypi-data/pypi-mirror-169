## Easily configure loggers.

### Use the default logger:
```python
from ready_logger import logger
```

### Use a custom logger:
```python
logger = get_logger(
    name='my-logger',
    log_level='DEBUG',
    log_dir='/home/user/my_logs'
)
```
see [get_logger]('ready_logger/configure.py#L11') for more details.

### Configuration
All `get_logger` arguments besides for `name` can be set via environment variables in the form `READY_LOGGER_{VARIABLE NAME}`.   

To set configuration specific to a named logger,
use the format `{LOGGER NAME}_{VARIABLE NAME}`