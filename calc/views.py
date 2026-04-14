from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')
def calculate(request):
    # 1. Initialize 'res' with a default value
    res = None 
    
    try:
        # 2. Get data from the POST request
        val1 = int(request.POST.get('num1', 0))
        val2 = int(request.POST.get('num2', 0))
        operation = request.POST.get('operation')

        # 3. Perform Logic
        if operation == 'add':
            res = val1 + val2
        elif operation == 'subtract':
            res = val1 - val2
        elif operation == 'multiply':
            res = val1 * val2
        elif operation == 'divide':
            try:
                res = val1 / val2
            except ZeroDivisionError:
                res = "Error: You cannot divide by zero."
            else:
                res = "Error: Division by zero"
        else:
            res = "No operation selected"
            
    except (ValueError, TypeError):
        res = "Invalid Input: Please enter numbers only."

    # 4. Pass 'res' to the template
    return render(request, 'result.html', {'result': res})