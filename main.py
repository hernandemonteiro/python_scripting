from jenkins import Jenkins


jenkins_server = Jenkins(
    'http://localhost:3005', username='admin', password='admin')
print(jenkins_server.get_version())
