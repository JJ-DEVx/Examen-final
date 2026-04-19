from flask import request, jsonify
from models import Workshop, Registration
from database import db

def init_routes(app):

    @app.route('/workshops', methods=['GET'])
    def get_workshops():
        workshops = Workshop.query.all()
        return jsonify([{
            "id": w.id,
            "name": w.name,
            "description": w.description,  # 👈 AQUI ESTA EL CAMBIO
            "date": w.date,
            "time": w.time,
            "place": w.place,
            "category": w.category
        } for w in workshops]), 200

    @app.route('/workshops/<int:id>', methods=['GET'])
    def get_workshop(id):
        w = Workshop.query.get_or_404(id)
        return jsonify({
            "id": w.id,
            "name": w.name,
            "description": w.description,
            "date": w.date,
            "time": w.time,
            "place": w.place,
            "category": w.category
        }), 200

    @app.route('/workshops', methods=['POST'])
    def create_workshop():
        data = request.json
        new = Workshop(**data)
        db.session.add(new)
        db.session.commit()
        return jsonify({"message": "Workshop creado"}), 201

    @app.route('/workshops/<int:id>', methods=['PUT'])
    def update_workshop(id):
        w = Workshop.query.get_or_404(id)
        data = request.json

        for key, value in data.items():
            setattr(w, key, value)

        db.session.commit()
        return jsonify({"message": "Actualizado"}), 200

    @app.route('/workshops/<int:id>', methods=['DELETE'])
    def delete_workshop(id):
        w = Workshop.query.get_or_404(id)
        db.session.delete(w)
        db.session.commit()
        return jsonify({"message": "Eliminado"}), 200

    @app.route('/workshops/<int:id>/register', methods=['POST'])
    def register(id):
        data = request.json
        reg = Registration(student_name=data["name"], workshop_id=id)
        db.session.add(reg)
        db.session.commit()
        return jsonify({"message": "Registrado"}), 201