# Statistical Data Visualization Platform

## Overview

This project is a web application that allows users to upload CSV or Excel files, which are then processed on the server-side using Python Flask. The processed data is visualized and displayed to the user. The front end is built using Next.js and Node.js.

## File Structure

project-root/
│
├── client/ # Frontend directory
│ ├── pages/ # Next.js pages
│ ├── public/ # Public static files
│ ├── styles/ # CSS styles
│ ├── components/ # React components
│ └── .gitignore # Git ignore file
│ └── package.json # Node.js dependencies and scripts
│
├── server/ # Backend directory
│ ├── app.py # Flask application
│ ├── requirements.txt # Python dependencies
│
└── .gitignore # Git ignore file

## Setup Instructions

### Frontend Setup

#### Navigate to the Client Directory\*\*:

```bash
cd client
```

#### Install Dependencies:

Ensure you have Node.js v18.17.0 or later installed. Run:

```bash
npm install
```

#### Run the Development Server:

```bash
npm run dev
```

The application will be available at http://localhost:3000.

### Backend Setup

#### Navigate to the Server Directory:

```bash
cd server
```

#### Set Up a Virtual Environment (optional but recommended)::

Ensure you have Python 3.8 or later installed. Run:

```bash
python -m venv venv
source venv/bin/activate
```

#### Install Dependencies:

```bash
pip install -r requirements.txt
```

#### Run the Flask Application:

```bash
python app.py
```

    The Flask application will be available at http://localhost:5000.

## Project Description

### Frontend:

    •	The frontend is built with Next.js and is responsible for providing a user interface where users can upload CSV or Excel files.
    •	Upon file upload, the frontend sends a POST request to the backend with the file.

### Backend:

    •	The backend is built with Flask and processes the uploaded files.
    •	It reads the file, performs data analysis, and generates visualizations (Curve Plot, Boxplot, Moments, and Heatmap).
    •	The visualizations are returned as images to the frontend.

### Visualizations:

    •	Curve Plot: Shows a line plot for the first numeric column.
    •	Boxplot: Displays the distribution of data through boxplots for numeric columns.
    •	Moments Plot: Visualizes statistical moments including mean, variance, skewness, and kurtosis.
    •	Heatmap: Shows the correlation matrix of numeric columns.

## Dependencies

### Frontend (client)

    •	Next.js
    •	React

### Backend (server)

    •	Flask
    •	Flask-CORS
    •	pandas
    •	matplotlib
    •	seaborn
    •	scipy
