import logging
import colorlog
from blessed import Terminal
from django.db import connection
import json

# Initialize terminal for enhanced output
terminal = Terminal()

def setup_api_db_logging():
    """Setup API database logging only"""
    logger = logging.getLogger('api_db_operations')
    logger.setLevel(logging.INFO)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Console handler with colors
    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Color formatter for API database operations
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - API-DB - %(message)s",
        datefmt='%H:%M:%S',
        log_colors={
            'INFO': 'cyan',
            'WARNING': 'yellow', 
            'ERROR': 'red',
        }
    )
    
    console_handler.setFormatter(color_formatter)
    logger.addHandler(console_handler)
    
    return logger

# Get API database logger
api_db_logger = logging.getLogger('api_db_operations')

def print_api_db_operation(method, endpoint, operation, table, details=""):
    """Print API database operation with color"""
    if operation.upper() in ['CREATE', 'INSERT', 'POST']:
        print(terminal.green(f"🟢 {method} {endpoint} → DB CREATE in {table} {details}"))
    elif operation.upper() in ['UPDATE', 'PUT', 'PATCH']:
        print(terminal.yellow(f"🟡 {method} {endpoint} → DB UPDATE in {table} {details}"))
    elif operation.upper() in ['DELETE']:
        print(terminal.red(f"🔴 {method} {endpoint} → DB DELETE from {table} {details}"))
    elif operation.upper() in ['READ', 'GET']:
        print(terminal.blue(f"🔵 {method} {endpoint} → DB READ from {table} {details}"))

class APILoggingMiddleware:
    """Middleware to log database operations through API calls only"""
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Only log for API endpoints
        if self.is_api_request(request):
            # Count queries before request
            queries_before = len(connection.queries)
            
            response = self.get_response(request)
            
            # Count queries after request  
            queries_after = len(connection.queries)
            query_count = queries_after - queries_before
            
            if query_count > 0:
                self.log_api_db_operations(request, response, queries_before, queries_after)
        else:
            response = self.get_response(request)
        
        return response
    
    def is_api_request(self, request):
        """Check if request is an API call based on our Food5 project structure"""
        # Skip admin and static files
        excluded_paths = ['/admin/', '/static/', '/media/', '__debug__']
        if any(path in request.path for path in excluded_paths):
            return False
        
        # Include requests that are likely API calls for our Food5 apps
        api_indicators = [
            # JSON content type (REST API calls)
            request.content_type == 'application/json',
            # requests to your app endpoints (GET, POST, PUT, DELETE)
            request.method in ['GET', 'POST', 'PUT', 'DELETE'],
            # Any request with Accept: application/json header
            'application/json' in request.META.get('HTTP_ACCEPT', ''),
            # Requests to your app patterns (based on your app names)
            any(app in request.path for app in [
                'drink', 'bread', 'dessert', 'customer', 
                'menu', 'order', 'first-course', 'second-course'
            ]),
            # DRF browsable API requests
            'browsable' in request.META.get('HTTP_ACCEPT', ''),
        ]
        
        return any(api_indicators)
    
    def log_api_db_operations(self, request, response, queries_before, queries_after):
        """Log database operations for API requests"""
        method = request.method
        endpoint = request.path
        status_code = response.status_code
        
        # Log each query
        for query in connection.queries[queries_before:queries_after]:
            sql = query['sql'].strip()
            time_taken = query['time']
            
            # Determine operation type and table
            operation, table = self.parse_sql_operation(sql)
            
            # Create log message
            details = f"({time_taken}s, status: {status_code})"
            
            api_db_logger.info(f"{method} {endpoint} → {operation} on {table} - {details}")
            print_api_db_operation(method, endpoint, operation, table, details)
    
    def parse_sql_operation(self, sql):
        """Parse SQL to determine operation type and table"""
        sql_upper = sql.upper().strip()
        
        # Determine operation type
        if sql_upper.startswith('SELECT'):
            operation = 'READ'
        elif sql_upper.startswith('INSERT'):
            operation = 'CREATE'
        elif sql_upper.startswith('UPDATE'):
            operation = 'UPDATE'
        elif sql_upper.startswith('DELETE'):
            operation = 'DELETE'
        else:
            operation = 'QUERY'
        
        # Extract table name
        table = "unknown_table"
        try:
            if 'FROM' in sql_upper:
                # SELECT queries
                parts = sql_upper.split('FROM')[1].split()
                table = parts[0].strip('`"').replace('"', '').replace('`', '')
            elif 'INTO' in sql_upper:
                # INSERT queries
                parts = sql_upper.split('INTO')[1].split()
                table = parts[0].strip('`"').replace('"', '').replace('`', '')
            elif 'UPDATE' in sql_upper:
                # UPDATE queries
                parts = sql_upper.split('UPDATE')[1].split()
                table = parts[0].strip('`"').replace('"', '').replace('`', '')
            
            # Clean table name (remove schema prefix if exists)
            if '.' in table:
                table = table.split('.')[-1]
            
            # Simplify table names for Food5 apps
            if table.startswith('app_'):
                # Convert app_drink_drink to just "drinks"
                parts = table.split('_')
                if len(parts) >= 3:
                    app_name = parts[1]
                    table = f"{app_name}s" if not app_name.endswith('s') else app_name
                
        except Exception:
            table = "unknown_table"
        
        return operation, table