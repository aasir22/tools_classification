from flask import Flask, request, jsonify, render_template, flash, redirect
import os
from predict import rps
from werkzeug.utils import secure_filename
from flask import Response


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)


# CORS(app)


# @cross_origin()
# class ClientApp:
#     def __init__(self):
#         self.filename = "r.png"
#         self.classifier = rps(self.filename)



@app.route("/", methods=['GET'])
# @cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET','POST'])
# @cross_origin()
def upload():
    try:
        if request.method == 'POST':
            # Get the file from post request
            f = request.files['file']

            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)

            rps_ob = rps(file_path)
            result = rps_ob.prediction()
            print(result, 'main folder')

            return (str(result))
        return None


    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        print('exception occured exception is ' + str(e))
        return Response("Error Occurred! %s" % e)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    # clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=2100, debug=True)

