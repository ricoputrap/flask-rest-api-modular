from flask import request
from flask_restful import Resource, abort
from project.models.todo import TodoModel
from project.serializers.todo import TodoSchema
from project.utils.util import db

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

class Todo(Resource):

  def get(self):
    todos = TodoModel.query.all()
    return todos_schema.dump(todos)

  def post(self):
    name = request.json['name']
    todo = TodoModel(name=name)
    db.session.add(todo)
    db.session.commit()
    
    return todo_schema.dump(todo)

  def put(self, todo_id):
    todo = TodoModel.query.filter_by(id=todo_id).first()

    if not todo:
      abort(404, message="Could not find todo with that id...")
    
    request_body = request.get_json()

    if "name" in request_body:
      todo.name = request_body['name']
    if "checked" in request_body:
      todo.checked = request_body['checked']
    
    db.session.commit()

    return todo_schema.dump(todo)

  def delete(self, todo_id):
    todo = TodoModel.query.filter_by(id=todo_id).first()

    if not todo:
      abort(404, message="Could not find todo with that id...")

    db.session.delete(todo)
    db.session.commit()

    return {
      'message': f'Todo item with id = {todo_id} has been successfully deleted.'
    }