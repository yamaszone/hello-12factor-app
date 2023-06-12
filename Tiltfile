docker_build('fastapi-app', '.')
k8s_yaml('deployments/app.yaml')
k8s_resource('fastapi-app', port_forwards=8000)
