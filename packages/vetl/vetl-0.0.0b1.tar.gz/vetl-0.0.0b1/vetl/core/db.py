from sqlite3 import connect
import psycopg2 as pc
import redshift_connector as rc
try:
    from vetl import tool
except:
    import sys
    sys.path.insert(1, '/Users/asyraf/Documents/_Asyraf/# PRIVATE/Workspace/git/asyrafadianto_vetl')
    from vetl import tool

data = {
    "credential":{},
    "session":{}
}
default = {
    "port": {
        "5432": "postgres",
        "5439": "redshift"
    }
}
model = {
    "parameter": {
        "host": str,
        "port": int,
        "dbname": str,
        "username": str,
        "password": str,
        "engine": str
    }
}
message = {
    "error": {
        "credential":{
            "user_args_and_kwargs_together": "Cannot run when both args and kwargs are provided!",
            "user_args_too_much": "Too much args provided!",
            "user_args_mistype": "Invalid data type of provided args!",
            "internal_update_less_input": "Required 'host', 'port', 'dbname', 'username' and 'password' but only got %s!"
        }
    }
}

def start(connection_name):
    pass

def credential(connection_name, *args, **kwargs):
    '''
    Credential CRUD

    Create (Done)
        Provide at least the 'connection_name'
            Example:
                credential('test')
                ~#  <timestamp> Log: Create database credential with connection name 'test' success!

    Retrieve (Done)
        Provide at least the 'connection_name'
            Example:
                print(credential('test'))
                ~#  ...
                #   {}

    Update
        1. Provide a 'connection_name' and multiple 'kwargs' value
            Example:
                credential('test', host='1', port=0, ...)
                ~#  <timestamp> Log: Update database credential (host: 'host', port: 'port', ...) for the connection name 'test' success!
        2. Provide a 'connection_name' and a single 'args' value with 'dict' type
            Example:
                credential('test', {'host':'1', 'port':0, ...})
                ~#  <timestamp> Log: Update database credential (host: 'host', port: 'port', ...) for the connection name 'test' success!

    Delete
        Provide a 'connection_name' and a 'delete' args
            Example:
                credential('test', delete)
                ~#  <timestamp> Log: Delete database credential with connection name 'test' success!

    
    '''
    if len(args) == 0:
        if (len(kwargs) == 0): # Provide only the connection_name
            return _credential_retrieve_(connection_name)
        elif len(kwargs) != 0: # Provide a connection_name and multiple kwargs -> ..., host='', port=0, ...
            if _credential_retrieve_(connection_name) == None:
                _credential_create_(connection_name)
            ckwargs = {}
            for key, value in kwargs.items():
                ckwargs[key] = value
            _credential_update_(connection_name, ckwargs)
    elif len(args) == 1: 
        if len(kwargs) == 0: # Provide connection_name and only one structured args -> ..., {'host':'', 'port':0, ...}
            if type(args[0]) == type({}) :
                if _credential_retrieve_(connection_name) == None:
                    _credential_create_(connection_name)
                _credential_update_(connection_name, args[0])
            elif args[0] == 'delete':
                _credential_delete_(connection_name)
            else:
                raise ValueError(message['error']['credential']['user_args_mistype'])
        elif len(kwargs) != 0:
            raise ValueError(message['error']['credential']['user_args_and_kwargs_together'])
    else:
        raise ValueError(message['error']['credential']['user_args_too_much'])

def _credential_create_(connection_name):
    global data
    data['credential'][connection_name] = {}
    print("<%s> Log: Create database credential with connection name '%s' success!"%(tool.utcnow(), connection_name))

def _credential_retrieve_(connection_name):
    global data
    return data['credential'].get(connection_name)

def _credential_update_(connection_name, *args):
    global data
    required = ['host', 'port', 'dbname', 'username', 'password']
    for key, value in args[0].items():
        if key in required:
            tool.validate_type(value, model['parameter'][key])
            data['credential'][connection_name][key] = value
            if key == 'port':
                if 'engine' in args[0].keys():
                    data['credential'][connection_name]['engine'] = args[0]['engine']
                else:
                    data['credential'][connection_name]['engine'] = default['port'][str(value)]
    print(
        "<%s> Log: Update database credential (host: %s, port: %s, dbname: %s, username: %s, engine: %s) for the connection name '%s' success!"%(
            tool.utcnow()
            ,data['credential'][connection_name].get('host')
            ,data['credential'][connection_name].get('port')
            ,data['credential'][connection_name].get('dbname')
            ,data['credential'][connection_name].get('username')
            ,data['credential'][connection_name].get('engine')
            ,connection_name
        )
    )

def _credential_delete_(connection_name):
    global data
    data['credential'].pop(connection_name)
    print("<%s> Log: Delete database credential with connection name '%s' success!"%(tool.utcnow(), connection_name))

def test():
    try:
        credential(
            'rds-stag'
            ,{
                'host': 'renos-v2-staging-rds.cssnfgwcjwmm.ap-southeast-1.rds.amazonaws.com'
                ,'port': 5432
                ,'dbname': 'renosdb'
                ,'username': 'aws_glue_staging'
                ,'password': '/>jF>YS-22;6x{vHNV.nnq)"_p-h}N7&'
            }
        )
        credential('rds-stag', host='a')
        print(credential('rds-stag'))
    except Exception as e:
        print('Error: %s'%(e))
test()