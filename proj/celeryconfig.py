broker_url = 'redis://celery-example_redis_1:6379/0'
result_backend = 'redis://celery-example_redis_1:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Tokyo'
enable_utc = True
include = ['proj.tasks']