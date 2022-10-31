from flask import Flask

# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)

# @app.route('/courses/<id>')
# def courses(id):
#     return f'Course id: {id}'
@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/<course_id>/lessons/<lesson_id>')
def courses(course_id, lesson_id):
    return f'Course id: {course_id}, Lesson id: {lesson_id}'

