from project import app,USERDATA
from project.implement import write_to_json_file

if __name__ == '__main__':
    app.run(debug = True, port = 8080)

    '''
    User = {}
    User['gary'] = {
        "password":'1234',
        "email":"1234@gmail"
    }
    write_to_json_file(USERDATA, User)
    '''
