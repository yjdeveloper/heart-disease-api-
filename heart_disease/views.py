from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('heart_disease/model.pkl', 'rb'))

# Create your views here.
@csrf_exempt
def predict(request):
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    chest_pain_type = request.POST.get('chest_pain_type')
    resting_bp_s = request.POST.get('resting_bp_s')
    cholesterol = request.POST.get('cholesterol')
    fasting_blood_sugar = request.POST.get('fasting_blood_sugar')
    resting_ecg = request.POST.get('resting_ecg')
    max_heart_rate = request.POST.get('max_heart_rate')
    exercise_angina = request.POST.get('exercise_angina')
    oldpeak = request.POST.get('oldpeak')
    ST_slope = request.POST.get('ST_slope')

    attr = [
        age, sex, chest_pain_type, resting_bp_s, cholesterol, fasting_blood_sugar,
        resting_ecg, max_heart_rate, exercise_angina, oldpeak, ST_slope
        ]
    
    data = pd.DataFrame([attr], columns =['age', 'sex', 
                                      'chest_pain_type', 
                                      "resting_bp_s", "cholesterol", 
                                      'fasting_blood_sugar', 'resting_ecg', 
                                      'max_heart_rate', 
                                      'exercise_angina', 
                                      'oldpeak', 'ST_slope'
                                      ])
    
    result = model.predict(data)[0]

    if result == 1:
        return JsonResponse({'disease': 'YES'})
    else:
        return JsonResponse({'disease': 'NO'})



    return JsonResponse({'result':result})