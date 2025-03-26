from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Serper API configuration
SERPER_API_KEY = 'e367025275637ae71d660021a3199b0cb4c63cba'
SERPER_API_URL = 'https://google.serper.dev/search'

@app.route('/', methods=['GET', 'POST'])
def search():
    results = None
    query = ''
    error = None

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        
        if not query:
            error = 'Please enter a search query'
        else:
            try:
                # Prepare headers for Serper API request
                headers = {
                    'X-API-KEY': SERPER_API_KEY,
                    'Content-Type': 'application/json'
                }

                # Make request to Serper API
                response = requests.get(
                    f'{SERPER_API_URL}?q={query}', 
                    headers=headers
                )

                # Check if request was successful
                response.raise_for_status()
                
                # Parse JSON response
                results = response.json()

            except requests.RequestException as e:
                error = f'Error fetching search results: {str(e)}'

    return render_template(
        'search.html', 
        results=results, 
        query=query, 
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)
    