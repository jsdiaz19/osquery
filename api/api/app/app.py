from flask import Flask, jsonify, json
from flask import Flask, render_template
from routes import init_api_routes
import osquery

app = Flask(__name__)
@app.route("/user")

def QueryU():
    instance = osquery.SpawnInstance()
    instance.open()
    result = instance.client.query("SELECT * FROM users")
    return jsonify(result.response[0])

@app.route("/version")

def makeQuery():
	instance = osquery.SpawnInstance()
	instance.open()
	result = instance.client.query("SELECT version FROM os_version")
	return jsonify(result.response[0])


@app.route("/processes")

def Query():
    instance = osquery.SpawnInstance()
    instance.open()
    result = instance.client.query("SELECT * FROM processes")
    return jsonify(result.response[0])

@app.route("/time")

def Query2():
    instance = osquery.SpawnInstance()
    instance.open()
    result = instance.client.query("SELECT * FROM cpu_time")
    return jsonify(result.response[0])

@app.route("/memory")

def Query3():
    instance = osquery.SpawnInstance()
    instance.open()
    result = instance.client.query("SELECT memory_total FROM memory_info")
    return jsonify(result.response[0])


@app.route("/paquete")

def Query4():
    instance = osquery.SpawnInstance()
    instance.open()
    result = instance.client.query("SELECT * FROM deb_packages")
    return jsonify(result.response[0])

# def main():
#     makeQuery("SELECT * FROM processes")
#     makeQuery("SELECT * FROM cpu_time")
#     makeQuery("SELECT version FROM os_version")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
