from flask import request, jsonify
from models import Workshop, Registration
from database import db

def init_routes(app):

    # Obtener todos los talleres
    @app.route('/workshops', methods=['GET'])
    def get_workshops():
        workshops = Workshop.query.all()
        return jsonify([{
            "id": w.id,
            "name": w.name,
            "description": w.description,
            "date": w.date,
            "time": w.time,
            "place": w.place,
            "category": w.category
        } for w in workshops]), 200

    # Obtener un taller
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

    # Crear taller (ARREGLADO)
    @app.route('/workshops', methods=['POST'])
    def create_workshop():
        data = request.get_json()

        print("DEBUG DATA:", data)  # 👈 para verificar en logs

        new = Workshop(
            name=data.get("name", ""),
            description=data.get("description", ""),
            date=data.get("date", ""),
            time=data.get("time", ""),
            place=data.get("place", ""),
            category=data.get("category", "")
        )

        db.session.add(new)
        db.session.commit()

        return jsonify({"message": "Workshop creado"}), 201

    # Actualizar taller
    @app.route('/workshops/<int:id>', methods=['PUT'])
    def update_workshop(id):
        w = Workshop.query.get_or_404(id)
        data = request.get_json()

        w.name = data.get("name", w.name)
        w.description = data.get("description", w.description)
        w.date = data.get("date", w.date)
        w.time = data.get("time", w.time)
        w.place = data.get("place", w.place)
        w.category = data.get("category", w.category)

        db.session.commit()

        return jsonify({"message": "Actualizado"}), 200

    # Eliminar taller
    @app.route('/workshops/<int:id>', methods=['DELETE'])
    def delete_workshop(id):
        w = Workshop.query.get_or_404(id)
        db.session.delete(w)
        db.session.commit()
        return jsonify({"message": "Eliminado"}), 200

    # Registrar estudiante
    @app.route('/workshops/<int:id>/register', methods=['POST'])
    def register(id):
        data = request.get_json()
        reg = Registration(student_name=data.get("name", ""), workshop_id=id)
        db.session.add(reg)
        db.session.commit()
        return jsonify({"message": "Registrado"}), 201