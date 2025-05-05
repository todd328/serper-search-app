 
# Serper Search App
 
![Serper Logo](https://serper.dev/_next/static/media/serper-logo.a4214a22.svg)
 
A powerful search application that leverages the Serper API to provide fast, accurate Google search results. This application allows you to perform web searches, retrieve comprehensive search data, and integrate search capabilities into your projects.
 
## 🌟 Features
 
- **Lightning-Fast Search Results**: Get Google search results in just 1-2 seconds
- **Comprehensive Search Data**: Access various search verticals including:
  - Web pages
  - Images
  - News
  - Maps
  - Places
  - Videos
  - Shopping
  - Scholar
  - Patents
  - Autocomplete suggestions
- **Rich Search Response Data**:
  - Knowledge Graph information
  - Organic search results
  - "People Also Ask" questions
  - Related searches
- **Customizable Query Location**: Set specific geographic locations for more relevant search results
- **Multiple Search Types**: Support for different search verticals and result formats
- **Simple Integration**: Easy to integrate with other applications and services
 
## 📋 Prerequisites
 
- Node.js (v14 or higher)
- npm or yarn package manager
- Serper API key (get one at [Serper.dev](https://serper.dev/))
 
## 🚀 Installation
 
1. Clone this repository:
```bash
git clone https://github.com/yourusername/serper-search-app.git
cd serper-search-app
```
 
2. Install dependencies:
```bash
npm install
# or
yarn install
```
 
3. Create a `.env` file in the root directory with your Serper API key:
```
SERPER_API_KEY=your_api_key_here
```
 
4. Start the application:
```bash
npm start
# or
yarn start
```
 
## 🔧 Configuration
 
The application can be configured through environment variables:
 
| Variable | Description | Default |
|----------|-------------|---------|
| `SERPER_API_KEY` | Your Serper API key (required) | - |
| `PORT` | Port for the server to listen on | 3000 |
| `DEFAULT_NUM_RESULTS` | Default number of results to return | 10 |
| `DEFAULT_COUNTRY` | Default country code for searches | "us" |
| `DEFAULT_LANGUAGE` | Default language code for searches | "en" |
 
## 📚 API Usage
 
### Basic Search
 
```javascript
// Example using fetch
const response = await fetch('/api/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    query: 'artificial intelligence',
    numResults: 5,
    gl: 'us',
    hl: 'en',
    autocorrect: true
  }),
});
 
const data = await response.json();
console.log(data);
```
 
### Search Parameters
 
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `query` | string | Search query (required) | - |
| `numResults` | number | Number of results to return | 10 |
| `gl` | string | Country code (e.g., "us", "uk") | "us" |
| `hl` | string | Language code (e.g., "en", "es") | "en" |
| `autocorrect` | boolean | Enable autocorrect | true |
 
### Response Format
 
The search results include rich data:
 
```json
{
  "searchParameters": {
    "q": "artificial intelligence",
    "gl": "us",
    "hl": "en",
    "autocorrect": true
  },
  "knowledgeGraph": {
    "title": "Artificial intelligence",
    "type": "Computer science",
    "description": "Artificial intelligence is intelligence demonstrated by machines...",
    "attributes": {
      "Subdisciplines": "Machine learning, Natural language processing, Computer vision, MORE"
    }
  },
  "organic": [
    {
      "title": "What is Artificial Intelligence (AI)?",
      "link": "https://www.ibm.com/topics/artificial-intelligence",
      "snippet": "Artificial intelligence is the simulation of human intelligence processes by machines...",
      "position": 1
    }
  ],
  "peopleAlsoAsk": [
    {
      "question": "What is artificial intelligence in simple words?",
      "snippet": "Artificial intelligence is the ability of a computer or a robot...",
      "link": "https://www.example.com/ai-definition"
    }
  ],
  "relatedSearches": [
    {
      "query": "artificial intelligence examples"
    }
  ]
}
```
 
## 🔍 Response Types
 
### Knowledge Graph
 
Contains entity information when available:
- Title and type
- Website URL
- Description
- Key attributes
 
### Organic Results
 
List of search results including:
- Title and URL
- Snippet (description)
- Position in results
- Sitelinks when available
 
### People Also Ask
 
Common questions related to the search:
- Question text
- Answer snippet
- Source link
 
### Related Searches
 
List of related search queries users often make.
 
## 🧩 Integration with Other Tools
 
### LangChain Integration
 
This app can be easily integrated with LangChain for AI-powered applications:
 
```python
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
 
import os
 
os.environ["SERPER_API_KEY"] = "your_serper_api_key"
os.environ['OPENAI_API_KEY'] = "your_openai_api_key"
 
llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]
 
self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")
```
 
## 📊 Pricing
 
Serper offers a simple, affordable pricing model with a top-up system:
 
| Plan | Price | Credits | Cost per 1k queries |
|------|-------|---------|---------------------|
| Starter | $50 | 50,000 | $1.00 |
| Standard | $375 | 500,000 | $0.75 |
| Scale | $1,250 | 2,500,000 | $0.50 |
| Ultimate | $3,750 | 12,500,000 | $0.30 |
 
All plans include:
- Real-time results
- Customizable query location
- Credits valid for 6 months
 
## 🤝 Contributing
 
Contributions are welcome! Please feel free to submit a Pull Request.
 
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
 
## 📄 License
 
This project is licensed under the MIT License - see the LICENSE file for details.
 
## 🙏 Acknowledgments
 
- [Serper API](https://serper.dev/) for providing the Google search capabilities
- [LangChain](https://python.langchain.com/) for the integration examples
 
