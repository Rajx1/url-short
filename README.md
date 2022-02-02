# url-short
a url shortener, react front end and python backend

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.



# Run Demo

_NB: These instructions assume you have Pipenv installed within your current version of Python. For non-Pipenv users, a `requirements.txt` is provided, including dev dependencies._
- `pipenv shell`
- `pipenv install --dev`
- Run dev server with `pipenv run dev`
- Run prod server with `pipenv run start`
- Run tests with `pipenv run test`
- Get coverage report with `pipenv run coverage`

- Start mongodb docker container `docker run --name mongodb -d -p 27017:27017 mongo`
- Stop and remove docker `docker stop mongodb && docker container rm mongodb`

Available routes: \
`GET`, `POST`: `/api/cats` \
`GET`, `PATCH`, `PUT` ,`DELETE`: `/api/cats/:id`
