from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
import numpy as np
import pandas as pd
from .models import Homes
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_absolute_percentage_error
from .forms import HouseForm

# Create your views here.

homes = pd.DataFrame(list(Homes.objects.all().values()))
x_train = np.c_[homes['beds'], homes['baths'], homes['square_feet'], 
                homes['year_built'], homes['garages'], homes['lot_sqft']]
y_train = np.array(homes['price'])
steps = [('scaler', StandardScaler()),
        ('poly', PolynomialFeatures(3, include_bias=False)),
        ('model', Ridge(alpha=11.1))]
pipe = Pipeline(steps)
model = pipe.fit(x_train, y_train)
yhat = model.predict(x_train)
error = mean_absolute_percentage_error(yhat, y_train)

def index(request):
    if request.method == "POST":
        beds = request.POST["beds"]
        baths = request.POST["baths"]
        square_feet = request.POST["square_feet"]
        year_built = request.POST["year_built"]
        garages = request.POST["garages"]
        lot_sqft = request.POST["lot_sqft"]
        pred = model.predict([[
            beds, baths, square_feet, year_built, garages, lot_sqft]])
        return render(request, "predict/index.html", {
            "error": round(error * 100, 3),
            "prediction": f"{round(pred[0]):,}",
            "form": HouseForm()
        })
    if "house" not in request.session:
        request.session["house"] = []
    return render(request, "predict/index.html", {
        "error": round(error * 100, 3),
        "form": HouseForm()
    })

def saved(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            beds = form.cleaned_data["beds"]
            baths = float(form.cleaned_data["baths"])
            square_feet = form.cleaned_data["square_feet"]
            year_built = form.cleaned_data["year_built"]
            garages = form.cleaned_data["garages"]
            lot_sqft = form.cleaned_data["lot_sqft"]
            price_int = round(model.predict([[
                beds, baths, square_feet, year_built, garages, lot_sqft
                ]])[0])
            price = "$" + f"{price_int:,}"
            request.session["house"] += [[
                beds, baths, square_feet, year_built, 
                garages, lot_sqft, price]]
        return HttpResponseRedirect(reverse("saved"))
    return render(request, "predict/saved.html", {
        "houses": request.session["house"]
    })
