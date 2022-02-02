# url-short
A url shortener, React frontend and Python backend with data stored to MongoDB.

- Users can submit a url and a server generated url will display.
- The generated url can be clicked on or can be copied to the clipboard

## Installation & Usage
- Clone the repo
- Navigate to the cloned folder

### Docker
- Navigate to the server folder
- Start a mongodb docker container `docker run --name mongodb -d -p 27017:27017 mongo`
- When finished stop and remove docker container `docker stop mongodb && docker container rm mongodb`

### Python server
_NB: These instructions assume you have Pipenv installed within your current version of Python. For non-Pipenv users, a `requirements.txt` is provided, including dev dependencies._
- Navigate to the server folder
- `pipenv shell`
- `pipenv install --dev`
- Run dev server with `pipenv run dev`

### React client
- Navigate to the client folder
- Run `npm install` to install dependencies
- Run `npm start`. Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.


## Wins & Challenges
- Managed to implement all functionality