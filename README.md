# Random Joke Generator

A simple web application that fetches random jokes from a public API and displays them on a beautiful, interactive interface.

## Features

- Fetch random jokes using the [Official Joke API](https://official-joke-api.appspot.com/).
- Responsive and user-friendly interface styled with CSS.
- Built with Flask for the backend and HTML/CSS/JavaScript for the frontend.
- Easily deployable on platforms like Render, Heroku, or Vercel.

## Project Structure

```
random-joke-generator/
├── app.py          # Backend using Flask
├── static/
│   └── style.css   # CSS for styling
├── templates/
│   └── index.html  # HTML for the frontend
├── requirements.txt # Dependencies for the project
└── README.md       # Project documentation
```

## Requirements

- Python 3.7+
- Flask
- requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/random-joke-generator.git
   cd random-joke-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## Usage

1. Click the "Get Another Joke" button to fetch a random joke.
2. Enjoy the jokes or share them with friends!

## API Details

This app uses the [Official Joke API](https://official-joke-api.appspot.com/) to fetch jokes. The API provides random jokes in JSON format with the following structure:

```json
{
  "setup": "Why don't skeletons fight each other?",
  "punchline": "They don't have the guts."
}
```

## Customization

- **Style**: Modify `static/style.css` to change the look and feel of the app.
- **Logic**: Update the `app.py` file to fetch jokes from a different API or add new features.

## Deployment

You can deploy this app on:

- **Render**: [https://render.com/](https://render.com/)
- **Heroku**: [https://www.heroku.com/](https://www.heroku.com/)
- **Vercel**: [https://vercel.com/](https://vercel.com/)

Follow the platform-specific instructions to upload your project and run it in the cloud.

## Acknowledgments

- [Official Joke API](https://official-joke-api.appspot.com/) for providing the jokes.
- Flask for making backend development simple and elegant.

