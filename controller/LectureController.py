from flask import jsonify, request
from app.app import app
from services.LectureService import LectureService
from models.Lecture import Lecture
import jsonpickle


@app.route("/lectures", methods=["GET"])
def get_lectures():
    lectureService = LectureService()
    lectures = lectureService.read()
    lecturesSerialized = []

    for i in range(0, len(lectures)):
        lecturesSerialized.append(lectures[i].serialize())

    return jsonify(lecturesSerialized), 200


@app.route("/lectures/<int:id>", methods=["GET"])
def get_lecture_by_id(id):
    lectureService = LectureService()
    lecture = lectureService.read_by_id(id)

    if not lecture:
        return jsonify({"error": "not found"}), 404

    return jsonify(lectureService.read_by_id(id).serialize()), 200


@app.route("/lectures", methods=["POST"])
def save_lecture():
    data = request.get_json()
    lectureService = LectureService()

    lecture = Lecture()
    lecture.from_json(data)

    return jsonify(lectureService.create(lecture).serialize()), 201
