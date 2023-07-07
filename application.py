from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField
from wtforms.validators import DataRequired, NumberRange
import os
import pickle
import pandas as pd

# Load the preprocessor and models
preprocessor_path = os.path.join(os.getcwd(), 'artifacts', 'models', 'preprocessor.pkl')
with open(preprocessor_path, 'rb') as f:
    preprocessor = pickle.load(f)

heating_load_model_path = os.path.join(os.getcwd(), 'artifacts', 'models', 'heating_load_model.pkl')
with open(heating_load_model_path, 'rb') as f:
    heating_load_model = pickle.load(f)

cooling_load_model_path = os.path.join(os.getcwd(), 'artifacts', 'models', 'cooling_load_model.pkl')
with open(cooling_load_model_path, 'rb') as f:
    cooling_load_model = pickle.load(f)

# Initialize the app
application = Flask(__name__)
app = application
app.config['SECRET_KEY'] = 'a094eea3408c508ab02586c190d2ae03'
app.template_folder = 'templates'

# Energy Efficiency Form
class EnergyEfficiencyForm(FlaskForm):
    relative_compactness = DecimalField('Relative Compactness', validators=[DataRequired(), NumberRange(min=0.6, max=1.0)])
    surface_area = DecimalField('Surface Area', validators=[DataRequired(), NumberRange(min=500, max=900)])
    wall_area = DecimalField('Wall Area', validators=[DataRequired(), NumberRange(min=200, max=400)])
    roof_area = DecimalField('Roof Area', validators=[DataRequired(), NumberRange(min=100, max=500)])
    overall_height = DecimalField('Overall Height', validators=[DataRequired(), NumberRange(min=2.0, max=8.0)])
    orientation = SelectField('Orientation', choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    glazing_area = DecimalField('Glazing Area', validators=[DataRequired(), NumberRange(min=0.0, max=0.5)])
    glazing_area_distribution = SelectField('Glazing Area Distribution', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Energy Efficiency Form
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = EnergyEfficiencyForm()
    if form.validate_on_submit():
        data = {
            'relative_compactness': form.relative_compactness.data,
            'surface_area': form.surface_area.data,
            'wall_area': form.wall_area.data,
            'roof_area': form.roof_area.data,
            'overall_height': form.overall_height.data,
            'orientation': form.orientation.data,
            'glazing_area': form.glazing_area.data,
            'glazing_area_distribution': form.glazing_area_distribution.data
        }
        return redirect(url_for('prediction', **data))
    return render_template('form.html', form=form)

# Energy Efficiency Prediction
@app.route('/prediction', methods=['GET'])
def prediction():
    data = {
        'Relative_Compactness': float(request.args.get('relative_compactness')),
        'Surface_Area': float(request.args.get('surface_area')),
        'Wall_Area': float(request.args.get('wall_area')),
        'Roof_Area': float(request.args.get('roof_area')),
        'Overall_Height': float(request.args.get('overall_height')),
        'Orientation': int(request.args.get('orientation')),
        'Glazing_Area': float(request.args.get('glazing_area')),
        'Glazing_Area_Distribution': int(request.args.get('glazing_area_distribution'))
    }
    df = pd.DataFrame([data])
    df_preprocessed = preprocessor.transform(df)
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=df.columns)
    heating_load = heating_load_model.predict(df_preprocessed)[0]
    cooling_load = cooling_load_model.predict(df_preprocessed)[0]
    heating_load = round(heating_load, 2)
    cooling_load = round(cooling_load, 2)
    return render_template('prediction.html', heating_load=heating_load, cooling_load=cooling_load)

if __name__ == '__main__':
    app.run(debug=True)
